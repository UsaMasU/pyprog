# nginx and Waitress
Watch on YouTube: Deploy Django with NGINX and Waitress on Windows Server 2019

##Steps
1) Download and copy nginx to C:/.
2) Install Python 3.8 in C:/Python38 and install django, waitress
3) Edit ALLOWED_HOSTS in settings.py. Waitress will be running the Django server at http://localhost:8080.
4) Collect static files by running python manage.py collectstatic
5) Edit nginx_waitress/main_nginx.conf
6) Edit the server_name
7) Edit the path to /static (and /media if needed)
8) Edit proxy_pass to match the server running from Waitress (i.e. runserver.py). This will usually be localhost or your IP address
9) Create two directories inside of C:/nginx/
10) Create sites-enabled and sites-available
11) Copy webproject_nginx.conf to the two directories
12) Edit C:/nginx/conf/nginx.conf
13) Add include <path to your sites-enabled/webproject_nginx.conf>;
14) Change port 80 to a non-essential port like 10. We will need to utilize 80 for our Django project

##Check nging configuration
Open a terminal at C:/nginx/ and run nginx.exe -t to check files, and if everything is successful run nginx.exe to start the server

###Start waitress
python runserver.py

###Start nginx from CMD
start /B nginx

###Stop nginx from CMD
nginx -s stop

###Run server
Open a web browser and navigate to http://localhost
