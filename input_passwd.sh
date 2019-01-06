#! /bin/bash
#This script cannot be changed, except the password string
#This is because we are trying to simulate how a real-life input file would be
passwd=c
#read -sp "Enter your password: " attempt
#echo You enterred: $attempt #temporary; for testing
attempt=$1
if [[ $attempt == $passwd ]];
	then
	echo Correct entry.
	echo Your top secret message after all your hardwork is as folllows:-
	echo Sarabi is the name of Simba\'s mother

else
	echo Incorrect entry.

fi
