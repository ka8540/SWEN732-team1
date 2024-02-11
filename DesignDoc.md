
# PROJECT Design Documentation

Project Name: Price Compare Plus

## Team Information
* Team name: TEAM 1
* Team members
  * Kush Jayesh Ahir 
  * Love Jayesh Ahir
  * Shridhar Vilas Shinde
  * Bharathi Pandurangan

## Executive Summary

The "Price Compare Plus" project is to provide a mobile application that gives consumers access to product details and price comparisons from different online merchants. It provides customers with a comprehensive tool to locate the cheapest prices on a variety of items by centralizing data from several sources. The program aims to improve the online shopping experience by providing access to comprehensive product descriptions, reviews, and price notifications, which will facilitate informed decision-making.


## Requirements

This section describes the features of the application.

### Definition of MVP
The "Price Compare Plus" MVP is a mobile application that enables users to browse product details, compare prices from various online merchants, search for items, save favorites, and get alerts when prices drop.


### MVP Features
1. User Authentication: Implement user registration and login functionality to allow users to create accounts and log in securely.
2. Product Search: Enable users to search for products by name using a search bar or a search function.
3. Product Details Display: Display detailed information about each product, including its features, specifications, and descriptions.
4. Price Comparison: Gather pricing information for the searched product from different online retailers and display them in a comparative format.
5. Save Favorites: Allow users to save products they're interested in, to a favorites list for easy access later.
6. Product Reviews: Integrate product review functionality to provide users with insights from other consumers' experiences.
7.  Sort and Filter Options: Provide users with the ability to sort search results by criteria such as price, relevance, or ratings, and filter results based on factors like brand, price range, or availability.
8. Product Image Display: Show images of the searched product to help users identify it visually.
9. Basic User Interface (UI): Create a simple intuitive user interface with essential components such as search bar, product display area, and navigation menu.
10. Responsive Design: Ensure that the app is responsive and works well on various mobile devices and screen sizes.
11. Currency Conversion: Incorporate currency conversion functionality to allow users to view prices in their preferred currency. This feature can be especially useful for users who shop across different regions or countries.
12. Price Drop Notifications: Enable users to receive notifications when the prices of their saved favorite products drop below a specified threshold. This feature allows users to take advantage of discounts and promotions without constantly monitoring prices themselves.



## Architecture and Design

This section describes the application architecture.

### Software Architecture
[Architecture Design](images/A_Design.jpg)

The "Price Compare Plus" application employs a microservices architecture to enable robust, scalable online shopping features. The architecture is delineated into several key components:

- **Mobile App**: The front-end interface that interacts with users, pushing alerts and sending user requests.
- **Microservices**: Decomposed backend services, including:
  - **Notification Service**: Manages and sends notifications to users.
  - **Favorites Service**: Handles the management of user favorites.
  - **Price Comparison Service**: Fetches and compares prices from various sources.
  - **User Service**: Responsible for authentication and user management.
  - **Product Service**: Manages product search and details retrieval.
- **External APIs**: Interfaces with Currency Conversion API and Retailer APIs to update product information and facilitate currency conversion.
- **API Gateway**: Acts as the entry point for all client requests, routing them to the appropriate microservice and providing security measures like rate limiting.
- **SQL Database**: Stores user data including credentials and profiles.
- **NoSQL Database**: Holds product-related data such as price data and favorites for quick retrieval.

The architecture supports both RESTful services and third-party API integration, ensuring that product information is current and accurate. The use of both SQL and NoSQL databases caters to the efficient management of structured and unstructured data respectively.



### Use Cases
> _Place a use case diagram here._
> _Describe your use case diagram._


### Class Diagram
> _Place a class diagram here._
> _Describe your class diagram._
