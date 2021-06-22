# Automate-WhatsApp-Python-project-pywhatkit
Python offers numerous inbuilt libraries to ease our work. Among them pywhatkit is a Python library for sending WhatsApp messages at a certain time, it has several other features too.

Following are some features of pywhatkit module:

Send WhatsApp messages.
Play a YouTube video.
Perform a Google Search.
Get information on particular topic.
In Python3 pywhatkit module will not come pre-installed, so you can install it by using the command:

pip install pywhatkit

# importing the module
import pywhatkit

# using Exception Handling to avoid
# unprecedented errors
try:
	
# sending message to reciever
# using pywhatkit
pywhatkit.sendwhatmsg("+91xxxxxxxxxx",
						"Hello from Abhirashmi",
						22, 28)
print("Successfully Sent!")

except:
	
# handling exception
# and printing error message
print("An Unexpected Error!")
