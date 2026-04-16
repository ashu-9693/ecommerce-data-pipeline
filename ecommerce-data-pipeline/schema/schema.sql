CREATE TABLE raw_events (
    event_time VARCHAR(30),
    event_type VARCHAR(20),
    product_id BIGINT,
    category_id BIGINT,
    category_code VARCHAR(100),
    brand VARCHAR(100),
    price DECIMAL(10,2),
    user_id BIGINT,
    user_session VARCHAR(100)
);