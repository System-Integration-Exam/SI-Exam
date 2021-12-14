#![allow(dead_code, unused_imports)]

use crate::entities::{
    stock_info::StockInfo, store, store::StoreManyToManyBook, store::StoreManyToManyVinyl,
};
use crate::{connection::sqlite_connection::get_db_pool, entities::store::StoreConverter};
use serde_derive::{Deserialize, Serialize};

pub async fn create(
    request: store::CreateStoreRequest,
) -> anyhow::Result<store::CreateStoreResponse> {
    let pool = get_db_pool().await?;

    match sqlx::query(
        r#"
        INSERT INTO store (address, phone_number, email)
        VALUES( $1, $2, $3 )
        "#,
    )
    .bind(request.address)
    .bind(request.phone_number)
    .bind(request.email)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::CreateStoreResponse {
                msg: "201".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;

            Ok(store::CreateStoreResponse {
                msg: "500".to_owned().to_owned(),
            })
        }
    }
}

pub async fn read(request: store::ReadStoreRequest) -> anyhow::Result<store::ReadStoreResponse> {
    let pool = get_db_pool().await?;
    let store = sqlx::query_as::<_, store::StoreConverter>(
        r#"
        SELECT * FROM store WHERE id = $1
        "#,
    )
    .bind(request.id)
    .fetch_one(&pool)
    .await
    .expect("Could not read store");
    pool.close().await;

    Ok(store.to_read_response())
}

pub async fn read_store_by_address(
    request: store::ReadStoreByAddressRequest,
) -> anyhow::Result<store::ReadStoreByAddressResponse> {
    let pool = get_db_pool().await?;
    let store = sqlx::query_as::<_, store::StoreConverter>(
        r#"
        SELECT * FROM store 
        WHERE address = $1
        "#,
    )
    .bind(request.address)
    .fetch_one(&pool)
    .await
    .expect("Could not read store");
    pool.close().await;

    Ok(store::ReadStoreByAddressResponse {
        store: Some(store::StoreObject {
            address: store.address,
            phone_number: store.phone_number,
            email: store.email,
            created_at: store.created_at.unwrap().to_string(),
            updated_at: store.updated_at.unwrap().to_string(),
        }),
    })
}

pub async fn update(
    request: store::UpdateStoreRequest,
) -> anyhow::Result<store::UpdateStoreResponse> {
    let pool = get_db_pool().await?;

    match sqlx::query(
        r#"
        UPDATE store SET (address, phone_number, email) = ( $1, $2, $3)
        WHERE ID = $4
        "#,
    )
    .bind(request.address)
    .bind(request.phone_number)
    .bind(request.email)
    .bind(request.id)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::UpdateStoreResponse {
                msg: "204".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::UpdateStoreResponse {
                msg: "500".to_owned().to_owned(),
            })
        }
    }
}

pub async fn update_store_by_address(
    request: store::UpdateStoreByAddressRequest,
) -> anyhow::Result<store::UpdateStoreByAddressResponse> {
    let pool = get_db_pool().await?;

    match sqlx::query(
        r#"
        UPDATE store SET (address, phone_number, email) = ( $1, $2, $3)
        WHERE address = $4
        "#,
    )
    .bind(request.address_update)
    .bind(request.phone_number)
    .bind(request.email)
    .bind(request.address_match)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::UpdateStoreByAddressResponse {
                msg: "204".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::UpdateStoreByAddressResponse {
                msg: "500".to_owned().to_owned(),
            })
        }
    }
}

pub async fn delete(
    request: store::DeleteStoreRequest,
) -> anyhow::Result<store::DeleteStoreResponse> {
    let pool = get_db_pool().await?;
    match sqlx::query(
        r#"
        DELETE FROM store WHERE id = $1
        "#,
    )
    .bind(request.id)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::DeleteStoreResponse {
                msg: "200".to_owned().to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::DeleteStoreResponse {
                msg: "200".to_owned().to_owned(),
            })
        }
    }
}

pub async fn delete_store_by_address(
    request: store::DeleteStoreByAddressRequest,
) -> anyhow::Result<store::DeleteStoreByAddressResponse> {
    let pool = get_db_pool().await?;
    match sqlx::query(
        r#"
        DELETE FROM store WHERE address = $1
        "#,
    )
    .bind(request.address)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::DeleteStoreByAddressResponse {
                msg: "200".to_owned().to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::DeleteStoreByAddressResponse {
                msg: "200".to_owned().to_owned(),
            })
        }
    }
}

pub async fn read_list(
    _request: store::ReadStoreListRequest,
) -> anyhow::Result<store::ReadStoreListResponse> {
    let pool = get_db_pool().await?;
    let store = sqlx::query_as::<_, StoreConverter>(
        r#"
        SELECT * FROM store
        "#,
    )
    .fetch_all(&pool)
    .await
    .expect("Could not read list of store");

    pool.close().await;

    Ok(StoreConverter::to_list_response(store))
}

pub async fn add_book_to_store(
    request: store::AddBookToStoreRequest,
) -> anyhow::Result<store::AddBookToStoreResponse> {
    let pool = get_db_pool().await?;
    match sqlx::query(
        r#"
        INSERT INTO store_m2m_book(store_id, book_id)
        VALUES($1,$2)
    "#,
    )
    .bind(request.store_id)
    .bind(request.book_id)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::AddBookToStoreResponse {
                msg: "200".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::AddBookToStoreResponse {
                msg: "500".to_owned(),
            })
        }
    }
}

pub async fn remove_book_to_store(
    request: store::RemoveBookFromStoreRequest,
) -> anyhow::Result<store::RemoveBookFromStoreResponse> {
    let pool = get_db_pool().await?;

    match sqlx::query(
        r#"
        DELETE TOP 1 * FROM store_m2m_book
        WHERE store_id = $1 AND book_id = $2
    "#,
    )
    .bind(request.store_id)
    .bind(request.book_id)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::RemoveBookFromStoreResponse {
                msg: "200".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::RemoveBookFromStoreResponse {
                msg: "500".to_owned(),
            })
        }
    }
}

pub async fn get_amount_of_specific_book_from_store(
    request: store::GetAmountOfSpecificBookFromStoreRequest,
) -> anyhow::Result<store::GetAmountOfSpecificBookFromStoreResponse> {
    let pool = get_db_pool().await?;

    let matches = sqlx::query_as::<_, StoreManyToManyBook>(
        r#"
        SELECT * FROM store_m2m_book 
        WHERE store_id = $1 AND book_id = $2
        "#,
    )
    .bind(request.store_id)
    .bind(request.book_id)
    .fetch_all(&pool)
    .await?;

    Ok(store::GetAmountOfSpecificBookFromStoreResponse {
        amount: matches.len() as i32,
    })
}

pub async fn add_vinyl_to_store(
    request: store::AddVinylToStoreRequest,
) -> anyhow::Result<store::AddVinylToStoreResponse> {
    let pool = get_db_pool().await?;
    match sqlx::query(
        r#"
        INSERT INTO store_m2m_vinyl(store_id, vinyl_id)
        VALUES($1,$2)
    "#,
    )
    .bind(request.store_id)
    .bind(request.vinyl_id)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::AddVinylToStoreResponse {
                msg: "200".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::AddVinylToStoreResponse {
                msg: "500".to_owned(),
            })
        }
    }
}

pub async fn remove_vinyl_from_store(
    request: store::RemoveVinylFromStoreRequest,
) -> anyhow::Result<store::RemoveVinylFromStoreResponse> {
    let pool = get_db_pool().await?;

    match sqlx::query(
        r#"
        DELETE TOP 1 * FROM store_m2m_vinyl
        WHERE store_id = $1 AND vinyl_id = $2
    "#,
    )
    .bind(request.store_id)
    .bind(request.vinyl_id)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::RemoveVinylFromStoreResponse {
                msg: "200".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::RemoveVinylFromStoreResponse {
                msg: "500".to_owned(),
            })
        }
    }
}

pub async fn get_amount_of_specific_vinyl_from_store(
    request: store::GetAmountOfSpecificVinylFromStoreRequest,
) -> anyhow::Result<store::GetAmountOfSpecificVinylFromStoreResponse> {
    let pool = get_db_pool().await?;

    let matches = sqlx::query_as::<_, StoreManyToManyVinyl>(
        r#"
        SELECT * FROM store_m2m_vinyl 
        WHERE store_id = $1 AND vinyl_id = $2
        "#,
    )
    .bind(request.store_id)
    .bind(request.vinyl_id)
    .fetch_all(&pool)
    .await?;

    Ok(store::GetAmountOfSpecificVinylFromStoreResponse {
        amount: matches.len() as i32,
    })
}

pub async fn add_to_stock_info(
    request: store::AddToStockInfoRequest,
) -> anyhow::Result<store::AddToStockInfoResponse> {
    let pool = get_db_pool().await?;
    match sqlx::query(
        r#"
        INSERT INTO store_id(uuid, store_id, total_count, reserved_count)
        VALUES($1, $2, $3, $4)
    "#,
    )
    .bind(request.uuid)
    .bind(request.store_id)
    .bind(request.total_count)
    .bind(request.reserved_count)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::AddToStockInfoResponse {
                msg: "200".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::AddToStockInfoResponse {
                msg: "500".to_owned(),
            })
        }
    }
}

pub async fn remove_from_stock_info(
    request: store::RemoveFromStockInfoRequest,
) -> anyhow::Result<store::RemoveFromStockInfoResponse> {
    let pool = get_db_pool().await?;

    match sqlx::query(
        r#"
        DELETE FROM stock_info 
        WHERE uuid = $1 AND store_id = $2
    "#,
    )
    .bind(request.uuid)
    .bind(request.store_id)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::RemoveFromStockInfoResponse {
                msg: "200".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::RemoveFromStockInfoResponse {
                msg: "500".to_owned(),
            })
        }
    }
}

pub async fn read_stock_info(
    request: store::ReadStockInfoRequest,
) -> anyhow::Result<store::ReadStockInfoResponse> {
    let pool = get_db_pool().await?;

    let stock_info = sqlx::query_as::<_, StockInfo>(
        r#"
        SELECT * FROM store_m2m_vinyl 
        WHERE uuid = $1 AND store_id = $2
        "#,
    )
    .bind(request.uuid)
    .bind(request.store_id)
    .fetch_one(&pool)
    .await?;

    Ok(store::ReadStockInfoResponse {
        uuid: stock_info.uuid,
        store_id: stock_info.store_id,
        total_count: stock_info.total_count,
        reserved_count: stock_info.reserved_count,
        created_at: stock_info.created_at.unwrap().to_string(),
        updated_at: stock_info.updated_at.unwrap().to_string(),
    })
}

pub async fn increment_reserved_stock_info(
    request: store::IncrementReservedStockInfoRequest,
) -> anyhow::Result<store::IncrementReservedStockInfoResponse> {
    let pool = get_db_pool().await?;

    match sqlx::query(
        r#"
        UPDATE stock_info
        SET reserved_count = reserved_count + 1
        WHERE uuid = $1 AND store_info = $2
    "#,
    )
    .bind(request.uuid)
    .bind(request.store_id)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::IncrementReservedStockInfoResponse {
                msg: "200".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::IncrementReservedStockInfoResponse {
                msg: "500".to_owned(),
            })
        }
    }
}

pub async fn decrement_reserved_stock_info(
    request: store::DecrementReservedStockInfoRequest,
) -> anyhow::Result<store::DecrementReservedStockInfoResponse> {
    let pool = get_db_pool().await?;

    match sqlx::query(
        r#"
        UPDATE stock_info
        SET reserved_count = reserved_count - 1
        WHERE uuid = $1 AND store_info = $2
    "#,
    )
    .bind(request.uuid)
    .bind(request.store_id)
    .execute(&pool)
    .await
    {
        Ok(_) => {
            pool.close().await;
            Ok(store::DecrementReservedStockInfoResponse {
                msg: "200".to_owned(),
            })
        }
        Err(_) => {
            pool.close().await;
            Ok(store::DecrementReservedStockInfoResponse {
                msg: "500".to_owned(),
            })
        }
    }
}
