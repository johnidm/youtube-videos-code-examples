-- Create produtos table

DROP TABLE IF EXISTS produtos;

CREATE TABLE produtos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert 30 sample products
INSERT INTO produtos (name, description) VALUES
('Smartphone Galaxy', 'Latest Android smartphone with advanced camera features'),
('Laptop Pro 15"', 'High-performance laptop for professionals and gamers'),
('Wireless Headphones', 'Noise-canceling Bluetooth headphones with premium sound'),
('Coffee Maker Deluxe', 'Programmable coffee maker with built-in grinder'),
('Gaming Mouse RGB', 'Precision gaming mouse with customizable RGB lighting'),
('Mechanical Keyboard', 'Cherry MX switches mechanical keyboard for typing enthusiasts'),
('4K Monitor 27"', 'Ultra HD monitor with HDR support and USB-C connectivity'),
('Fitness Tracker Pro', 'Advanced fitness tracker with heart rate and GPS monitoring'),
('Bluetooth Speaker', 'Portable waterproof speaker with 360-degree sound'),
('Electric Toothbrush', 'Smart toothbrush with app connectivity and multiple modes'),
('Air Fryer Digital', 'Large capacity air fryer with digital controls and presets'),
('Tablet 10" WiFi', 'Lightweight tablet perfect for reading and entertainment'),
('Wireless Charger', 'Fast wireless charging pad compatible with all Qi devices'),
('Smart Watch Series', 'Feature-rich smartwatch with health monitoring capabilities'),
('USB-C Hub 7-in-1', 'Multi-port hub with HDMI, USB 3.0, and SD card slots'),
('Webcam HD 1080p', 'High-definition webcam with auto-focus and noise reduction'),
('Power Bank 20000mAh', 'High-capacity portable charger with fast charging support'),
('Gaming Chair Ergonomic', 'Comfortable gaming chair with lumbar support and adjustability'),
('LED Desk Lamp', 'Adjustable LED lamp with multiple brightness levels and USB charging'),
('Microphone USB Studio', 'Professional USB microphone for streaming and recording'),
('External SSD 1TB', 'Fast portable SSD with USB 3.2 Gen 2 connectivity'),
('Router WiFi 6', 'Next-generation wireless router with advanced security features'),
('Action Camera 4K', 'Compact action camera with image stabilization and waterproof case'),
('Smart Home Hub', 'Central hub for controlling all your smart home devices'),
('Drone with Camera', 'Beginner-friendly drone with HD camera and GPS return-to-home'),
('VR Headset Gaming', 'Immersive virtual reality headset for gaming and entertainment'),
('Printer All-in-One', 'Wireless printer with scanning, copying, and faxing capabilities'),
('Smart Doorbell', 'Video doorbell with motion detection and two-way audio'),
('Electric Kettle Smart', 'Temperature-controlled electric kettle with app connectivity'),
('Portable Projector', 'Mini projector with WiFi connectivity and built-in speakers');