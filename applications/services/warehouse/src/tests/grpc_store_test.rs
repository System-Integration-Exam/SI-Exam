use crate::utils::config::CONFIG;
lazy_static! {
    pub static ref SERVER_URI: String =
        format!("http://{}:{}", CONFIG.server.host, CONFIG.server.port);
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
            address: "test_address".to_owned(),
            phone_number: "test phone number".to_owned(),
            email: "test_email".to_owned(),
        });

        let response = create_client()
            .await
            .expect("Could not create client in store tests")
            .create_store(request)
            .await
            .expect("Could not create store")
            .into_inner()
            .msg;

        assert_eq!(response, "201")
    }

    #[tokio::test]
    async fn update_store() {
        let request = tonic::Request::new(store::CreateStoreRequest {
            address: "update_by_address".to_owned(),
            phone_number: "test phone number".to_owned(),
            email: "test_email".to_owned(),
        });

        let response = create_client()
            .await
            .unwrap()
            .create_store(request)
            .await
            .unwrap()
            .into_inner()
            .msg;

        assert_eq!(response, "201");

        let request = tonic::Request::new(store::UpdateStoreByAddressRequest {
            address_match: "update_by_address".to_owned(),
            address_update: "address was updated".to_owned(),
            phone_number: "292921".to_owned(),
            email: "email@email.onion".to_owned(),
        });

        let response = create_client()
            .await
            .expect("Could not create client in store tests")
            .update_store_by_address(request)
            .await
            .expect("Could not update store")
            .into_inner()
            .msg;

        assert_eq!(response, "204");

        let request = tonic::Request::new(store::ReadStoreByAddressRequest {
            address: "address was updated".to_owned(),
        });

        let email_response = create_client()
            .await
            .expect("Could not create client in store tests")
            .read_store_by_address(request)
            .await
            .expect("Could not read store")
            .into_inner()
            .store
            .unwrap()
            .email;

        assert_eq!(email_response, "email@email.onion".to_owned())
    }

    #[tokio::test]
    async fn delete_store_by_address() {
        let request = tonic::Request::new(store::CreateStoreRequest {
            address: "address_to_delete".to_owned(),
            phone_number: "test phone number".to_owned(),
            email: "test_email".to_owned(),
        });

        let response = create_client()
            .await
            .unwrap()
            .create_store(request)
            .await
            .unwrap()
            .into_inner()
            .msg;

        assert_eq!(response, "201");

        let msg = create_client()
            .await
            .expect("Could not create client in store tests")
            .delete_store_by_address(tonic::Request::new(store::DeleteStoreByAddressRequest {
                address: "address_to_delete".to_owned(),
            }))
            .await
            .expect("Could not delete store")
            .into_inner()
            .msg;

        assert_eq!(msg, "200")
    }

    #[tokio::test]
    async fn read_store_by_address() {
        let request = tonic::Request::new(store::CreateStoreRequest {
            address: "address_to_read".to_owned(),
            phone_number: "test phone number".to_owned(),
            email: "test_email".to_owned(),
        });

        let response = create_client()
            .await
            .unwrap()
            .create_store(request)
            .await
            .unwrap()
            .into_inner()
            .msg;

        assert_eq!(response, "201");

        let msg = create_client()
            .await
            .expect("Could not create client in store tests")
            .read_store_by_address(tonic::Request::new(store::ReadStoreByAddressRequest {
                address: "address_to_read".to_owned(),
            }))
            .await
            .expect("Could not read store")
            .into_inner();

        let phone_number = msg.store.unwrap().phone_number;


        assert_eq!(phone_number, "test phone number")
    }

}
