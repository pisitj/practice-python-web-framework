import requests

header = {}
header['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY3NDk1NzA2LCJqdGkiOiI1NzE0YzQ3ZWY1ZGU0MTUxYWIyYTZiN2U5ZmMwNGFhNyIsInVzZXJfaWQiOjF9.-wNWUHisd5f1Hiilm6JYzwLApqw4U9mWMciF-ycSTy8'

r = requests.get('http://127.0.0.1:8000/api/paradigm/', headers=header)

print(r.text)