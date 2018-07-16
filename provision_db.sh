#!/bin/bash
#set -x

#
#   This will run from 'sudo su -c' when provisioning so no need to sudo each call
#

PGCONFIG_DIR=/etc/postgresql/9.5/main


# Create the database user.  
# The password will need to be set manually for now
sudo -u postgres createuser -S -D -R cbadmin


# Create the database, ownded by the cbadmin user
sudo -u postgres createdb -O cbadmin craftbar -E utf-8


# Modify the postgresql.conf
# set the listening interface
sed -i "s/#\(listen_addresses = 'localhost\)\('.*\)/\1,192.168.101.12\2/" ${PGCONFIG_DIR}/postgresql.conf


# Modify pg_hba.conf.
# ALLOW_NET will be added after the line MATHC_LINE
# This will allow logins from the 192.168.101.12 network
MATCH_LINE='host    all             all             127.0.0.1\/32            md5'
ALLOW_NET='host    all             all             192.168.101.12/24            md5'


sed -i "/${MATCH_LINE}/a ${ALLOW_NET}" ${PGCONFIG_DIR}/pg_hba.conf

service postgresql restart
