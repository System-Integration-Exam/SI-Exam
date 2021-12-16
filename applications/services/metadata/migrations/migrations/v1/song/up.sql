CREATE TABLE IF NOT EXISTS song(
    id CHAR(36) PRIMARY KEY DEFAULT (lower(hex(randomblob(4))) || '-' || lower(hex(randomblob(2))) || '-4' || substr(lower(hex(randomblob(2))),2) || '-' || substr('89ab',abs(random()) % 4 + 1, 1) || substr(lower(hex(randomblob(2))),2) || '-' || lower(hex(randomblob(6)))),
    title VARCHAR(255),
    duration_sec INTEGER,
    vinyl_id CHAR(36),
    FOREIGN KEY(vinyl_id) REFERENCES vinyl(id) 
);

