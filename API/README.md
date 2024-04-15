# Project Name
Bloggergyan

## Description
This project is a blog application built using Django and Django REST Framework.

## Installation and Setup
### Prerequisites
- Python 3
- Django 
- Django REST Framework

### Installation
1. Clone the repository:

2. Navigate to the project directory, Create and activate virtual env:
python3 -m venv venv
source venv/bin/activate (linux)

3. Install the required dependencies:
pip install -r requirements.txt
4. Apply database migrations:
python3 manage.py makemigrations
python3 manage.py migrate

### Running the Application
To run the application, execute the following command:
python3 manage.py runserver
The application will start running at `http://localhost:8000/`.

## API Endpoint Documentation
### Post Endpoints
## Register account
POST /register/
example:

{
    "username" : "gpranshu260",
    "password" : "pass123",
    "email" : "gpranshu260@gmail.com"
}
# login
POST /login/

{
    "username" : "gpranshu260",
    "password" : "pass123"
    
}
# after login we will get token like below. copy the token and use on header of Postman
# as key and value like this -
Authorization : Token f80f9f76caa2a780032ef521ab602800cedbd643

{
    "token": "f80f9f76caa2a780032ef521ab602800cedbd643"
}

# List Posts: 
GET /posts/
Returns a list of all posts.

# Create Post, Update Post:
POST /posts/
PUT /posts/<post_id>/   (updates posts)
  - Creates a new post.
  - Example request body:
   
    {
      "title": "New Post",
      "content": "This is a new post.",
      "author": "gpranshu260"
    }
 

# Retrieve Post:
GET /posts/<post_id>/
  - Retrieves details of a specific post.

# Delete Post:
DELETE /posts/<post_id>/
  - Deletes an existing post.

### Comment Endpoints
# List Comments:
GET /posts/<post_id>/comments/
  - Returns a list of comments for a specific post.
# Create Comment: 
POST /posts/<post_id>/comments/
  - Creates a new comment for a specific post.
  - Example request body:
   
    {
      "text": "This is a new comment.",
      "post" : <post_id>,
      "author" : "gpranshu260"
    }
    
# Like Post:
POST /posts/<post_id>/like

{
    "post" : <post_id>,
    "user" : "gpranshu260"
}
