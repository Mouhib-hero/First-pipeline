# Secure Web Application with Password Strength and Login Monitoring

This is a simple web application built using Python and Flask. The application provides user registration, secure login, and real-time feedback on password strength. It also logs login attempts for security monitoring and offers graphical visualization of login statistics.

## Features

- Password strength requirements (minimum length, uppercase, lowercase, digits, special characters) with real-time feedback.
- User registration and secure login using hashed passwords.
- Logging of login attempts with timestamps and usernames.
- Visualization of login attempts using a bar chart.
- Simple and user-friendly web interface.

## Prerequisites

- Python 3.x
- Flask
- Chart.js (for graphical login attempt visualization)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/secure-web-app.git
    ```

2. Install dependencies:

    ```bash
    pip install flask
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

- Register as a new user with a strong password that meets the specified requirements.
- Log in using the registered username and password.
- The application provides real-time feedback on password strength.
- View login attempt logs and visualizations by clicking on "View Login Attempt Logs" on the login page.

## Docker and Jenkins Integration

This project includes a Dockerfile and Jenkinsfile for seamless integration with Docker and Jenkins.

### Docker Integration

1. Ensure you have Docker installed.

2. Build the Docker image using the provided Dockerfile:

    ```bash
    docker build -t starprophecy/simplewebapp .
    ```

3. Run the Docker container:

    ```bash
    docker run -p 5000:5000 starprophecy/simplewebapp
    ```

### Jenkins Integration

1. Install Jenkins and set up a Jenkins job to automate the build and deployment of the Docker container.

2. Configure the Jenkins job to pull the latest code from your version control system (e.g., GitHub) and build the Docker image using the provided Jenkinsfile.

3. Use Jenkins to automate the deployment of the Docker container to your server. Ensure you have defined credentials for Docker Hub as specified in your Jenkinsfile.

### License

You are free to use, edit, and modify this code.
