"""
By: Prabhat
Output: All possible password combinations in increasing order or length
Limitation(s): This code outputs password guesses only from the chracter set {a-z}
				Thus, the password also must be containing only characters from {a-z}
Current standard: It becomes super slow after 5-length strings

Working:-
1. First all 1-digit combinations
2. Then recursive call
3. Then all 2-digit combinations
4. Then recursive call
5. And so on

If the code is currently trying to generate all passwords of n-length, it will only contain passwords of (n-1)-length
lower length passwords are getting dynamically removed from the list
One layer [of n-length combinations] is removed before the recursive call

The previous layer is also called the generator layer, as it generates new combinations
The current layer is called the curr_layer
"""



from time import sleep #useful for testing

start=97 #a
end=122 #z

curr_length=1 #current length of password combinations


def initialiser(start,end):
	#We need to pre-compute these(1-length combinations) seperately in order to be able to generate 2-length combinations	
	list_combinations=[]
	for i in range(97,end+1):
		list_combinations.append(chr(i))
		print(list_combinations[i-97]) #slow-ish step but only 26 values so no worries
	return list_combinations

def printer(list_combinations=[]):
	global curr_length
	global start
	global end
	if(curr_length==1):
		list_combinations=initialiser(start,end)
	new_combinations=[]
	sleep(1)
	for i in range(len(list_combinations)):
		for j in range(start,end+1):
			new_combo=list_combinations[i]+chr(j)
			new_combinations.append(new_combo)
			print(new_combo)

	#This nested loop will always end at 'zz...zz'
	#Thus, making the recursive call at the end of the nested for loop is correct

	curr_length+=1
	return printer(new_combinations) #There is no base case; this is meant to be an infinite loop

x=printer()  #parameter can be left blank
#print(x)
