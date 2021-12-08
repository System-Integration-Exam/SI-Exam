-- Add migration script here
CREATE TABLE IF NOT EXISTS store_m2m_vinyl(
    store_id INTEGER,
    vinyl_id INTEGER
);