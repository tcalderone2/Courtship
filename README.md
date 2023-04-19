# Courtship Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## What is Courtship?

Courtship is an app designed to help connect high school basketball players with college coaches. Players who want to continue their basetkball careers in college want to be able to build a profile to share with college coaches and demonstrate their interests. College coaches want to be able to search for recruits, build a relationship with them, and have a watchlist of talent to communicate with staff. This app, Courtship, will be the bridge between these two users and aid both high school basketball players and college coaches with the recruitment process.

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 




