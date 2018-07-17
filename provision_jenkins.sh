#!/bin/bash

#:<<COMMENT

# Install java
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update

echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections
apt-get install --yes oracle-java8-installer
yes "" | apt-get -f install

#COMMENT
