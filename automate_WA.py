'''
Automate WhatsApp using Python
Author: Abhirashmi Kumari on 22nd june 2021
'''

#import the necessary module!
import pywhatkit as kt
import getpass as gp

#display welcome msg
print("Let's Automate Whatsapp!")

#capture the target phone number
p_num = gp.getpass(prompt='Phoneumber: ', stream=None) 

#capture the message
msg = "I love Python"

# call the method
kt.sendwhatmsg(p_num, msg, 10, 25)

# --------------------------------------------------------------
#2 lines of code

import pywhatkit as kt
kt.sendwhatmsg("+91**********", "HY:)!", 10, 25)