# Backend Code for personal site, flip.rip

Full-stack Streamlit implementation, [see this repo](https://github.com/sapped/Authenticated-Full-Stack-Streamlit) for a template you can more quickly rip. This is for my personal website. I predominately use it to track my own goals, but the idea is to put it all here. It will continue to change, but figure I'd share what I make here.

## Goals Tracker
Create goals, which have optional amounts. Then track them. Store it in a Postgres DB, manage db with Pgadmin4, and GUI via Streamlit.

## Users
Functionality for barebones users. Lacks basics like creation routine, logout, etc. But if you just need ***something***, I hope this does the trick for you.

Relies upon:
- Docker (internal, non-exposed networking & enable reverse-proxy with NGINX)
- NGINX (auth_basic, $remote_user)
- Implementation of Streamlit Sessionstate (important to avoid cross-talk between sessions, don't want three users logged in on different computers but they're all being served as if they were the same user)

See sidebar for confirmation 'you are logged in as {user}'. Worth testing on two devices simultaneously with two different users to confirm they are both different, and not the same user.

### The magic behind my implementation

#### Configure reverse proxy, the auth_basic manges the user auth
Probably fancier ways to do this, but auth_basic proves the concept

1. edit file ~/main_dir/nginx/conf/project.conf
2. At every exposed endpoint, add the code I have, anything that starts with 'auth_basic' (as of writing, this is 'auth_basic' and 'auth_basic_user_file')
3. follow the README.md in ~/main_dir/nginx/auth/README.md to create users. Requires some apache2 tools installed so you can run htpasswd
4. This is it for configuration of nginx reverse proxy for auth. The magic now is: within our local docker container network, we can speak in HTTP without worrying about HTTPS stifling us ([see forum](https://discuss.streamlit.io/t/user-authentication/612/5?u=eddie))

#### Forward User via HTTP
1. edit file ~/main_dir/nginx/conf/project.conf
2. go to 'location /stream {}'. Not fully sure what stream does, but I know it passes the HTTP headers to my app
3. add code "proxy_set_header $remote_user (this shares username)"

#### Access headers in streamlit
This one was a doozy to figure out! Thanks to all in links referenced below for valuable guidance.
- see code in ~/main_dir/streamlit/users/users.py, which relies on session_state
- app.py grabs user and displays on sidebar
- you can use from users.users import get_user on whichever page you need users. Or maybe just implement it as part of global context somehow.
- in this build, look at sidebar (if collapsed, click the tiny triangle in the top left of the webpage). Should say at bottom "logged in as **{user}**".

#### My Opinion on Security
From what I've read in the links below, this is secure. All user communication is handled inside the docker network (internal, inaccessible by outside world). One thing this is missing for a real-life implementation is an SSL certificate. I'll let you handle that on your own - it's a straightforward nginx configuration that you can Google easily.

But PLEASE let me know if you disagree! Security is essential. I want to ensure this implementation is totally safe and up to modern standards of security.

### Links referenced when designing users
- https://discuss.streamlit.io/t/access-request-header-in-streamlit/1882
- https://github.com/streamlit/streamlit/issues/1083
- https://gist.github.com/okld/0aba4869ba6fdc8d49132e6974e2e662

## Other helpful things
- dbdiagram.io lets me visualize my ERD (entity relationship diagrams). Aka, those DB tables with connector things. Right now, I think DBML is a cool language for designing databases).

## TBU
- Format time on read entries from epoch float