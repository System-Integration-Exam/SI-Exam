CREATE TABLE IF NOT EXISTS store(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

