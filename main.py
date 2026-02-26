from my_functions import get_plaintext, check_equals, get_alpha_lst
# DO NOT UPDATE CODE ABOVE THIS LINE

#TODO: (Input)   Assign data to the variables.
alpha_lst = get_alpha_lst() #list of letter A - Z
plaintext = get_plaintext() #generates 3 random letters
#TODO: (Process) Manipulate the string.
jointext = ' '.join(plaintext)
print(jointext)
#TODO: (Output)  Display the asserted cipher text.

'''
# Ready for the extra credit?
exp, act = 'DEF', 'ABC'
assert check_equals(exp,act,False), "this should fail"
'''
