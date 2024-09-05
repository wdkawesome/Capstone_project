
# my_page Django Project

This README provides instructions on how to build and run the MyPage Django project with virtual environments (`venv`) and Docker. 

##Description
Creating a small website using django, with at least 3 pages, at least 1 data base deriven

## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- Python 3.x
- Django (installed in your virtual environment)
- Docker (if using Docker for containerization)

## Project Structure

Your project structure should look like this:
L3T10
├── Webpage/
├── gitignore
├── Dockerfile
├── manage.py
├── requirements.txt

## Getting Started
To get a local copy up and running, follow these simple steps.
```bash
git clone <repository_url>

##Create virtual environments(optional)
# Navigate to your project directory
cd <project_directory>
# Create a virtual environment (Python 3.8+ recommended)
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

##Install project dependencies:
pip install -r requirements.txt

##Apply migrations:
python manage.py migrate

##Start the Django development server:
python manage.py runserver
Access your application in your web browser at http://localhost:8000

##Running with Docker
Build the Docker image (assuming you have a Dockerfile in your project root):
docker build -t my-django-app .
Run the Docker container:
docker run -d -p 8000:8000 my-django-app
Access your application in your web browser at http://localhost:8000.
If your application requires environment variables, create a .env file 






