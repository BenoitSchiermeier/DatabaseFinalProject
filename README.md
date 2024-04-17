# Project Overview
Co-Op Connect is an innovative web platform designed to enhance the co-op education experience by facilitating transparent sharing of reviews and insights from students and recruiters. It allows users to post and access detailed feedback on various co-op positions, including aspects like job roles, skills involved, work environment, hourly pay, and more. The site features an intuitive interface with advanced search and filtering capabilities, making it easy for users to find relevant information based on company and specific role. By providing a centralized space for honest reviews and compensation transparency, Co-Op Connect aims to empower students and recruiters to make informed decisions and foster a supportive community around co-operative education.

By Shrey Patel, Benoit Schiermeier, Aahil Jubair, Jason Ie, Parth Shah

# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 




