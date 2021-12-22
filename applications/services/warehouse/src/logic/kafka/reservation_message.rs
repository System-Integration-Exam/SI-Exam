use crate::connection::sqlite_connection::get_db_pool;
use regex::Regex;
use sqlx;

pub struct ReservationMessage {
    item_id: String,
    status_command: String,
    store_id: String,
}


impl ReservationMessage {
    pub fn from_payload(payload: String) -> Self {
        let re = Regex::new(r"[ {}\x22]").unwrap();
        let payload_formatted = re.replace_all(payload.as_str(), "");
        let params: Vec<&str> = payload_formatted.split(",").collect();

        Self {
            item_id: params[0].replace("ItemId:", ""),
            status_command: params[1].replace("StatusCommand:", ""),
            store_id: params[2].replace("StoreId:", ""),
        }
    }
    pub async fn and_resolve(&self) -> anyhow::Result<()> {
        match self.status_command.as_str() {
            "Reserved" => self.increment().await,
            "Fulfilled" => self.collect().await,
            "Cancelled" => self.decrement().await,
            _ => self.unknown_message().await,
        };
        Ok(())
    }

    async fn increment(&self) {
        let pool = get_db_pool().await.unwrap();

        sqlx::query(
            r#"
            UPDATE stock_info
            SET reserved_count = reserved_count + 1
            WHERE uuid = $1 AND store_id = $2
        "#,
        )
        .bind(&self.item_id)
        .bind(&self.store_id)
        .execute(&pool)
        .await
        .expect("Could not increment reserved count");

        pool.close().await;
    }

    async fn decrement(&self) {
        let pool = get_db_pool().await.unwrap();

        sqlx::query(
            r#"
            UPDATE stock_info
            SET reserved_count = reserved_count - 1
            WHERE uuid = $1 AND store_id = $2
        "#,
        )
        .bind(&self.item_id)
        .bind(&self.store_id)
        .execute(&pool)
        .await
        .expect("Could not decrement reserved count");

        pool.close().await;
    }

    async fn collect(&self) {
        let pool = get_db_pool().await.unwrap();

        sqlx::query(
            r#"
            UPDATE stock_info
            SET (reserved_count, in_stock) = (reserved_count - 1, in_stock - 1)
            WHERE uuid = $1 AND store_id = $2
        "#,
        )
        .bind(&self.item_id)
        .bind(&self.store_id)
        .execute(&pool)
        .await
        .expect("Could not decrement reserved count");

        pool.close().await;
    }

    async fn unknown_message(&self) {
        println!("Unknown command: {}", self.status_command);
    }
}
