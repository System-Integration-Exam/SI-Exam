use serde_derive::Deserialize;
use std::error::Error;
use std::fs;

lazy_static! {
    static ref CONFIG_PATH: &'static str = "config.toml";
    pub static ref CONFIG: Config =
        read_config_file(&CONFIG_PATH).expect("Config file could not be read at lazy static");
}

#[derive(Deserialize)]
pub struct Config {
    pub server: Server,
    pub database: Database,
    pub kafka: Kafka,
}

#[derive(Deserialize)]
pub struct Server {
    pub port: u32,
    pub host: String,
}

#[derive(Deserialize)]
pub struct Database {
    pub db: String,
}

#[derive(Deserialize)]
pub struct Kafka {
    pub bootstrap_servers: String,
    pub producer: Producer,
    pub consumer: Consumer,
}

#[derive(Deserialize)]
pub struct Producer {
    pub message_timeout_ms: String,
    pub log_conf: String,
}

#[derive(Deserialize)]
pub struct Consumer {
    pub enable_partition_eof: String,
    pub enable_auto_commit: String,
    pub session_timeout_ms: String,
    pub log_conf: String,
    pub topics: Vec<String>,
}

fn read_config_file(path: &str) -> Result<Config, Box<dyn Error>> {
    let file_contents: String = fs::read_to_string(path)?;
    let config: Config = toml::from_str(&file_contents)?;
    Ok(config)
}
