[![Python Check](https://github.com/tarekmulla/discrete-math/actions/workflows/check-python.yml/badge.svg)](https://github.com/tarekmulla/discrete-math/actions/workflows/check-python.yml)
[![Terraform deployment](https://github.com/tarekmulla/discrete-math/actions/workflows/terraform-deploy.yml/badge.svg)](https://github.com/tarekmulla/discrete-math/actions/workflows/terraform-deploy.yml)
[![ECR Image](https://github.com/tarekmulla/discrete-math/actions/workflows/ecr-image.yml/badge.svg)](https://github.com/tarekmulla/discrete-math/actions/workflows/ecr-image.yml)

<p align="center">
  <img src="/docs/images/math-logo.svg" alt="Logo" width="300"/>
</p>

# Discrete Math repository

Discrete Math demo is a tool built by [Tarek Mulla](https://www.linkedin.com/in/tarekmulla/), student number [s3992651](mailto:s3992651@student.rmit.edu.au).

The purpose of this application is to demonstrate the material of Course [ MATH2415 - Discrete Mathematics](http://www1.rmit.edu.au/courses/045682) in [RMIT University](https://www.rmit.edu.au/) | [Master of Cyber Security](https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-cyber-security-mc159).

<hr>

## Architecture ##

The project contains 2 parts: [Infrastructure](./infrastructure/), and [Web application](./webapp/)

### Infrastructure ###

The infrastructure part responsible for provisioning the cloud resources in AWS, this part is built using [Terraform](https://www.terraform.io/).

The [RMIT infrastructure](https://github.com/tarekmulla/rmit-infrastructure) should be provisioned before the application infrastructure, this repo is responsable to create all **base** (e.g. ECR, S3) and **shared** (e.g. VPC, NAT) resources for [RMIT](https://www.rmit.edu.au/) projects; Please check the repository [rmit-infrastructure](https://github.com/tarekmulla/rmit-infrastructure) for more details.

The following architecture shows all the components in the cloud infrastructure (both the base and the app resources):

<p align="center">
  <img src="/webapp/app/static/architecture.svg" alt="design" width="800"/>
</p>


### Web application ###

The web application is built using [flask framework](https://flask.palletsprojects.com/), and is hosted in Fargate in AWS. The application uses the web template engine [Jijna](https://jinja.palletsprojects.com) for the [python](https://www.python.org/) programming language.

The web application can be accessed via the URL: [discrete-math.rmit.mulla.au](https://discrete-math.rmit.mulla.au/); The application interacts with the backend by sending requests to the API gateway [api.discrete-math.rmit.mulla.au](api.discrete-math.rmit.mulla.au).
**Note** that the api gateway required a token to authorize access to its resources.*

The web application provides access to the user after they signing in to the website, all user details are saved securely in [Amazon Cognito](https://aws.amazon.com/cognito/).

<hr>

## Deployment prerequisites ##

Before you provision the infrastructure you will need to make sure the following requirements are satisfied:

1. Make sure the [RMIT nfrastructure](https://github.com/tarekmulla/rmit-infrastructure) is provisioned in the same account the web application will deployed to.

<hr>

## DevSecOps practices ##

The application has couple of check to follow best practices, and make sure the application is secure, please notice that this part still in-progress.

### Github actions ###

The project use github action to check, test, and deploy the application. The followings are the actions it supported now:
* [ecr-image](https://github.com/tarekmulla/discrete-math/actions/workflows/ecr-image.yml): This action responsable on generating the ECR image and push it to AWS ECR when a new commit pushed to the main branch.
* [check-python](https://github.com/tarekmulla/discrete-math/actions/workflows/check-python.yml): This action is triggered whenever a new pull request opened, it runs couple of tools to check the python linting, format, static code analysis, and run unittests for the python source code.
* [terraform-plan](https://github.com/tarekmulla/discrete-math/actions/workflows/terraform-plan.yml): This action checks the Terraform plan and shows it in the pull request.
* [terraform-deploy](https://github.com/tarekmulla/discrete-math/actions/workflows/terraform-deploy.yml): This action deploys the terraform infrastructure when a new commit pushed to the main branch.


### Other tools ###

The repository has integration with other tools to check the security for the source code; Those tools are:
* [gitguardian](https://www.gitguardian.com/): To scan the opened pull requests and check if it contains secrets or senstive information in the code changes.
* [Snyk](https://snyk.io/): To scan the source code, and find vulnerabilities in both Terraform and docker images, and suggest security best practices.

<hr>

## How do I get set up? ##

### Terraform ###

* Install [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
* Install and configure [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions) based on where you want to provision the tool.
* Create `terraform.tfvars` file, and customize the terraform variable values.
* Init, plan and apply terraform. See: [Provisioning Infrastructure](https://developer.hashicorp.com/terraform/cli/run)


### Web application ###

* [Install docker](https://docs.docker.com/get-docker/)
* [Install docker compose](https://docs.docker.com/compose/install/)
* Create .env by copying .env.example and update the values
* Make sure docker is running
* Run commands that provided in *./Makefile*:
    * `make run`: run the webapp, can be accessed on [localhost:8080](https://localhost:8080)
    * `make stop`: stop the webapp

<hr>

## Who do I talk to? ##

You can contact me directly using one of the following:
* Linkedin: [Tarek Mulla](https://www.linkedin.com/in/tarekmulla/)
* Personal Email [rmit@mulla.au]((mailto:rmit@mulla.au))
* University Email [s3992651@student.rmit.edu.au](mailto:s3992651@student.rmit.edu.au)

<hr>

## Resources ##

Resources used to help creating this application:

1. Logo generated using [logo.com](https://logo.com)
2. [Bootstrap documentation](https://getbootstrap.com/docs)
3. [Terraform documentation](https://developer.hashicorp.com/terraform/docs)
4. https://www.geeksforgeeks.org/print-all-prime-factors-and-their-powers
5. https://github.com/BaReinhard/Hacktoberfest-Mathematics/blob/master/algebra/bezout/python/bezout.py
6. https://github.com/xehoth/TruthTableGenerator
