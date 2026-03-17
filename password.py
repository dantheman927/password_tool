import random as rd
import string as s
def check_ul(pPASS):
    has_upper = False
    has_lower = False 

    for char in pPASS:
        if char.islower() and char.isalnum():
            has_lower = True
        if char.isupper() and char.isalnum():
            has_upper = True
    if has_lower and has_upper:
        return True
    else:
        return False


def pass_ch(pUSRPASS:list):
    score = 0
    has_sym = False
    has_char_8 = False 
    has_upper_lower = False
    has_num = False
    if len(pUSRPASS) >= 8:
        has_char_8 = True
    if check_ul(pUSRPASS):
        has_upper_lower = True
    for char in pUSRPASS:
        if char.isdigit():
            has_num = True
        elif not char.isalnum():
            has_sym =True
    for ls in [has_sym,has_char_8,has_upper_lower,has_num]:
        if ls == True:
            score += 1

    all = [score,has_sym,has_char_8,has_upper_lower,has_num]
    return all 

def pass_gen(pass_len: int):
    new_pass = []
    ucase = list(s.ascii_uppercase)
    lcase = list(s.ascii_lowercase)
    sym = list(s.punctuation)
    num = list("0123456789")
    random_list = [ucase,num,sym,lcase]
    for i in range (pass_len):
        lt = rd.choice(random_list)
        char = rd.choice(lt)
        new_pass.append(char)
    return "".join(new_pass)

while True:
    usr_in = int(input("enter what u would like to do \n1.check ur password\n2.generate password\n3.exit\n"))
    if usr_in == 1:
        usr_pass = input("enter ur password\n")
        result = pass_ch(usr_pass)
        if result[1] == False:
            print("u need symbols im ur password")
        if result[2] == False:
            print("u need to has more then or 8 charchters")
        if result[3] == False:
            print("u need at upper case and lower case letters ")
        if result[4] == False:
            print("u need to include numbers")

        if result[0] == 4:
            print("\nstong password\n")
        elif (result[0] < 4) and (result[0] > 1):
            print("\nmedium password\n")
        else:
            print("\nweek password\n")
    elif usr_in == 2:
        user_pass_len = int(input("how long would u like ur new password to be\n"))
        new_pass_out = pass_gen(user_pass_len)
        print(new_pass_out)
    elif usr_in == 3:
        exit()

    else: 
        print("u havnt selected a option that was 1 or 2 or 3\n")

