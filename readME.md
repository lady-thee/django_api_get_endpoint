# TITLE

API Endpoint for GET request. 

## Introduction

This project is the stage one task for the HNGX Internship 2023. It is a simple API endpoint
that takes two parameters in it's query request and returns a JSON object with the current author(ME) details
concerning the internship. It was created with Django/ Django Rest Framework. 

## Objective

Create and host an endpoint using any programming language of choice. The endpoint should take two GET request
query parameters and return specific information in JSON format. 
### Expected Results: 
The JSON Format should have the following:
1. Slack name: name of the author on the HNG slack channel
2. Current day of the week (eg: Saturday, Monday)
3. Current UTC time (with validation of +/-2, i.e, 2 hours into the future and 2 hours behind the current UTC time)
4. Track (i.e; Backend, Frontend, Figma, etc)
5. The GitHub URL of the file being run (In this case would be the `views.py` file in the `api/` sub directory)
6. The GitHub URL of the full source code
7. A status code of success.

## Requirements

1. Django
2. Django Rest Framework
3. Docker
4. Virtual environment to handle dependencies(Pipenv or pip)


## How it works

It's pretty simple. using the link below, 
[https://hng-s1-xdeg.onrender.com/api/?slack_name=Theola%20Onuh&track=backend]
You can access the information in the GET endpoint request. 

## Hosting Platform:
The project was hosted using [render.com]
