#!/usr/bin/env bash

# Install python venv
python -m venv codexenv
source codexenv/bin/activate
pip install wheel
pip install flask gunicorn

dnf install nginx

# We create the armorclad user
useradd armorclad -G nginx 

# to set up selinux
sudo chcon -v --type=httpd_sys_content_t /home/armorclad/docs/ 
