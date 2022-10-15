#!/usr/bin/env bash

# Install nginx
dnf install nginx

# We create the armorclad user
useradd armorclad -G nginx 
