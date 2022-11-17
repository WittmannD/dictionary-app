# Dictionary app monorepo
___

### What's shipped with this repo?
- `React` (SSR) `Next.js` app &nbsp;&nbsp;&nbsp;&nbsp; * *soon* *
- `Django Rest Framework` app
- Configured `PostgreSQL`
- `docker-compose`

### Bootstrap project using Docker Compose
- To build (rebuild) `docker-compose --env-file=.env.dev up --build`
- To start without building `docker-compose --env-file=.env.dev up`
- To stop `docker-compose --env-file=.env.dev down`
- Don't forget to run migrations on first run

Migrations
- To run in docker `docker exec -it backend sh`
- To show all migrations `python app/manage.py showmigrations -l`
- To generate new migrations based on the changes detected to models `python app/manage.py makemigrations [app_label]`
- To run migrations `python app/manage.py migrate`
- To exit `docker exit`

More about migrations cli [in docs](https://docs.djangoproject.com/en/4.1/topics/migrations/)

___
By default, app starts at http://localhost:8000. API documentation available at [/swagger](http://localhost:8000/swagger) route
