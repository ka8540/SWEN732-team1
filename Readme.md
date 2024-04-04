# Price Compare Plus - User Authentication Feature

## Overview

Price Compare Plus's User Authentication feature ensures a secure and personalized shopping experience for users. The system allows users to sign up, log in, and access their accounts, which enables them to use functionalities like searching for products, adding them to favorites, and maintaining a shopping cart.

## Features

### Sign Up

![Sign Up Page](images/SignUp.png)

The sign-up page is the entry point for new users. The process is straightforward, requesting essential information:

- First Name
- Last Name
- Email
- Username
- Password (hashed for security)
- Confirm Password

Form validations are in place to ensure data integrity. A session key is generated at this stage but remains null until the user logs in.
Passwords are hashed before storage.

### Log In

![Login Page](images/Login.png)

Returning users will authenticate themselves on the login page by entering their:

- Username
- Password

Upon successful authentication, a unique session key is generated to manage the user's session. The system includes protective measures such as validation checks that trigger generic error messages for improved user privacy.

- Incorrect Username
  - If a user enters a username that does not exist in the database, they will receive the following message:
  - **"Invalid username or password, please try again."**
- Incorrect Password
  - If a user enters a valid username but the wrong password, they will receive the same message as above:
  - **"Invalid password, please try again."**

### Home

![Home Page](images/Home_Page.png)

The home page serves as the main dashboard, featuring:

- A search bar for product queries.
- Navigation buttons for the Home, Favorites, Shopping Cart, and Account sections.
- Products Available for purchase eg. Phones,Headphones etc.

### Product

![Products](images/Products.png)
The Products page showcases a list of items available for comparison. Users can browse through the selection of phones and electronic devices, view detailed descriptions, and compare prices from different retailers.

featuring:

- Product Descriptions: Detailed insights into product features, specifications, and enhancements, allowing users to make informed decisions.
- Price Listing: Displays the current prices from various retailers, ensuring users can find the best deal.

### ProductDescription

![ProductsDescription](images/ProductDescription.png)
![ProductsRetailers](images/RetailerPrice.png)
The Product Description page provides in-depth information about each product, including camera specs, processor details, and other unique features.

featuring:

- Product Title.
- Product Image.
- Product Description.
- Retailers Available with their current Price.

### Shopping Cart

![Shopping Cart](images/ShoppingCart.png)

The shopping cart displays all the products that the user intends to purchase. Each product includes details like quantity and pricing.

### Account

![Account Section](images/Account.png)

The Account section displays the logged-in user's:

- Username
- First Name
- Last Name
- Email

A logout option is available for users to end their session. On logout, the session key is reset to null to maintain security, preventing unauthorized access and maintaining the privacy and integrity of the user's session.

---

### Coverage 
[![codecov](https://codecov.io/gh/ka8540/SWEN732-team1/graph/badge.svg?token=EDJ42TSNSN)](https://codecov.io/gh/ka8540/SWEN732-team1)

### LICENSE 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
`[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)`

