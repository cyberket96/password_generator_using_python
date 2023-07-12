import pyfiglet as fig
from colorama import Fore, Back, Style

print()
print(Fore.YELLOW + "Hello user...")
print("Project - Password Generator")
print()

banner = fig.figlet_format("Password Tool")
print(Fore.GREEN + banner)
print(Style.RESET_ALL)

print()                            
print(Fore.YELLOW + "Developer : Ketan Mote") 
print("Codename : ")
print("Github   : ")
print("Version  : ")                                                                                                           
print("Contact  : +91 9696969696 / mail96@email.com") 
print(Style.RESET_ALL)

print("----------------------------------------------------------------------------------------------------------------------------")

print("")

print("[+] Available Generators")

print("")
print(Fore.BLUE + "[1] Password")
print("[2] OTP")
print(Style.RESET_ALL)
print("")

opt = int(input("Enter the Option :"))
print("")

if (opt == 1):

   import passwd
   plen = 0
   print(passwd.passwd(plen))
   
elif (opt == 2):

   import otp
   olen = 0
   print(otp.otp(olen))
   
else:
   print("Enter right option!")
