#!/usr/bin/env bash

# Install python venv
python -m venv codexenv
source codexenv/bin/activate
pip install wheel
pip install flask gunicorn

dnf install nginx

# We create the armorclad user
useradd armorclad -G nginx 
