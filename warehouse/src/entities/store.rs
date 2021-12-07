#![allow(dead_code)]
tonic::include_proto!("store");

//use serde_derive::{Deserialize, Serialize};
use chrono::NaiveDateTime;

// Sqlx => Tonic
#[derive(sqlx::FromRow)]
pub struct StoreConverter {
    pub id: i32,
    pub address: String,
    pub phone_number: String,
    pub email: String,
    pub role: String,
    pub created_at: Option<NaiveDateTime>,
    pub updated_at: Option<NaiveDateTime>,
}

impl StoreConverter {
    pub fn to_read_response(&self) -> ReadStoreResponse {
        ReadStoreResponse {
            store: Some(StoreObject {
                address: self.address.clone(),
                phone_number: self.phone_number.clone(),
                email: self.email.clone(),
                created_at: self.created_at.unwrap().to_string(),
                updated_at: self.updated_at.unwrap().to_string(),
            }),
        }
    }
    pub fn to_store_object(&self) -> StoreObject {
        StoreObject {
            address: self.address.clone(),
            phone_number: self.phone_number.clone(),
            email: self.email.clone(),
            created_at: self.created_at.unwrap().to_string(),
            updated_at: self.updated_at.unwrap().to_string(),
        }
    }
    fn list_collect(store_vec: Vec<StoreConverter>) -> Vec<StoreObject> {
        let mut stores = vec![];
        for store in store_vec.into_iter() {
            stores.push(store.to_store_object());
        }
        stores
    }

    pub fn to_list_response(store_vec: Vec<StoreConverter>) -> ReadStoreListResponse {
        ReadStoreListResponse {
            store_list: StoreConverter::list_collect(store_vec),
        }
    }
}

#[derive(sqlx::FromRow)]
pub struct StoreManyToManyBook {
    pub store_id: i32,
    pub book_id: i32,
}

#[derive(sqlx::FromRow)]
pub struct StoreManyToManyVinyl {
    pub store_id: i32,
    pub vinyl_id: i32,
}
