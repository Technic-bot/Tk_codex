# TK Codex

This repo is my small database I made for [Twokinds](https://twokinds.keenspot.com) the comic by Tom Fischbach. 
In general it is very hard to try to look for anything specific
in the comic pages itself, this small website allows you to search per character and per textual dialogue.

This by no means try to replace the excellent [Codex Mr Amenon](https://2ks.wogcodex.com) did. Go check that out it is
very cool! Mine lacks features like negative searches and aliases. Moreover Amenons codex indexed panel content by hand
something mine does not. 

This is first an exercise for me to learn some web development, you can tell i know nothing of css, and combining something of my work on
twokinds data into something. Moreover this thing is up to date with the comic and has, or should have, some features to
keep it automatically in sync whenever a new page comes out. Finally it is completely open source so you can host your
own and or use it for whatever reason.

Again my final objective with this is for people to have some way to quickly crossreference information on the comic.
Hope you find this useful and at least half as interesting as I did making it. 

Rest of the README deals with the structure and the deployment methods

## Requirements
To run this a linux server with python 3 should be enough to run this, everything is run inside a python virtual env so should be
transparent for the OS and JS code is static so no need to install stuff. 

Deployment configurations are written with nginx in mind so you will have to deal install that one too. Will deal with
deployment in its own section though. 

Also git-lfs to deal with raw data and databse file.

Other than that you need sqlite3 for this to run and that should be it.

## Structure
This is a rather simple repo we have the frontend, data, backend and scripts folders, these names should be mostly self
explanatory but will spend some time detailing every section. Website is build with flask and python as a backend and
react as a frontend database is provided as a sqlite database file, comic is only around 1200 pages long so a full RDBMS
was overkill for this.

### Backend
Again this is built with python and flask, this provides and REST API with a couple endpoints to query the database
remotely, db folder inside contains the database file twk.db. It is imporant if you intent to deploy your own the main
app entrypoint codex.py needs to exist on the same folder as the db directory for it to work. In general try to simply
use the same repo structure. 

### Frontend 
React frontend use npm run build to create  a compiled version of the frontend and plop it on to server with scp, rsync
or whatever you see fit there is nothing needed to be installed as all that code is run by client browser.

CSS files are also here. I know nothing of design, you can probably tell for the looks, and most of the look and feel is
based on the [mozilla todo app
tutorial](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/React_todo_list_beginning)

### Config 
Miscelaneous configuration files. Serves as templates to set up both nginx to serve the js files and to foward api
requests to the python backend. Also provide some templates to run the backends as a systemd service in the background.
Bothe assume an user named armorclad is serving the app files, part of the nginx group, should probably make that
configurable at some point

Some setup scripts are provided, take them as generic notes on what you may need  to run to set up your server.

### data
The comic is provided as a sqlite3 database but raw csvs I used to create the database are available here. You can use
those and play with the data on pandas.

Main file is twk_data.csv which contain all pages, title, publication date and transcript if available. twk_chars.csv is
generated fromt he prior file and is a small table that indicates which characters appear on each page

### Scripts
Miscelaneous scripts massage_data.py creates the characters csv from the twk_data.csv since it is already provided you
do not need to run it.

create_tables.sql as the name implies turns the raw csv files into the twk.db so you can regenerate your db if you break something. 

update_db.py is a simple python script that allows you to scrape the comic page directly and automatically update/insert
a missing page. 

# TODOs
Favorite part, what i have not done! ~~PRs accepted~~

1. Tests, because TDD!
2. API Documentation 
3. Get some decent CSS 
4. Installation scripts
5. Docker for easier deployment

