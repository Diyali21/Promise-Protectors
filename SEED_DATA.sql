
CREATE TABLE venue(
venue_id INTEGER PRIMARY KEY,
name NVARCHAR(50) NOT NULL,
description NVARCHAR(500) NOT NULL,
max_guests INTEGER NOT NULL,
venue_image NVARCHAR(255) NOT NULL,
venue_price FLOAT NOT NULL);


CREATE TABLE users(
username NVARCHAR(25) PRIMARY KEY,
fullName NVARCHAR(50) NOT NULL,
email NVARCHAR(50) NOT NULL,
contact_no NVARCHAR(15) NOT NULL,
password NVARCHAR(200) NOT NULL);

CREATE TABLE wedding(
wed_id NVARCHAR(50) PRIMARY KEY,
no_guests INTEGER NOT NULL,
wed_date DATE NOT NULL,
total_price FLOAT NOT NULL,
username NVARCHAR(25) FOREIGN KEY REFERENCES users(username),
venue_id INTEGER FOREIGN KEY REFERENCES venue(venue_id)
);


CREATE TABLE insurance_cover(
cover_id INTEGER PRIMARY KEY,
cover_name NVARCHAR(50) NOT NULL,
cover_price FLOAT NOT NULL,
cover_description NVARCHAR(200) NOT NULL);

CREATE TABLE policy_user(
policy_id NVARCHAR(50) PRIMARY KEY,
wed_id NVARCHAR(50) FOREIGN KEY REFERENCES wedding(wed_id));

CREATE TABLE policy_cover(
policy_cover_id NVARCHAR(50) PRIMARY KEY,
policy_id NVARCHAR(50) FOREIGN KEY REFERENCES policy_user(policy_id),
cover_id INTEGER FOREIGN KEY REFERENCES insurance_cover(cover_id));

INSERT INTO insurance_cover VALUES
(1, 'Property Damage', 3000, 'Refers to accidental harm or destruction to property such as venues, decorations, or equipment that occurs during a wedding'),
(2, 'Guest Injury or Accident', 1500, 'Refers to unexpected harm or bodily injury to guests during the wedding'),
(3, 'Vendor No-Show', 2000, 'Refers to a situation where a hired vendor fails to appear or provide services as agreed upon'),
(4, 'Cancellation Coverage', 1000, 'Reimburses you if you need to cancel or postpone your wedding due to unforseen circumstances');

INSERT INTO venue VALUES
(1, 'Enchanted Garden', 'Imagine a place, where time stands still, and all that exists is the beauty of nature and the love you share. In this picturesque garden venue, the beauty of nature sets the stage for a romantic and unforgettable wedding celebration. Spend your special day surrounded by the sights, sounds, and scents of nature, your love will flourish, and your hearts will forever be entwined.',
200, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/62/53/c6/caption.jpg?w=1200&h=-1&s=1', 11500),
(2, 'Whispers of Love Banquet Hall', 'Envision getting married beneath soaring ceilings and sparkling chandeliers, surrounded by the opulence of a grand banquet hall. This majestic venue transforms into a fairytale setting, where luxurious textures, subtle lighting, and immpecable style converge to create an unforgettable celebration. As you dance beneath the stars, the banquet hall grandeur and magic will forever be etched in your hearts',
500, 'https://weddedwonderland.com/wp-content/uploads/2020/01/w9MAYKnQ.jpeg', 10500),
(3, 'Eternal Waves', 'Softly glowing sand, whispering waves, and endless blue horizons converge to create an enchanting beachside haven. As the warm breeze carries the sweet scent of saltwater and blooming beach flowers, your love will flourish in this serene coastal setting. With each gentle wave, the beach whispers secrets of forever, as you embark on your new journey together.',
100, 'https://image.wedmegood.com/resized-nw/1300X/wp-content/uploads/2018/12/Moving-Pictures.jpg', 8500),
(4, 'Savor the Moment', 'Within the warm, inviting ambiance of this restaurant venue, the savoury scents of exquisite cuisine, mingle with the sweetness of celebration. Soft lighting dances across rich textures, casting a golden glow on your special day, as the gentle hum of conversation and clinking glasses creates a joyful symphony. As you savor each moment, our restaurant venue transforms into an intimate haven, where love, laughter and delectable delights blend into an unforgettable feast for the senses',
300, 'https://www.arabiaweddings.com/sites/default/files/styles/max750/public/listing/2019/10/30/four_season.jpeg?itok=MbAzHwFh', 9500);
