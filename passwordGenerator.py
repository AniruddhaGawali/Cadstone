import random
import array

# Maximum length of password needed
MAX_LEN = 12

# Declare arrays of the character that we need in out password
# Represented as strings to enable easy string concatenation

DIG = ['0','1','2','3','4','5','6','7','8','9']
LOW_CASE_CHAR = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
UP_CASE_CHAR = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
SPL_CHAR = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|','\\',':',';','<','>','?','/']

# Combine all the character arrays above to form one array
rand_digit = random.choice(DIG)
rand_low_case = random.choice(LOW_CASE_CHAR)
rand_up_case = random.choice(UP_CASE_CHAR)
rand_spl_char = random.choice(SPL_CHAR)

# To store the password
temp_pass = rand_digit + rand_low_case + rand_up_case + rand_spl_char

# For the remaining length of the password, pick a random character from the combined list of character arrays
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(DIG + LOW_CASE_CHAR + UP_CASE_CHAR + SPL_CHAR)

    # Convert temporary password into array and shuffle to randomize the characters
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

# Traverse the temporary password array and append the characters to form the password
password = ""

for x in temp_pass_list:
    password = password + x

# Print the password
print(password)