import string
import random
from colorama import Fore

while True:
    if __name__ == '__main__':

        print(f"{Fore.CYAN}\n#\t#\t#####\t#\t #\t#\t#"
              "\n#\t#\t#\t#\t# #  #\t#\t#"
              "\n#####\t#####\t#  # #\t#\t#"
              "\n#\t#\t#\t#\t#   ##\t#\t#"
              "\n#\t#\t#\t#\t#    #\t#####"
              "\n#############################")

        print(f'{Fore.CYAN}[*] Code By HorridHanu(^_~).')
        print(f'{Fore.CYAN}[*] Generate random Password.')
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation
        s5 = string.octdigits
        s6 = string.hexdigits
        s7 = string.hexdigits
        # s8 = string.whitespace
        PaswordList = int(input(f'\n\n{Fore.RED}Enter The Password Length i.e. 7, 8, etc (: '))
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        s.extend(list(s5))
        s.extend(list(s6))
        s.extend(list(s7))
        # s.extend(list(s8))

        random.shuffle(s)
        print(f"\n{Fore.CYAN}[+] Password(: "+''.join(s[0:PaswordList]))
        Exit = input(f"{Fore.WHITE}\n[-] Press X for exit, Else just hit enter: ")
        if Exit == "x" or Exit == "X":
            print(f"{Fore.MAGENTA}[*] Thanks for using.")
            break
        else:
            pass
