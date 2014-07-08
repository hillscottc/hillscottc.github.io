#!/bin/bash 

## Base
apt-get update
apt-get upgrade
apt-get update
sudo apt-get install build-essential checkinstall
sudo apt-get install cvs subversion git-core mercurial
sudo chown $USER /usr/local/src
sudo chmod u+rwx /usr/local/src

apt-get install xfce4
apt-get install python-pip
apt-get install curl
apt-get install fabric

## Postgres
sudo apt-get install postgresql postgresql-contrib

# ## Using Virtualenvwrapper
# sudo easy_install virtualenv
# sudo easy_install virtualenvwrapper
# mkdir .virtualenvs
# export WORKON_HOME=~/.virtualenvs
# source /usr/local/bin/virtualenvwrapper.sh
# mkvirtualenv base_env # or workon if already exists

## To put gems in a proj's virtualenv. So, in each posactiv, or in bashrc 
# export GEM_HOME="$VIRTUAL_ENV/gems"
# export GEM_PATH=""
# export PATH=$PATH:"$GEM_HOME/bin”

## Django
# pip install django

## Create and run a django_project
# django-admin.py startproject django_project
# cd ~/django_project
# ./manage.py runserver [::]:8000





