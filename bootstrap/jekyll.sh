#!/bin/bash 

## Install RVM, Ruby, Jekyll

# \curl -L https://get.rvm.io | bash -s stable
source /home/vagrant/.rvm/scripts/rvm
rvm requirements
rvm install ruby
rvm use ruby --default
rvm rubygems current
gem install bundler