
# Backend Technical Test

There is a demo online at https://seal-app-6d5qj.ondigitalocean.app/docs

A Postman collection is included in this repo in the `postman` directory. It should work simply by importing it in Postman wit the default 
variable values.

1. Send a request with csrf/GET csrf to get a token
2. Send a reuqest with token/POST new token to get an authorization token for the existin `admin` user.
3. Try other requests included now that you are authenticated.

There are some request that are labeled anonymous, these only are able to get products, there is one to create a product by anonymous,
try it, it should bedy the create request.

## Development Setup

Clone the repository `git clone git@github.com:ecelis/luuna-backend.git`.

```sh
cd luuna-backend
```

Copy `sample.env` to `src/api/.env`and edit it to suit your environment.

```sh
cp sample.env src/api/.env 
```
With the default values it should simply work in docker.

But if you also want email notifications, you need either SMTP credentialsor a sendgrid 
API key and fill in the variables.

And set **EMAIL_CHANNEL** to either `smtp` or `sendgrid`.

```
API_DEBUG=True
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_PASSWORD=verysecret_password
POSTGRES_USER=luuna
POSTGRES_DB=retail
API_SECRET_KEY='really_long_and_random_String'
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
CSFR_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
CORS_ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
EMAIL_CHANNEL=sendgrid
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER="contact@example.com"
EMAIL_HOST_PASSWORD=very_secret_pwd
EMAIL_USE_TLS=True
SENDGRID_API_KEY=
```

## Docker

```sh
docker compose up
```

In a new terminal window create the first user, run the following command, it will ask for a password.

```sh
docker compose exec -i api sh -c 'python3 manage.py createsuperuser --username admin --email admin@example.com'
```

Browse the API http://localhost:8000

## Optional Manual Setup Steps

If you can't use docker, you can instead follow the next steps to setup the
app locally.


Create a python virtual environment and activate it

```sh
python -m venv ENV
source ENV/bin/activate
```

Install python dependencies
```sh
pip install -r src/api/requirements.txt
```


Run migrations to bootstrap the database

```sh
python src/api/manage.py migrate
```

Run the app

```sh
python src/api/manage.py runserver
```

Create the superuser

```sh
python src/api/manage.py createsuperuser --username admin --email admin@example.com
```

### OpenAPI Swagger

Update the schema every time the API changes

```sh
python src/api/manage.py spectacular --color --file schema.yml
```

### Generate documentation

It requires nodejs installed!!

```sh
npx @redocly/cli build-docs src/api/schema.yml --output docs/index.html
```

# Luuna Backend API Architecture Design

## 1. Introduction

This document outlines the architecture design for the Luuna Backend API, built using Python with Django and Django REST Framework. The API leverages a PostgreSQL database and employs JWT for authentication. It includes a modular design for product catalog, user management, and notification systems, ensuring loose coupling and scalability.

## 2. Goals

* **Scalability:** Design an architecture capable of handling increasing user loads and data volumes.
* **Maintainability:** Implement a modular structure to facilitate future development and maintenance.
* **Security:** Ensure secure authentication and authorization using JWT.
* **Flexibility:** Utilize design patterns (e.g., Factory Pattern) to enable easy extension and modification.
* **Reliability:** Implement robust deployment processes to minimize downtime.

## 3. Technology Stack

* **Programming Language:** Python 3.x
* **Web Framework:** Django 5.x
* **API Framework:** Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Authentication:** JSON Web Tokens (JWT)
* **Containerization:** Docker
* **Version Control:** Git (GitHub)
* **Deployment:** Dockerized environment on DigitalOcean (cloud-provider agnostic)
* **Notifications:** SMTP, SendGrid API

## 4. Architecture Diagram

```mermaid
graph LR
    A[Client Applications (Web, Mobile)] --> B(Luuna Backend API - Django/DRF);
    B --> C[PostgreSQL Database];
    B --> D[JWT Authentication];
    B --> E[Product Catalog Module];
    B --> F[User Management Module];
    B --> G[Notification System Module];
    G --> H{Notification Provider Factory};
    H --> I[SMTP Provider];
    H --> J[SendGrid Provider];
    K[GitHub (Main Branch)] --> L[CI/CD Pipeline (GitHub Actions)];
    L --> M{Build Success?};
    M -- Yes --> N[Docker Container Build & Push];
    N --> O[DigitalOcean Deployment];
    M -- No --> P[Build Failure (No Deployment)];
```

## 5. Architectural Components
### 5.1. API Layer (Django/DRF)

- Responsible for handling HTTP requests and responses.
- Utilizes Django REST Framework for API development.
- Implements RESTful API endpoints for products, users, and notifications.
- Manages request validation, serialization, and deserialization.

### 5.2. Database Layer (PostgreSQL)

- Stores application data persistently.
- Utilizes Django ORM for database interactions.
- Ensures data integrity and consistency.
- Managed PostgreSQL database for optimal performance and reliability.

### 5.3. Authentication (JWT)

- Provides secure authentication and authorization.
- Generates and verifies JWT tokens.
- Supports stateless authentication.
- Allows a wide variety of applications to consume the API.

### 5.4. Product Catalog Module

- Manages product data (e.g., product details, categories, inventory).
- Provides API endpoints for product retrieval and management.
- Implements data models and business logic related to products.

### 5.5. User Management Module

- Handles user registration, authentication, and authorization.
- Manages user profiles and permissions.
- Provides API endpoints for user management.

### 5.6. Notification System Module

- Sends notifications via various providers (SMTP, SendGrid).

- Utilizes Django signals to trigger notifications.

- Implements the Factory Pattern for provider flexibility.

- Allows to easily add or change notification providers.
- Notification Provider Factory:
    - Abstracts the creation of notification providers.
    - Allows dynamic selection of providers based on configuration.
    - Facilitates adding new providers without modifying existing code.
SMTP Provider:
    - Sends notifications via SMTP.
SendGrid Provider:
    - Sends notifications via the SendGrid API.

### 5.7. Containerization (Docker)

- Packages the application and its dependencies into Docker containers.
- Ensures consistent deployment across different environments.
- Facilitates scaling and management of the application.

### 5.8. CI/CD Pipeline (GitHub Actions)

- Automates the build, test, and deployment process.
- Triggers deployments upon successful merges to the main branch.
- Ensures zero downtime deployments.
Avoids deployments on build failures.

## 6. Deployment

- Deployed in a Dockerized environment on DigitalOcean.
- Utilizes a managed PostgreSQL database.
- Employs a CI/CD pipeline for automated deployments.
- Cloud-provider agnostic to allow easy migration to AWS, Azure, or GCP.

## 7. Future Enhancements

- Implement caching to improve performance.
- Add support for asynchronous tasks using Celery.
- Integrate with a message queue (e.g., RabbitMQ, Kafka) for event-driven architecture.
- Implement API versioning.
- Add more notification providers.
- Implement automatic scaling.


Hello! Thanks for your interest in applying to ZeBrands.
As a part of the recruiting process, we ask you to complete this task as a way for you to showcase your abilities and knowledge.

# Description of the task

We need to build a basic catalog system to manage _products_. A _product_ should have basic info such as sku, name, price and brand.

In this system, we need to have at least two type of users: (i) _admins_ to create / update / delete _products_ and to create / update / delete other _admins_; and (ii) _anonymous users_ who can only retrieve _products_ information but can't make changes.

As a special requirement, whenever an _admin_ user makes a change in a product (for example, if a price is adjusted), we need to notify all other _admins_ about the change, either via email or other mechanism.

We also need to keep track of the number of times every single product is queried by an _anonymous user_, so we can build some reports in the future.

Your task is to build this system implementing a REST or GraphQL API using the stack of your preference. 

## What we expect
We are going to evaluate all your choices from API design to deployment, so invest enough time in every step, not only coding. The test may feel ambiguous at points because we want you to feel obligated to make design decisions. In real life you will often find this to be the case.

We are going to evaluate these dimensions:
- Code quality: We expect clean code and good practices
- Technology: Use of paradigms, frameworks and libraries. Remember to use the right tool for the right problem
- Creativity: Don't let the previous instructions to limit your choices, be free
- Organization: Project structure, versioning, coding standards
- Documentation: Anyone should be able to run the app and to understand the code (this doesn't mean you need to put comments everywhere :))

If you want to stand out by going the extra mile, you could do some of the following:
- Add tests for your code
- Containerize the app
- Deploy the API to a real environment
- Use AWS SES or another 3rd party API to implement the notification system
- Provide API documentation (ideally, auto generated from code)
- Propose an architecture design and give an explanation about how it should scale in the future

## Delivering your solution
Please provide us with a link to your personal repository and a link to the running app if you deployed it.
