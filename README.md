# rishat_test

### Test project for vacancy

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info

This project is the simple store with stripe pay system :smiley_cat:.
	
## Technologies

Project is created with:
 * asgiref==3.6.0
 * certifi==2022.12.7
 * charset-normalizer==3.0.1
 * Django==4.1.6
 * djangorestframework==3.14.0
 * idna==3.4
 * python-dotenv==0.21.1
 * pytz==2022.7.1
 * requests==2.28.2
 * sqlparse==0.4.3
 * stripe==5.1.1
 * tzdata==2022.7
 * urllib3==1.26.14

	
## Setup

### First step: create .env file with generated DJANGO_SECRET_KEY and add yours stripe api token as STRIPE_TOKEN and add yours server address as SERVER_ADDRESS.
To run this project, install it locally using docker:
```
$ cd //yours_project_path//
$ cd ../infra/
$ docker-copose up -d --build
```

## Autors

![Stepanov Aleksndr](https://github.com/Funnysuslik)
