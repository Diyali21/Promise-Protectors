CREATE TABLE venue(
venue_id INTEGER PRIMARY KEY,
name NVARCHAR(50) NOT NULL,
description NVARCHAR(500) NOT NULL,
max_guests INTEGER NOT NULL,
venue_image NVARCHAR(255) NOT NULL,
venue_price FLOAT NOT NULL);


CREATE TABLE users(
username VARCHAR(25) PRIMARY KEY,
fullName VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
contact_no VARCHAR(15) NOT NULL,
password VARCHAR(100) NOT NULL);

CREATE TABLE wedding(
wed_id INTEGER PRIMARY KEY,
no_guests INTEGER NOT NULL,
wed_date DATE NOT NULL,
venue_name VARCHAR(50),
total_price FLOAT NOT NULL,
username VARCHAR(25) FOREIGN KEY REFERENCES users(username)
);

CREATE TABLE insurance_cover(
cover_id INTEGER PRIMARY KEY,
cover_name NVARCHAR(50) NOT NULL,
cover_price FLOAT NOT NULL);

INSERT INTO insurance_cover VALUES
(1, 'Property Damage', 3000),
(2, 'Guest Injury or Accident', 1500),
(3, 'Vendor No-Show', 2000),
(4, 'Cancellation Coverage', 1000);

INSERT INTO venue VALUES
(1, 'Enchanted Garden', 'Imagine a place, where time stands still, and all that exists is the beauty of nature and the love you share. In this picturesque garden venue, the beauty of nature sets the stage for a romantic and unforgettable wedding celebration. Spend your special day surrounded by the sights, sounds, and scents of nature, your love will flourish, and your hearts will forever be entwined.', 200, 'https://forbetterforworse.co.uk/wp-content/uploads/2013/07/Manor-by-the-lake-italian-pavilion-ceremony-.jpg', 50000),
(2, 'Whispers of Love Banquet Hall', 'Envision getting married beneath soaring ceilings and sparkling chandeliers, surrounded by the opulence of a grand banquet hall. This majestic venue transforms into a fairytale setting, where luxurious textures, subtle lighting, and immpecable style converge to create an unforgettable celebration. As you dance beneath the stars, the banquet hall grandeur and magic will forever be etched in your hearts', 500, 'https://media.weddingz.in/images/16ab8276a8bfa26550f679e8e6963687/best-wedding-reception-halls-in-patna-you-will-absolutely-fall-in-love-with.jpg', 100000),
(3, 'Eternal Waves', 'Softly glowing sand, whispering waves, and endless blue horizons converge to create an enchanting beachside haven. As the warm breeze carries the sweet scent of saltwater and blooming beach flowers, your love will flourish in this serene coastal setting. With each gentle wave, the beach whispers secrets of forever, as you embark on your new journey together.', 100, 'https://img.freepik.com/premium-photo/wedding-arch-with-flowers-beach_640852-4147.jpg', 30000),
(4, 'Savor the Moment', 'Within the warm, inviting ambiance of this restaurant venue, the savoury scents of exquisite cuisine, mingle with the sweetness of celebration. Soft lighting dances across rich textures, casting a golden glow on your special day, as the gentle hum of conversation and clinking glasses creates a joyful symphony. As you savor each moment, our restaurant venue transforms into an intimate haven, where love, laughter and delectable delights blend into an unforgettable feast for the senses', 300, 'https://weddingvenuemap.com/wp-content/uploads/2018/12/Ceviche-Tapas-Bar-and-Restuarant-Top-Restaurant-Wedding-Venue-A-Magic-Moment-2.jpg', 70000);
