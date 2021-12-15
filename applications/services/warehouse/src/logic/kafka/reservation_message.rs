
pub struct ReservationMessage{
    item_id: String,
    status_command: String,
    store_id: String
}

impl ReservationMessage{
    pub fn from_payload(payload: String) -> Self{
        let params: Vec<&str> = payload.split(",").collect();

        Self{
            item_id: params[0].split(":").collect(),
            status_command: params[1].split(":").collect(),
            store_id: params[2].split(":").collect(),
        }

    }
}