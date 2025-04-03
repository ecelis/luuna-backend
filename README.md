
<img src="https://zebrands.mx/wp-content/uploads/2021/07/WEB-ZEB-05-1-1024x291.png" width="300">

# Backend Technical Test



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
