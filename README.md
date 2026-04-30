# Day 5: User Authentication

This project extends the blog application by adding user authentication features, including user registration, login, and logout.

## Features

-   **User Registration**: New users can sign up for an account.
-   **User Login/Logout**: Registered users can log in to access their accounts and log out when finished.
-   **Django's Built-in Auth**: Utilizes Django's `django.contrib.auth` for robust and secure authentication.
-   **Forms**: Implements Django forms for handling user input for registration and login.
-   **Views**:
    -   `register`: Handles the user registration process.
    -   `login_view`: Manages user login.
    -   `logout_view`: Logs the user out.
-   **Templates**: HTML templates for registration, login, and to display user-specific content.

## How to Run

1.  **Clone the repository.**
2.  **Navigate to the `Day_05_User_Auth` directory.**
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Assuming a requirements.txt file exists. If not, you will need to install Django)*
4.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
6.  Open your browser and go to `http://127.0.0.1:8000/accounts/register/` to create a new account.
7.  Go to `http://127.0.0.1:8000/accounts/login/` to log in.
