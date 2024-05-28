User Registration

This project implements a user registration feature using React for the front end and Flask for the back end.
Features

    Allows users to register by providing their personal information.
    Validates user input on the client side before submitting the registration form.
    Sends user data to the server using a POST request.
    Handles the registration process on the server side, including data validation and storage.
    Provides error handling for registration failures.

Front End (React)

The front end is implemented using React, a JavaScript library for building user interfaces. The registration form includes input fields for the user's first name, last name, age, phone number, email, and GPRS location. It also includes a checkbox for agreeing to the privacy policy.
Installation

To run the front end locally, navigate to the frontend directory and run the following commands:

bash

npm install
npm start

This will start the development server and open the application in your default web browser.
Usage

    Fill in the registration form with your personal information.
    Click the "Register" button to submit the form.
    If the registration is successful, you will be redirected to another page.
    If there are any errors, they will be displayed on the form.

Back End (Flask)

The back end is implemented using Flask, a micro web framework for Python. It includes an API endpoint for handling user registration.
Installation

To run the back end locally, navigate to the backend directory and run the following commands:

bash

pip install -r requirements.txt
python app.py

This will start the Flask development server.
API Endpoints

    /api/register/: Handles user registration. Expects a POST request with JSON data containing the user's information.

Technologies Used

    Front End: React, styled-components
    Back End: Flask, Flask-RESTful
    Database: SQLite
