
def otp(olen):
    import random
    import string
    from colorama import Fore, Back, Style
    
    olen = int(input("Enter length of OTP = "))

    s1 = string.digits

    #otp = random.randint(999,10000)
    #print(otp)

    if (olen >= 3):
       s = list(s1)

       random.shuffle(s)
    
       print("")
       print(Fore.GREEN + "Your OTP is : " + "".join(random.sample(s,olen)))
       
    else:
       print("Give value more than 2")

