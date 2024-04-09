DROP TABLE IF EXISTS UserFavorites CASCADE;
DROP TABLE IF EXISTS ProductReviews CASCADE;
DROP TABLE IF EXISTS PriceAlerts CASCADE;
DROP TABLE IF EXISTS Prices CASCADE;
DROP TABLE IF EXISTS Products CASCADE;
DROP TABLE IF EXISTS Retailers CASCADE;
DROP TABLE IF EXISTS ProductCategories CASCADE;
DROP TABLE IF EXISTS user_authentication CASCADE;
DROP TABLE IF EXISTS Currency CASCADE;


-- Create Product User Authentication Table
CREATE TABLE user_authentication (
    user_id SERIAL PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    session_key VARCHAR(255) UNIQUE
);


-- Create Product Categories Table
CREATE TABLE ProductCategories (
    CategoryID SERIAL PRIMARY KEY,
    CategoryName VARCHAR(255) UNIQUE NOT NULL
);

-- Create Products Table
CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription TEXT,
    CategoryID INT,
    ImageURL TEXT,
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL
);

-- Create Retailers Table
CREATE TABLE Retailers (
    RetailerID SERIAL PRIMARY KEY,
    RetailerName VARCHAR(255) UNIQUE NOT NULL,
    WebsiteURL TEXT
);

-- Create Prices Table
CREATE TABLE Prices (
    PriceID SERIAL PRIMARY KEY,
    ProductID INT NOT NULL,
    RetailerID INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Currency VARCHAR(3) NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (RetailerID) REFERENCES Retailers(RetailerID) ON DELETE CASCADE
);

-- Create User Favorites Table
CREATE TABLE UserFavorites (
    FavoriteID SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    ProductID INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_authentication(user_id) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create Product Reviews Table
CREATE TABLE ProductReviews (
    ReviewID SERIAL PRIMARY KEY,
    ProductID INT NOT NULL,
    user_id INT NOT NULL,
    Rating INT CHECK (Rating >= 1 AND Rating <= 5),
    ReviewText TEXT,
    ReviewDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user_authentication(user_id) ON DELETE CASCADE
);

-- Optional: Create Currency Table
CREATE TABLE Currency (
    CurrencyID SERIAL PRIMARY KEY,
    CurrencyCode VARCHAR(3) UNIQUE NOT NULL,
    CurrencyName VARCHAR(255) NOT NULL
);

-- Optional: Create Price Alerts Table
CREATE TABLE PriceAlerts (
    AlertID SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    ProductID INT NOT NULL,
    ThresholdPrice DECIMAL(10, 2) NOT NULL,
    IsActive BOOLEAN NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_authentication(user_id) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);
