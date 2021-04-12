# Neighbourhood

## Author
NGENOH ZEPHENIA

## Description
This is web application that allows user to be in the loop about everything happening in their neighborhood.User is able to sign up and be able to view different neighbourhoods,join,leave and view details for their neighbourhood.


## Feature
* User is able to sign up and login the application
* User is able to view different neighbourhoods and join
* User can create or upload post
* User is able to edit their profile
* User is able to fInd list of different bussiness in their neighbour
* Create posts that will be visible to everyone in their neighbourhood
* User is able to change their neighbourhood

## Behaviour Driven Development
| Input | Output|
|-------| ------|
| User sign up to for them see the available hoods | Users sees the posted neighbourhoods |
| Click Join Neighbourhood | Close neighbourhood or Explore |
| User explores | Sees the bussiness site with |
| User add bussines | Available site |
| User add new post | New post

## Setup and Installations

* Get the project
- Clone this repository
   

* Install and activate Virtual
- python3 -m venv venv
- source venv/bin/activate

* Navigate into the folder
- cd neighborhood

* Install Dependencies
- pip install -r requirements.txt

* Setup Database
    - SetUp your database User,Password, Host then make migrations:
    - python manage.py makemigrations
    - python manage.py migrate

* Run application
    - python manage.py runserver

est

## Technology Used

* Python3.6.9
* Django 3.2.1
* Heroku

## Known Bugs
* There are no known bugs at the moment


## Copyright and License


