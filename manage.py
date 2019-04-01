#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys

#Run bot from bot/bot.py
def runbot():
    from bot import bot 
    bot.main() 
                
#Execute valid arguments
def execute_from_command_line(arg): 
    if arg == "runbot": 
        runbot()
        return True
#    elif ...:
#        pass
    else:
        print("{} not value argument!".format(arg))
        return False

#Give token from user and write to bot/secrets.py
def token_worker(): 
    try: 
        from bot.secrets import TOKEN 
        return True 
    except ImportError: 
        TOKEN = input("Please enter your API Token: ") 
        try: 
            with open("bot/secrets.py", "w") as secrets: 
                secrets.write('TOKEN = "' + TOKEN + '"') 
            return True 
        except Exception as e: 
            print("Bad error while write:", e) 
            return False 
    except Exception as e: 
        print("Bad error while Import:", e) 
        return False 

def main(argv):
    if token_worker() is True:
        arg = " ".join(argv)
        #Check arg is empty or not
        if len(arg) > 0:
            if execute_from_command_line(arg) is True:
                exit(0)
            else:
                exit(1)
        else:
            print("You must give a argument to me ...")
            exit(1)
    else: 
        exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])