#![allow(dead_code)]
tonic::include_proto!("store");

//use serde_derive::{Deserialize, Serialize};
use chrono::NaiveDateTime;

// Sqlx => Tonic
#[derive(sqlx::FromRow)]
pub struct StockInfo {
    pub uuid: String,
    pub store_id: i32,
    pub total_count: i32,
    pub reserved_count: i32,
    pub created_at: Option<NaiveDateTime>,
    pub updated_at: Option<NaiveDateTime>,
}
