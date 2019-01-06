#! /bin/bash

g++ cpp_ronly_passwd_bruteforce.cpp
./a.out

#How to change this to infinite while loop - while True
while ( echo hi | grep i )
do
./a.out | ./input_passwd.sh
done
