CREATE TABLE cars (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    model VARCHAR(255),
    year INT,
    price FLOAT
);

INSERT INTO cars (name, model, year, price) VALUES
('Toyota', 'Camry', 2019, 24000),
('Honda', 'Civic', 2018, 22000),
('Ford', 'Mustang', 2020, 30000),
('Chevrolet', 'Impala', 2017, 26000),
('BMW', '320i', 2021, 35000),
('Audi', 'A4', 2019, 33000),
('Mercedes', 'C-Class', 2020, 38000),
('Hyundai', 'Elantra', 2018, 19000),
('Nissan', 'Altima', 2017, 20000),
('Subaru', 'Outback', 2019, 27000),
('Kia', 'Optima', 2020, 23000),
('Volkswagen', 'Jetta', 2018, 21000),
('Lexus', 'ES 350', 2019, 34000),
('Jaguar', 'XE', 2020, 37000),
('Porsche', '911', 2018, 60000),
('Land Rover', 'Range Rover', 2019, 70000),
('Chrysler', '300', 2017, 25000),
('GMC', 'Sierra', 2021, 40000),
('Jeep', 'Grand Cherokee', 2018, 29000),
('Mazda', 'CX-5', 2019, 22000);

-- 1. Retrieve All Cars
SELECT * FROM cars;

-- 2. Search by Year
SELECT * FROM cars
WHERE year = 2018;

-- 3. Find Expensive Cars
SELECT * FROM cars
WHERE price > 20000;

-- 4. Count Cars by Name
SELECT name, COUNT(*) AS count
FROM cars
GROUP BY name;

-- 5. Average Price by Year
SELECT year, AVG(price) AS average_price
FROM cars
GROUP BY year;

-- 6. Find the Most Expensive Car
SELECT * FROM cars
ORDER BY price DESC
LIMIT 1;

-- 7. Cars within Price Range
SELECT * FROM cars
WHERE price BETWEEN 15000 AND 30000;

-- 8. Update Car Price
UPDATE cars
SET price = price * 1.10
WHERE year < 2015;

-- 9. Delete Old Cars
DELETE FROM cars
WHERE year < (YEAR(CURDATE()) - 10);

-- 10. Complex Query: Most Expensive Car for Each Year
SELECT year, name, model, price
FROM cars
WHERE price = (
    SELECT MAX(price)
    FROM cars AS sub
    WHERE sub.year = cars.year
);

-- 11. Complex Query 2: Average Price of Cars for Each Name with More Than Three Entries
SELECT name, AVG(price) AS average_price
FROM cars
GROUP BY name
HAVING COUNT(*) > 3;