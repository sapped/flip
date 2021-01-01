# Authenticated Full-Stack Streamlit

## Notes for Users

### Rationale & Features
[Streamlit](https://www.streamlit.io/a) is great, but it doesn't natively support user authentication. This repo leverages Nginx as a reverse proxy layer with enterprise-grade authentication. Nginx itself includes the ability to authenticate with most protocols like OAuth2, SAML, etc. which you should be able to implement in project.conf. However, this particular repo authenticates with Nginx's auth_basic, which is just a hashed username & password in a file (more below under first-time setup). If that's all you want, you can delete the folders that aren't "nginx" or "streamlit" and also remove any reference to them in the docker-compose.yml file.

But I also want a bit more than that. I also want a DB and an API to interact with the DB for a full-stack feel even for my smallest Streamlit applications. That's what the "api", "pgadmin4", and "postgres" folders / docker-compose services do. Ultimately, the goal is to separate presentation (streamlit) from logic, piping & persistence (FastAPI / Postgres). When presenting information in Streamlit, you process as little as possible. Ideally, your database and API calls should get most of the work done, be it with SQL queries to the DB or POST payload parameters to the API. This way, you'll be setup for an easy transition to a more robust Flask/Django app once you're finished prototyping in Streamlit. Or, you can just keep using Streamlit!

- Built on back of docker & docker-compose, so it's hopefully easy to deploy (see first-time setup instructions below)
- Streamlit application that interacts with an internal API powered by [FastAPI](https://fastapi.tiangolo.com/)
- Database is postgresql
- pgadmin at /pgadmin4/
- This works on a server like a Digitalocean droplet, but doesn't work on localhost. This is because I can't seem to make the :80 redirect work with local nginx.
- Nginx serves everything. See project.conf for the routes. Should be easy to read & follow-along the logic to add other services. Should even be easy to serve multiple streamlit applications with this

### First-time setup
1. The subfolders for the API, PGAdmin4, and Postgres each have ".env.template" files that you'll use to create your own ".env" files in each corresponding subdirectory. The ".env" files themselves are .gitignore'd. So, copy the .env.template files into new .env files. You should change out these default values with the real environment variables you're looking to use
2. you should gitignore your .env files so you aren't sharing any important credentials with the universe
3. create htpasswd .htpasswd -c <user> in the nginx > auth folder. More details in the READAME at nginx/auth. Also make sure that .htpasswd is in your gitignore, you probably don't want to share your hashed password with the world.
4. for subsequent users, you can print to command line by switching -c to -n and then copy-pasting the hashed password result
5. when you have made all the .env files and the .htpasswd file, build your docker. This can take some time!

    docker-compose up --build
6. Once you've built the app, you can run it again and exclude the slow build process with

    docker-compose up

7. If you need more help with docker, see below resources
8. See pgadmin4 referenced guide below for instructions on connecting DB to pgadmin4 if you need help with that

### Default Implementaion
This repo shows a default use-case where you can create, read, update, delete a basic "item" example. You can see how a RESTFUL configuration might flow between Streamlit, FastAPI, and Postgresql. With the added benefit of /pgadmin4/ to confirm your database is properly updated (see below reference resources on how to connect pgadmin4).

### Authentication
The nginx project.conf file puts everything behind basic htpasswd authentication by including this in the top "server" block. Again, see the README in the repo folder nginx/auth for details on how to create the (super easy to make) .htpasswd file that drives this basic authentication

    auth_basic "closed site";
    auth_basic_user_file /nginx/auth/.htpasswd;

## Guides Referenced when Building This
Here's some further detail if I'm not clear enough on anything. Thanks to everybody who wrote the guides below, they taught me a lot.

### Alembic
When you run your first alembic migration, type this:
    docker-compose run [service name] alembic revision --autogenerate -m "First migration"

And when you make other revisions you can just type in:
    docker-compose run [service name] alembic revision --autogenerate

replace [service name] with the docker-compose service name. In this case, it's called "api" per docker-compose.yaml in the top directory

[Reference I used to learn alembic in this context](https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396)

### FastAPI Quirks
1. [How to get openapi.json to load, required for the /docs/ endpoint](https://github.com/tiangolo/fastapi/issues/102#issuecomment-739520277)
2. [But also need to define root-path="/api/v1" for /docs to work](https://fastapi.tiangolo.com/advanced/behind-a-proxy/)

### PGAdmin4 References when Setting This Up:
Connect to postgres server in pgadmin(ctrl+f for "connect to a database server,": https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396

- [Fully comprehensive, did this one first. But also see below. Nginx should port_forward to 80, not 5050, for the GUI](https://www.enterprisedb.com/postgres-tutorials/reverse-proxying-pgadmin)
- [But needs to do the port 80 in nginx config, not the 5050 for me to use it](https://stackoverflow.com/questions/61802782/reverse-proxy-in-docker-using-nginx-for-pgadmin4)

### Docker Basics
In case you are unfamiliar with docker, [Jeff Astor has a really nice series](https://www.jeffastor.com/blog/pairing-a-postgresql-db-with-your-dockerized-fastapi-app) on "enough Docker to get by." This is a link to part two, which has some helpful commands. But you might want to rewind to Part 1, which is linked at the top of his blog post.

### Awesome-streamilt
Shoutout to Marc, providing a great workaround for pagination via [awesome-streamlit (pypi)](https://pypi.org/project/awesome-streamlit/) which I gladly repurposed here. And of course, here is the [awesome-streamlit github repo](https://github.com/MarcSkovMadsen/awesome-streamlit).

## Next Steps
- In production, I'll look to replace the 'auth_basic' login using an htpasswd with an 'auth_requeset' SP-initiated SAML 2.0 SSO login flow. Then I'll host the streamlit apps at different endpoints, restricting access to a user whitelist.