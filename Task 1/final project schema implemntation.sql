
--creates stores table
CREATE TABLE stores (
    store_id INT PRIMARY KEY IDENTITY(1,1),
    store_location VARCHAR(255) NOT NULL,
    store_latitude FLOAT NOT NULL,
    store_longitude FLOAT NOT NULL
);


--creates reviews table
CREATE TABLE reviews (
    review_id INT PRIMARY KEY IDENTITY(1,1),
    store_id INT,
    review_date DATE,
    review_month INT,
    reviewer_country VARCHAR(255),
    review_title VARCHAR(255),
    review_text TEXT,
    review_rating INT,
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);



--populate tables from imported data

INSERT INTO stores (store_location, store_latitude, store_longitude)
SELECT DISTINCT store_location, latitude, longitude
FROM dbo.TeePublic_review$;


INSERT INTO reviews (store_id, review_date, review_month, reviewer_country, review_title, review_text, review_rating)
SELECT
    s.store_id,
    CAST(dbo.TeePublic_review$.year AS DATE),
    dbo.TeePublic_review$.month,
    dbo.TeePublic_review$.store_location,
    dbo.TeePublic_review$.title,
    dbo.TeePublic_review$.review,
    dbo.TeePublic_review$.[review-label]
FROM dbo.TeePublic_review$
JOIN stores s ON dbo.TeePublic_review$.store_location = s.store_location
    AND dbo.TeePublic_review$.latitude = s.store_latitude
    AND dbo.TeePublic_review$.longitude = s.store_longitude;



--view tables
	SELECT * FROM stores;


	SELECT * FROM reviews;
	

--Reviews with the Most Frequent Use of Certain Keywords (e.g., 'bad', 'poor')

SELECT review_id, review_title, review_text
FROM reviews
WHERE review_text LIKE '%bad%'
   OR review_text LIKE '%poor%'
   OR review_text LIKE '%terrible%'
ORDER BY review_id;

--Find the Most Active Store Locations by Number of Reviews


SELECT store_id, COUNT(review_id) AS total_reviews
FROM reviews
GROUP BY store_id
ORDER BY total_reviews DESC;

--All Reviews from a Specific Store Location

SELECT * 
FROM reviews
WHERE store_location = 'CA';


--Find the Most Active Store Locations by Number of Reviews
SELECT store_location, COUNT(review_id) AS total_reviews
FROM reviews
GROUP BY store_location
ORDER BY total_reviews DESC;