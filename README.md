# movie_api
An API that allows users to create collections of their favourite movies

## Authentication:
Authentication in the APIs is done with the help of the simplejwt package. The endpoint `register/` returns the JWT access token upon the user's registration which can then be used to access the other APIs. Please note that as the access tokens are mainly used in the Authorization Header for the requests. Testing in this project was mainly done with the help of Postman, which allowed me to send requests with the Authorization header in the request.

## CRUD:
The CRUD functionality of the app works as expected and the responses are in the JSON format, and displayed with the help of GenericAPIView or APIViews.
For each request method and data object, there is a corresponding serializer that helps serialize and format the data so that it can be handled efficiently. For Example : GETCollections & POSTCollections
The model for this project is very simple, it just has one Collections class with the required data fields in it, as Movie data is not retrieved from a database, but from a third-party API.

## Middleware for request counting
The custom middleware designed, keeps track of the requests that come in with the help of a request attribute that keeps track of the number of requests recieved by the app. The assignment required me to try and implement a scalable concurrent middleware, and I tried to do that with threading. Unfortunately, when threading is involved, a new thread needs to be created everytime a request is received, which means that it is not the most scalable approach. Therefore, I reverted to using a standard approach, but would love to learn more about writing scalable middlewares.

## Installing and working on the project:
1. Create an environment for the project, here I'm using Conda
`conda create -n webdev python=3.10.6`
2. Activate the environment 
`conda activate webdev`
3. Install the python dependencies for the project
`pip install -r requirements.txt`
4. Clone the repo and use the `cd` command to change directories
5. Run the django web server locally
`python manage.py runserver`

