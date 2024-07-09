import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz" # all possible letters
num = "0123456789" # all possible digits
special = "@#$%&*" # all possible special chars

# pass_len=random.randint(8,13)  #without User Input
pass_len = int(input("Enter Password Length: ")) # with User Input

# length of password by 50-30-20 formula
alpha_len = pass_len//2 # use half of pwd len for letters
num_len = math.ceil(pass_len*30/100) # 30% of pwd len for digits
special_len = pass_len-(alpha_len+num_len) # 20% of pwd len for special chars

password = [] # init empty list for storing pwd chars

def generate_pass(length, array, is_alpha=False):
    for i in range(length): # loop used for char nums needed
        index = random.randint(0, len(array) - 1) # get rand index within array
        character = array[index] # get char at random index
        if is_alpha: # if array is alphabetic
            case = random.randint(0, 1) # randomly decide if letter should be uppercase
            if case == 1:
                character = character.upper() # if selected, convert letter to uppercase
        password.append(character) # add char to empy pwd list


# alpha password
generate_pass(alpha_len, alpha, True)

# numeric password
generate_pass(num_len, num)

# special char password
generate_pass(special_len, special)

# shuffle the generated password list
random.shuffle(password)

# convert List To string
gen_password = "" # init empty string for final pwd
for i in password: # loop through every char of pwd list
    gen_password = gen_password + str(i) #concatenate each char to final pwd string
print(gen_password) # print generated pwd