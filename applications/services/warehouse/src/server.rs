use rdkafka::util::get_rdkafka_version;
use store::store_server::{Store, StoreServer};
use store::{CreateStoreRequest, CreateStoreResponse};
use tonic::{transport::Server, Request, Response, Status};
use log::{info};

#[macro_use]
extern crate lazy_static;

mod connection;
mod entities;
mod logic;
mod utils;
mod tests;

use entities::store;
use logic::store_handler;

use utils::config::CONFIG;

use crate::logic::kafka::consumer::consume_and_print;
use crate::logic::kafka::logger::setup_logger;

#[derive(Default)]
pub struct StoreCon {}

#[tonic::async_trait]
impl Store for StoreCon {
    async fn create_store(
        &self,
        request: Request<CreateStoreRequest>,
    ) -> Result<Response<CreateStoreResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::create(request.into_inner())
                .await
                .expect("Store Creation failed"),
        ))
    }

    async fn read_store(
        &self,
        request: tonic::Request<store::ReadStoreRequest>,
    ) -> Result<tonic::Response<store::ReadStoreResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::read(request.into_inner())
                .await
                .expect("Store Read failed"),
        ))
    }

    async fn read_store_by_address(
        &self,
        request: tonic::Request<store::ReadStoreByAddressRequest>,
    ) -> Result<tonic::Response<store::ReadStoreByAddressResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::read_store_by_address(request.into_inner())
                .await
                .expect("Store Read failed"),
        ))
    }

    async fn update_store(
        &self,
        request: tonic::Request<store::UpdateStoreRequest>,
    ) -> Result<tonic::Response<store::UpdateStoreResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::update(request.into_inner())
                .await
                .expect("Store Update failed"),
        ))
    }

    async fn update_store_by_address(
        &self,
        request: tonic::Request<store::UpdateStoreByAddressRequest>,
    ) -> Result<tonic::Response<store::UpdateStoreByAddressResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::update_store_by_address(request.into_inner())
                .await
                .expect("Store Update failed"),
        ))
    }

    async fn delete_store(
        &self,
        request: tonic::Request<store::DeleteStoreRequest>,
    ) -> Result<tonic::Response<store::DeleteStoreResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::delete(request.into_inner())
                .await
                .expect("Store Delete failed"),
        ))
    }

    async fn read_store_list(
        &self,
        request: tonic::Request<store::ReadStoreListRequest>,
    ) -> Result<tonic::Response<store::ReadStoreListResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::read_list(request.into_inner())
                .await
                .expect("Store Read List failed"),
        ))
    }

    async fn add_book_to_store(
        &self,
        request: tonic::Request<store::AddBookToStoreRequest>,
    ) -> Result<tonic::Response<store::AddBookToStoreResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::add_book_to_store(request.into_inner())
                .await
                .expect("Store Read List failed"),
        ))
    }

    async fn remove_book_from_store(
        &self,
        request: tonic::Request<store::RemoveBookFromStoreRequest>,
    ) -> Result<tonic::Response<store::RemoveBookFromStoreResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::remove_book_to_store(request.into_inner())
                .await
                .expect("Store Read List failed"),
        ))
    }

    async fn get_amount_of_specific_book_from_store(
        &self,
        request: tonic::Request<store::GetAmountOfSpecificBookFromStoreRequest>,
    ) -> Result<tonic::Response<store::GetAmountOfSpecificBookFromStoreResponse>, tonic::Status>
    {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::get_amount_of_specific_book_from_store(request.into_inner())
                .await
                .expect("Store Read List failed"),
        ))
    }

    async fn add_vinyl_to_store(
        &self,
        request: tonic::Request<store::AddVinylToStoreRequest>,
    ) -> Result<tonic::Response<store::AddVinylToStoreResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::add_vinyl_to_store(request.into_inner())
                .await
                .expect("Store Read List failed"),
        ))
    }

    async fn remove_vinyl_from_store(
        &self,
        request: tonic::Request<store::RemoveVinylFromStoreRequest>,
    ) -> Result<tonic::Response<store::RemoveVinylFromStoreResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::remove_vinyl_from_store(request.into_inner())
                .await
                .expect("Store Read List failed"),
        ))
    }

    async fn get_amount_of_specific_vinyl_from_store(
        &self,
        request: tonic::Request<store::GetAmountOfSpecificVinylFromStoreRequest>,
    ) -> Result<tonic::Response<store::GetAmountOfSpecificVinylFromStoreResponse>, tonic::Status>
    {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            store_handler::get_amount_of_specific_vinyl_from_store(request.into_inner())
                .await
                .expect("Store Read List failed"),
        ))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = format!("{}:{}", CONFIG.server.host, CONFIG.server.port)
        .parse()
        .unwrap();

    println!(
        "Server running on: {}:{}",
        CONFIG.server.host, CONFIG.server.port
    );
    tokio::spawn(async move {
        setup_logger(true,Some(&CONFIG.kafka.consumer.log_conf));

        let (version_n, version_s) = get_rdkafka_version();
        info!("rd_kafka_version: 0x{:08x}, {}", version_n, version_s);
    
        let topics = CONFIG.kafka.consumer.topics.to_owned();
        let half_owned_topics: Vec<_> = topics.iter().map(String::as_str).collect();
        let group_id = "reservation".to_owned();
    
        consume_and_print(group_id.as_str(), &half_owned_topics).await
    });
    Server::builder()
        .add_service(StoreServer::new(StoreCon::default()))
        .serve(addr)
        .await
        .unwrap();
    Ok(())
}
