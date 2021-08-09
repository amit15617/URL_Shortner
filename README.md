# URL-shortener : Developed and designed by Amit Kumar || Linkedin : https://www.linkedin.com/in/amit-kumar-3914a2101/ || Gmail: Amit15617@gmail.com || Hackerrank : https://www.hackerrank.com/amit15617 || Git Hub : https://github.com/amit15617

This is a simple flask app which takes an URL and shortens it. This shortened verion of the URL redirects to the user to the long URL. 

For each long URL given by the user the application randomly generates an alphabetical combination which redirects to the long URL.

# Technical Aspects
This URL shortner tool is specially designed for converting long URs to fit it into respective short URLs.

This web application is containerized (Using Docker). It used docker-compose to run its web service.
## Language
    Front-End - HTML, Bootstrap, CSS
    Back-End - Python || DB - SQLAlchemy
    Framework - Flask
    Others supported tools - Git, Docker, Docker Compose

# List of Features :-
    1. Convert long URLs into short URLs.
    2. List all previous shorted URLs (Show History).
    3. For same long URL it will always return same short URL.
    4. Redirect to actual web url: Once you click either Long URL or Short URL shown
       in tables, you will be redirected to actual web page.

# How to run this application
    1. As this project is already Dockerized so, you just need to go to the directory where
        docker-compose.yml file is present and then just type 'docker-compose up' to run the application. It will run the application on by default port 5000(http://127.0.0.1:5000).

# Project Structure
>Amit_URL_Shortner
    > Code
      > templates
        . all_url.html
        . base.html
        . shorturl.html
        . url_page.html
      > url_shortner
        . bin
        . include
        . lib
      > .dockerignore
      > app.py
      > requirements.txt
      > site.db
    > .gitignore
    > docker-compose.yml
    > README.md

# Docker Image --> Docker Hub (public registry)
    https://hub.docker.com/r/amitkumar15617/amit_url_shortner_web

