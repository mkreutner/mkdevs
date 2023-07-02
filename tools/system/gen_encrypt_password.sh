#!/usr/bin/env bash

read -s -p "Enter Password: " pwd;
encpwd=$(openssl passwd -1 -stdin <<< $pwd)
echo
echo "API_PASSWD='$(pwd)'"
echo "API_ENCRYPTED_PASSWORD='${encpwd}'"
