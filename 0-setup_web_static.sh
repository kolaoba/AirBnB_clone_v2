#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static.

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Welcome to Kolapo.tech
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo rm -rf /etc/nginx/sites-enabled
sudo ln -sf /etc/nginx/sites-available/ /etc/nginx/sites-enabled
sudo chown -hR ubuntu:ubuntu /data
sudo service nginx restart
