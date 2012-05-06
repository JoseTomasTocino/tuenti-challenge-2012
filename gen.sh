#!/bin/bash

num=$1
mkdir p$num
cp blank.py p$num/p$num.py
chmod +x p$num/p$num.py
touch p$num/entrada
