<p align="center">
  <img src="/docs/images/math-logo.svg" alt="Logo" width="300"/>
</p>

# Discrete Math repository

Discrete Math demo is a tool built by [Tarek Mulla](https://www.linkedin.com/in/tarekmulla/), student number [s3992651](mailto:s3992651@student.rmit.edu.au).

The purpose of this application is to demonstrate the material of Course [ MATH2415 - Discrete Mathematics](http://www1.rmit.edu.au/courses/045682) in [RMIT University](https://www.rmit.edu.au/) | [Master of Cyber Security](https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-cyber-security-mc159).


## How do I get set up? ##

* [Install docker](https://docs.docker.com/get-docker/)
* [Install docker compose](https://docs.docker.com/compose/install/)
* Create .env by copying .env.example and update the values
* Make sure docker is running
* Run commands that provided in *./Makefile*:
    * `make run`: run the webapp, can be accessed on [localhost:8080](https://localhost:8080)
    * `make stop`: stop the webapp
