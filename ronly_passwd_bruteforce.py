"""
By: Prabhat Soni
This program outputs all the combinations of a-z.
The output is in form of a string.
First we output all 1-length ones, then 2-length ones and so on
This could potentially be used for password cracking


length=3,6,etc
flag_str='11011','1011','1111',etc 1 means that pos has last char. and 0 means that pos doesnt have last char. flag_str is a string
string='adbg','zzez',etc
"""

from time import sleep
import sys

def z_on_right(string):
	ctr=0
	for i in range( len(string)-1 ,-1,-1):
		if string[i]==last_char:
			ctr+=1
		else:
			break
	return ctr


#POSSible improvement is to remove need for for loop  ;   remove the function as it is giving overkill i guess
#put another var - 3rd parameter pass the prev z count or somehting
#first make assuming it is for a-z only. use that in statements no prob

sys.setrecursionlimit(20000)


def func(a,b):
	print(b,end="\t")
	#sleep(0.01)
	length=a
	string=b

	if(string==length*last_char):
		new_length=length+1
		return func(new_length,new_length*first_char)
	elif(string[-1]!=last_char):
		new_char=chr(ord(string[-1])+1)
		return func(length,string[:-1]+new_char)
	elif(string[-1]==last_char):
			ctr=z_on_right(string)
			pos_to_change=length -1 - ctr
			new_char=chr(ord(string[pos_to_change])+1)
			new_string = string[:length-1-ctr] + new_char + first_char*ctr
			return func(length,new_string)
	else:
		print("ERROR: -X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-")

first_char='a'
last_char='z'
func(1,'a')
