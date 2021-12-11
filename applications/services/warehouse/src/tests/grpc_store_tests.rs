use crate::utils::config::CONFIG;
lazy_static! {
    pub static ref SERVER_URI: String = {
        format!(
            "http://{}:{}",
            CONFIG.server.host, CONFIG.server.port
        )
    };
}

#[cfg(test)]
mod tests {
    #![allow(dead_code, unused_imports, unused_variables)]
    use tonic::transport::Channel;

    use super::*;
    use crate::entities::store;
    use crate::entities::store::store_client::StoreClient;

    async fn create_client() -> Result<StoreClient<Channel>, Box<dyn std::error::Error>> {
        Ok(StoreClient::connect(SERVER_URI.to_owned())
            .await
            .expect("sdf"))
    }

    #[tokio::test]
    async fn create_store() {
        let request = tonic::Request::new(store::CreateStoreRequest {
            address: "Some Address".to_owned(),
            phone_number: "29392912".to_owned(),
            email: "Some Email".to_owned(),
        });

        create_client()
            .await
            .expect("Could not create client in store tests")
            .create_store(request)
            .await
            .expect("Could not create store");
    }
}
