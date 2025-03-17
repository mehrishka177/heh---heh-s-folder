-- 1. Create Database
CREATE DATABASE CapstoneDB;
USE CapstoneDB;

-- 2. Create Tables

-- Customers Table
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    City VARCHAR(50),
    JoinDate DATE
);

-- Products Table
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Price DECIMAL(10,2)
);

-- Orders Table
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- 3. Insert Sample Data

-- Insert Customers
INSERT INTO Customers (Name, Email, City, JoinDate) VALUES
('Alice Johnson', 'alice@example.com', 'New York', '2023-01-10'),
('Bob Smith', 'bob@example.com', 'Los Angeles', '2022-06-20'),
('Charlie Brown', 'charlie@example.com', 'Chicago', '2023-03-15');

-- Insert Products
INSERT INTO Products (ProductName, Category, Price) VALUES
('Laptop', 'Electronics', 800.00),
('Smartphone', 'Electronics', 600.00),
('Headphones', 'Accessories', 150.00);

-- Insert Orders
INSERT INTO Orders (CustomerID, ProductID, Quantity, OrderDate, TotalAmount) VALUES
(1, 1, 1, '2024-02-10', 800.00),
(2, 2, 2, '2024-02-15', 1200.00),
(3, 3, 3, '2024-03-01', 450.00);

-- 4. Querying the Data

-- a) Retrieve all customers from New York
SELECT * FROM Customers WHERE City = 'New York';

-- b) Get total sales amount per customer
SELECT Customers.Name, SUM(Orders.TotalAmount) AS TotalSpent
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY Customers.Name;

-- c) Find the most recent orders
SELECT * FROM Orders ORDER BY OrderDate DESC LIMIT 5;

-- d) Count the number of orders placed
SELECT COUNT(*) AS TotalOrders FROM Orders;

-- e) Get the most popular product (based on quantity sold)
SELECT Products.ProductName, SUM(Orders.Quantity) AS TotalSold
FROM Orders
JOIN Products ON Orders.ProductID = Products.ProductID
GROUP BY Products.ProductName
ORDER BY TotalSold DESC
LIMIT 1;