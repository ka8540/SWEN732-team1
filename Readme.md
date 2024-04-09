# PROJECT Design Documentation

[![codecov](https://codecov.io/gh/ka8540/SWEN732-team1/graph/badge.svg?token=EDJ42TSNSN)](https://codecov.io/gh/ka8540/SWEN732-team1)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Name: Price Compare Plus

## Team Information

- Team name: TEAM 1
- Team members
  - Kush Jayesh Ahir
  - Love Jayesh Ahir
  - Shridhar Vilas Shinde
  - Bharathi Pandurangan

## Executive Summary

The "Price Compare Plus" project is to provide a mobile application that gives consumers access to product details and price comparisons from different online merchants. It provides customers with a comprehensive tool to locate the cheapest prices on a variety of items by centralizing data from several sources. The program aims to improve the online shopping experience by providing access to comprehensive product descriptions, reviews, and price notifications, which will facilitate informed decision-making.

## Documentation

https://github.com/ka8540/SWEN732-team1/blob/master/DesignDoc.md


## Minimum Requirements

1. Node.js (React-Native)
2. PostgreSQL
3. Python Flask(python 9.0 or higher)

## How to Run "Price Compare Plus"

Running "Price Compare Plus" involves setting up both the backend (Flask) and the frontend (React Native) components. This guide assumes you have Python and Node.js installed on your system. Follow these steps to get the application up and running:

### Backend Setup (Flask)

1. **Clone the Repository**: First, clone the project repository to your local machine using Git.

   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   
2. **Create a Virtual Environment**: It's recommended to create a virtual environment for Python projects to manage dependencies effectively.
    python -m venv venv
    Activate the virtual environment:
    - On Windows:
      ```
      .\venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source venv/bin/activate
      ```
3. **Install Dependencies**: Install all required Python packages for the backend.
     pip install -r requirements.txt
    
4. **Start the Flask Server**: Run the Flask application.
     python src/server.py

   This command starts the backend server, typically running on `http://localhost:5000`.

### Frontend Setup (React Native)

  1. **Install Expo CLI**: Expo CLI is a command-line utility for React Native. Install it globally using npm.
        npm install -g expo-cli
  2. **Install Dependencies**: Navigate to the frontend directory and install the required npm packages.
        cd path/to/your/frontend/directory
        npm install
  3. **Start the Expo Development Server**: Run the following command to start the Expo development server.
        expo start
     This command will open a new tab in your default web browser with the Expo developer tools. You can run the app on a simulator or on a physical device by scanning the QR code.

## Testing

### Overview

Testing is a critical part of the "Price Compare Plus" project development process, ensuring the reliability, security, and performance of the application. Our testing strategy encompasses various aspects of the application, including API endpoints, user authentication processes (sign up, sign in, sign out), and product-related functionalities (category API, product API, etc.). By adopting a comprehensive testing approach, we aim to identify and mitigate potential issues early in the development cycle, enhancing the overall quality of the application.

### Testing Framework and Tools

We utilize Python's `unittest` framework, a powerful and versatile tool for developing automated tests. This choice allows us to write clear and concise test cases, leveraging features such as test discovery, test fixtures, and assertions to verify our code's correctness. Additionally, the `unittest.mock` module is extensively used to isolate tests from their external dependencies, enabling us to simulate various scenarios and responses from external services and APIs.

### Mocking and Patching

A significant aspect of our testing methodology involves the use of mocking and patching techniques, facilitated by the `unittest.mock` module. This approach allows us to create mock objects that simulate the behavior of real-world entities, such as HTTP responses from external APIs. By patching parts of our system during tests, we can control the inputs and outputs of various components, ensuring that our tests are not only fast and reliable but also independent of external factors.

### Test Case Structure

Our test cases are methodically structured to cover a wide range of scenarios, including positive flows, error handling, and edge cases. For instance, the `SignUpApiTestCase` class contains tests for user registration, where we simulate both successful sign-ups and various failure scenarios (e.g., invalid inputs, duplicate users). Similarly, test cases for sign in, sign out, category management, and product functionalities are designed to validate each endpoint's expected behavior under different conditions.

### Continuous Integration and Deployment

Integration with Continuous Integration (CI) tools forms an integral part of our testing strategy. Upon each code commit, our test suite is automatically executed, allowing us to detect and resolve issues early in the development process. This automated pipeline ensures that all new changes are thoroughly tested before they are merged into the main branch, maintaining the integrity and stability of our codebase.

### Code Coverage

We strive to achieve high code coverage with our tests, ensuring that a significant portion of our codebase is verified for correctness. Tools such as Codecov are integrated into our CI pipeline, providing detailed insights into our testing coverage and highlighting areas that may require additional testing. This practice helps us maintain a robust and reliable codebase, reducing the likelihood of bugs and regressions in production.

### Conclusion

Our testing approach emphasizes thoroughness, automation, and continuous improvement. By leveraging advanced testing frameworks and methodologies, we ensure that "Price Compare Plus" meets the highest standards of quality and reliability. This commitment to quality testing reflects our dedication to providing a seamless and secure shopping comparison experience for our users.



