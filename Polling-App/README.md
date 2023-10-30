# Django Polling App

## Overview

The Django Polling App is a web application built with Django, allowing users to create, manage, and vote on polls in real-time. This README provides an overview of the project, its features, and how to get it up and running.

## Features

- User Authentication: Users can create and manage polls by signing in.
- Real-time Results: As users cast their votes, the results are updated in real-time.
- Database Management: Data is managed using Django's Object-Relational Mapping (ORM) and stored in a SQLite database.
- Responsive Design: The app is designed to work on various screen sizes, including mobile devices.
- User-friendly Interface: A clean and intuitive user interface makes it easy for users to participate in polls.

## Getting Started

1. **Installation**: Clone the repository and install the required dependencies.

   ```bash
   git clone https://github.com/don-reji/Django-Projects.git
   ```
   ```bash
   cd Polling-App
   pip install -r requirements.txt
2. **Run Migrations**
   Apply database migrations to create the necessary tables.
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```   
3. **Create a Superuser:** 
Create an admin superuser to manage the application.
   ```bash
   python manage.py createsuperuser
   ```
4. **Run the Application:** Start the Django development server.
   ```bash
   python manage.py runserver
   ```
5. **Access the App:** Open a web browser and navigate to http://localhost:8000/polls to access the app. The admin panel is available at http://localhost:8000/admin/.
## Acknowledgments
Special thanks to the Django community for their fantastic documentation and resources from which this app was built.
