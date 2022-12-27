# Dictionary app monorepo
___

### What's shipped with this repo?
- `React` (SSR) `Next.js` app
- `Django Rest Framework` app
- Swagger documentation for DRF
- Configured `PostgreSQL`
- Configured git hooks
- `docker-compose`

### Bootstrap

#### Manually starting
Start up backend project
```shell
cd backend
python -m venv .venv
source ./.venv/bin/activate  # `./.venv/Scripts/activate.bat` for windows
pip install requirements-dev.txt
python app/manage.py runserver
```

Start up frontend project:
```shell
cd frontend
npm install
npm start
```

#### Bootstrap project using Docker Compose
- To build (rebuild) `docker-compose --env-file=.env.dev up --build`
- To start without building `docker-compose --env-file=.env.dev up`
- To stop `docker-compose --env-file=.env.dev down`
- To execute commands in docker container context `docker exec -it backend sh`

By default, app starts at http://localhost:8000

***Don't forget to run migrations on first run***

#### Migrations
- To show all migrations `python app/manage.py showmigrations -l`
- To generate new migrations based on the changes detected to models `python app/manage.py makemigrations [app_label]`
- To run migrations `python app/manage.py migrate`

More about migrations cli [in docs](https://docs.djangoproject.com/en/4.1/topics/migrations/)

#### Git hooks
Run `npm install` in root directory to install git hooks framework, then run
`npx mookme init --only-hook --skip-types-selection` to install pre-commit hooks. 
