#!/bin/bash
cat /dev/urandom | tr -dc 'a-zA-Z0-9!@#$%^&()' | fold -w 48 | head -n 1 > ./secret.txt

