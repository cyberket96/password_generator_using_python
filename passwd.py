
def passwd(plen):
    import random
    import string
    from colorama import Fore, Back, Style

    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter length of password = "))
    
    if (plen >= 8):
       s = []
       s.extend(list(s1))
       s.extend(list(s2))
       s.extend(list(s3))
       s.extend(list(s4))

       random.shuffle(s)

       #print("".join(s[0:plen]))
       print("")
       print(Fore.GREEN + "Your Password is : " + "".join(random.sample(s,plen)))
       
    else:
       print("Give length more than 8 characters!")
       

