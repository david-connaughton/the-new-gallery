# The New Gallery

# Introduction

The New Gallery website is for my Full Stack Frameworks with Django Milestone Project submission. The site is an online Photography Gallery, Shop and Tour Enquiry platform. It is designed utilizing the Django Framework to allow the user to have a full Ecommerce Experience. It allows full user authentication with Create, Read, Edit and Delete (CRUD) permissions where appropriate. This is to the benefit of both the Site Owner and user.

The user journey is intended to be intuitive and seamless. I have created a multi-page site architecture broken into individual App components as follows:

* Home
* Photos (Gallery)
* Cart
* Checkout
* Reviews
* Tours
* Profiles (complete with Registration, Login, Logout and Password Reset functionality)

# Table of Contents

* [UX](#UX)
* [Features](#Features)
* [Technologies-Used](#Technologies-Used)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits](#Credits)

# UX

This site is designed Mobile First and is responsive on all devices. Full UX documentation with User Stories is contained in the [UX Document](documentation/UX-Documentation-The-New-Gallery.pdf) stored in the Documentation section of this GitHub Repository. 

* Wireframes for the site are stored [here](documentation/wireframes).
* Surface mockups for the site are stored [here](documentation/surface).

# Features

As stated in the [Introduction](#Introduction) section [The New Gallery](https://the-new-gallery.herokuapp.com/) is constructed as a composite of 7 Django Apps. Each App is both independent and interdependent on others and lends specific functionality to the site.

## Existing Features:

### Home App
The Home App is used to render the `index.html` file. This is the first touchpoint for a user when they visit [The New Gallery](https://the-new-gallery.herokuapp.com/). The user is greeted with a responsive page that extends from the `base.html` template. The page contains a Navbar and Footer (which persist across the site), a Hero Image and a Call-To-Action Button which invites the user to visit the Gallery.


### Photos App
The Photos App (aka Gallery) is used to render the images which the user can peruse prior to deciding to make a purchase. The images are rendered in individual Bootstrap Cards and limited to 6 images per page. 


The Photos page contains two bespoke features Filtering and Pagination. The Filter allows the user to view similar images. The user can also reset their filter choice by selecting `All`. The user can also navigate through the Photos by using the Pagination Buttons at the bottom of the Page.

By Pressing `Further Information` under an individual image, the user is transported to an individual Photo-Detail page for the selected image. 

On this page, a user is supplied with further Information on the selected image. They can also select the quantity they wish to add to their Cart and can also navigate back to the Gallery to view further options. Once an item quantity has been selected, the user's cart is updated in the Navbar with the total value of items they have selected.

### Cart App
The Cart App is used to render the items and quantities the user has opted to  purchase. The user has the option to edit the quantity. If the user opts to edit the quantity the monetary total and item count updates accordingly. The user has the option to continue to the Checkout by pressing the corresponding Button. The user also has the option to delete the selected item from their Cart and to return to the Gallery to view more images.

### Checkout App
The Checkout App allows the user to review their order on the checkout page by pressing the `Show/Hide Order` Button. The user can also opt to go straight tot the delivery details section. The user can complete the process as an unregistered customer but is encouraged to `Register` or `Login` via Call-To-Action Buttons. If the user is logged in they can press a checkbox to save their delivery details to their unique profile.

The customer can make a payment for their order using the Stripe Credit Card Facility. As this is a project site, the user should use the card number `4242 4242 4242 4242`. When the payment is successfully processed, the user is directed to a Checkout Success Page. This page supplies the customer with their order information. This order information is also saved to their user profile page and an email of confirmation is issued.

### Reviews App
The Reviews App allows a user to read reviews of images submitted by other users. If the customer is authenticated and logged in, there is a Call-To-Action Button inviting them to submit a review. If a user opts to leave a review they are directed to the Custom Review Form. When their review is submitted, they are redirected to the Reviews Page. The user's review will appear on this page and on their individual Profile Page.

The user retains full CRUD (Create, Read, Update and Delete) functionality of their review and can conduct any of these operations from both the Reviews Page and their Profile Page.

### Tours App
The Tours App features three components. 

* Tour options
* Map
* Custom Enquiry Form

The user is presented with two tour options and has the opportunity to engage with a Customized Map to see the journey distances for the Tours. If the user isn't logged in they are invited to `Login` or `Register`. One they have done this, they can complete a Custom Enquiry Form stating their tour preference and supply some information to the site Owner. The completed form is saved to Django Admin for the Site Owner. Upon completing the Form, the user is redirected to a success page to acknowledge receipt of their enquiry.

### Profiles App
The Profiles App consists of a single Profile Page. On this page, the user has full visibility of their Delivery Details (which they can update), Order History and Reviews. 

Via All-Auth Templates, the user can also Register, Login, Logout and Reset their Password.


## Features Left To Implement:

### Social Media Authentication:
Social Media Authentication would allow the user to Register, Login, Logout and Reset their password via a designated Social Media Account such as Facebook or Twitter. I reviewed this option during the Scope Process of UX and deemed it to be out-of-scope for the intial iteration of [The New Gallery](https://the-new-gallery.herokuapp.com/).

### Individual Artist Profiles:
I weighed up the merits of Individual Artist Profiles during my Focus Groups. A decision was made to forgo this functionality at this point. [The New Gallery](https://the-new-gallery.herokuapp.com/) aims to be a collaborative site and to encourage cross-pollination of styles and to expose users to the same. The inclusion of further Artists to the site may necessitate bespoke curation and individual sections for each.

# Technologies-Used

The New Gallery website was constructed using [Gitpod IDE](https://www.gitpod.io/). 

The programming languages utilized include:
* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Javascript](https://www.javascript.com/)/[jQuery](https://jquery.com/) 
* [Python](https://www.python.org/)
* [Django Framework](https://www.djangoproject.com/)

The Font Icons are from [Font Awesome](https://fontawesome.com/).

The payment system utilizes [Stripe](https://stripe.com/ie). 


The Map element is via the [Google API](https://developers.google.com/maps/documentation/javascript/overview) with Directions, Maps and Places libraries enabled.


I utilized [Bootstrap 4](https://getbootstrap.com/) for the  HTML Framework and [Balsamiq](https://balsamiq.com/) to complete the Wireframes.


A number of packages and libraries were installed via [PIP](https://pypi.org/project/pip/) to progress functionality on the site. These are documented in the [Deployment](#Deployment) section.


The code was validated where appropriate using the following validators:
* [HTML Validator](https://validator.w3.org/)
* [CSS Validator](http://jigsaw.w3.org/css-validator/)
* [Javascript Validator](https://codebeautify.org/jsvalidate)


The Static files and Images are stored on the [Amazon AWS S3](https://aws.amazon.com/s3/) server.


The email functionality is provided via [Gmail](https://www.google.com/gmail/about/).


The New Gallery is in production and released on [Heroku](https://the-new-gallery.herokuapp.com/).

# Testing

Extensive UAT(User Acceptance Testing) has been conducted with a total of 26 tests stored in the [Testing Document](documentation/Testing-Doc-The-New-Gallery.pdf) available in the Documentation section of this gitHub Repository. I also conducted some rudimentary Unit Testing for each App.

# Deployment

The New Gallery is deployed and available on [Heroku](https://the-new-gallery.herokuapp.com/)

As stated in the [Technologies-Used](#Technologies-Used) section, a number of requisites and dependencies were required to instantiate the project and a familiarity with the required Programming Languages is a must.

## How I Deployed This Project:

* Initiated a fresh project in my Coding Environment [Gitpod IDE](https://www.gitpod.io/)
* This environment comes with Python3 installed so there was no need to create a Virtual Environment.
* I installed Django by typing the command `pip3 install django` in the CLI.
* I initiated a new Django project by typing the command `django-admin startproject the_new_gallery .` in the CLI.
* This created the Django project and the `manage.py` file.
* To ensure this was successful, I typed `python3 manage.py runserver` into the CLI. This allowed me to open a webpage that confirmed Django was successfully installed and ready to use.
* To create my First App I typed the command `python3 manage.py startapp Home`
* I then navigated to `the_new_gallery` folder and added `Home` to Installed Apps in `settings.py` and the path to `urls.py`
* In the `Home` App, I created a a function in the `views.py` file that would render my first Django page.
* In the `Home` App, I created the following Folder/File structure `templates/home/index.html`
* In the `Home` App, i created a `urls.py` file and added the required routing.
* For Apps where a Model was created I also migrated the models using the following steps in the CLI:
    * `python3 manage.py makemigrations`
    * `python3 manage.py showmigrations`
    * `python3 manage.py migrate`
* These actions are necessary to update the Django Admin Panel and Database.
* Once this was completed my Home Page loaded successfully with the HTML I had written.
* I then created a `Superuser` by typing ` python3 manage.py createsuperuser` in the CLI. 
* I checked that this worked by visiting `https://8000-d16181d8-b1c9-43b2-b424-9a8c3b60aab5.ws-eu03.gitpod.io/admin/login/?next=/admin/` and logging in.
* This same process was repeated for each successive APP.
* To create consistency across the site I created: `base.html` and `static/css/base.css`. Every page on the site extends from these and it prevented repetition.
* To utilise images, I typed the command `pip3 install pillow` in the CLI.
* I then created a new Github Repository and linked it to my project.
* In [Heroku](https://www.heroku.com), I created a new project and linked it to my GitHub Repository for automatic deployment. I also navigated to resources and added `Heroku Postgres` as this was needed as database.
* In [Gitpod IDE](https://www.gitpod.io/), I typed the following command `pip3 install gunicorn`
* I then froze the requirements by typing `pip3 freeze --local > requirements.txt`
* I then created a `Procfile` with the command `web: gunicorn the_new_gallery.wsgi:application` typed inside of it. This was required to enable [Heroku](https://www.heroku.com) to run the project.
* To enable [Stripe](https://stripe.com/ie), I included the script file in `base.html` and then typed `pip3 install stripe` in the CLI.
* To enable authentication, I installed `allauth` by typing `pip3 install django-allauth`
* I also installed the allauth templates recursively by typing `cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/`
* I then made the necessary adjustments to `settings.py` following along with the documentation [here](https://django-allauth.readthedocs.io/en/latest/installation.html).
* To enable successful running of the site both in Development and Production the following Environment variables needed to be set in 

[Gitpod IDE](https://www.gitpod.io/):
1. Development = True
2. SECRET_KEY = 'Secret Key value'
3. STRIPE_PUBLIC_KEY = 'Stripe Public Key value'
4. STRIPE_SECRET_KEY = 'Stripe Secret Key value'

In [Heroku](https://www.heroku.com) Config Vars:
1. DATABASE_URL
2. SECRET_KEY = 'Secret Key value'
3. STRIPE_PUBLIC_KEY = 'Stripe Public Key value'
4. STRIPE_SECRET_KEY = 'Stripe Secret Key value'

* Following along with the [Code Institute](https://codeinstitute.net/) tutorial i then set up an account with [Amazon AWS S3](https://aws.amazon.com/s3/) this allowed me to upload all of my Static and Media Files.
* I then made the necessary adjustments to `settings.py`
* if 'USE_AWS' in os.environ:

    * AWS_S3_OBJECT_PARAMETERS = {
        * 'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        * 'CacheControl': 'max-age=94608000',
    * }

    * AWS_STORAGE_BUCKET_NAME = 'the-new-gallery'
    * AWS_S3_REGION_NAME = 'eu-west-1'
    * AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    * AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    * AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    * STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    * STATICFILES_LOCATION = 'static'
    * DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    * MEDIAFILES_LOCATION = 'media'

    * STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    * MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

* In [Heroku](https://www.heroku.com) Config Vars:
1. AWS_ACCESS_KEY_ID = "****My Key****"
2. AWS_SECRET_ACCESS_KEY = "****My Key****"
3. USE_AWS = True

* To complete the deployment i installed the following via the CLI `pip3 install dj_database_url` and `pip3 install psycopg2-binary`
* I then froze the requirements by typing `pip3 freeze --local > requirements.txt`
* I also imported `dj_database_url` to my settings.py file.
* To set up the Heroku Database, the following was added to `settings.py`
* if 'DATABASE_URL' in os.environ:
    * DATABASES = {
        * 'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    * }
* else:
    * DATABASES = {
        * 'default': {
            * 'ENGINE': 'django.db.backends.sqlite3',
            * 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        * }
    * }

* The final step was to enable email authentication via [Gmail](https://www.google.com/gmail/about/).
* I signed into my account and enabled Two-Factor authentication.
* The following was added to `settings.py`


* if 'DEVELOPMENT' in os.environ:
    * EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    * DEFAULT_FROM_EMAIL = '---------@example.com'
* else:
    * EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    * EMAIL_USE_TLS = True
    * EMAIL_PORT = 587
    * EMAIL_HOST = 'smtp.gmail.com'
    * EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    * EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    * DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')`

* I then added the following in In [Heroku](https://www.heroku.com) Config Vars:
    * EMAIL_HOST_PASS = '-------'
    * EMAIL_HOST_USER = '-------'

* I then completed code refactoring by typing `python3 -m flake8` in the CLI.
* This gave me a list of `.py` files across the project that needed to be reformatted to be `PEP 8` compliant. I made the adjustments to files I had created but as is best practice didn't alter system generated files.
* I made a final commit of my Code to GitHub and allowed the site to deploy automatically to [Heroku](https://www.heroku.com).

# Credits


### Content & Acknowledgments

* The Home App Cover Image Styling is inspired and customized by the following [tutorial](https://www.w3schools.com/howto/howto_css_hero_image.asp).
* The Cart and Checkout Apps are inspired and customized from a [Code Institute](https://codeinstitute.net/) Full Stack Frameworks with Django example.
* I sought inspiration for building Class Based views from the following [Tutorial](https://www.youtube.com/watch?v=-s7e_Fy6NRU&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=10).
* The implentation and styling of [Stripe](https://stripe.com/ie) in the Checkout App was assisted by this [Stripe Tutorial](https://stripe.com/docs/js/element/mount).
* The Map contained within the Tours App is inspired by the example [here](https://developers.google.com/maps/documentation/javascript/examples/directions-waypoints). The API key is included in the project as is required for Google API but is securely protected and restricted via my Google Developers Account.
* The Gallery images are kindly supplied by [Shane Connaughton](https://www.instagram.com/connaughtonshane/) and [Katie O'Neill](https://www.katie-oneill.com/).
