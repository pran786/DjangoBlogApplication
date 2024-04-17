import requests

# User credentials
username = 'gpranshu'
password = 'Password@123'

# API endpoints
login_url = 'http://localhost:8000/api/login/'
create_post_url = 'http://localhost:8000/posts/create/'

# Login to obtain authentication token
login_data = {'username': username, 'password': password}
response = requests.post(login_url, data=login_data)
token = response.json().get('token')
print(token)
# Create post with authentication token
post_data = {'title': 'New Post', 'content': 'Content of the new post'}
headers = {'Authorization': f'Token {token}'}
response = requests.post(create_post_url, data=post_data, headers=headers)

# Check the response
if response.status_code == 201:
    print('Post created successfully!')
else:
    print(response.text)
    print('Failed to create post.')
