from my_functions import get_plaintext, check_equals, get_alpha_lst
# DO NOT UPDATE CODE ABOVE THIS LINE

#TODO: (Input)   Assign data to the variables.
alpha_lst = get_alpha_lst() #list of letter A - Z
plaintext = get_plaintext() #generates 3 random letters
#TODO: (Process) Manipulate the string.
jointext = ' '.join(plaintext) #seperates letters by a space
splittext = jointext.split(' ') #splits text

first   = splittext[0]   #finds first element
second  = splittext[1]   #finds second element
third   = splittext[2]   #finds third element

avalue = alpha_lst.index(first)  #first value 
bvalue = alpha_lst.index(second) #second value
cvalue = alpha_lst.index(third)  #third value

anewvalue = avalue - 3 #reduces value by 3
bnewvalue = bvalue - 3
cnewvalue = cvalue - 3

afinalvalue = alpha_lst[anewvalue] #obtains new letter from the list
bfinalvalue = alpha_lst[bnewvalue]
cfinalvalue = alpha_lst[cnewvalue]

listvalue = afinalvalue + bfinalvalue + cfinalvalue #combines for display purposes

completevalue = ' '.join(listvalue)         #converts it into a proper list
completevalue = completevalue.split(' ')
ciph_text = str(completevalue)

#TODO: (Output)  Display the asserted cipher text.
print(ciph_text)
assert check_equals(plaintext,listvalue) #Checks if the Cipher worked correctly
print ("Test Completed")
