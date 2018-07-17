#!/bin/bash

:<<COMMENT
#TODO: get this working

# Install java
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update

echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections
apt-get install --yes oracle-java8-installer
yes "" | apt-get -f install

COMMENT

# 
# Install default-jdk
#

sudo apt-get install default-jdk -y


#
# Install Jenkins
#

# Add repo key to system
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -

# Append the debian package repo address to the sources.list
echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list

# Update
sudo apt-get update

# Install
sudo apt-get install jenkins -y
