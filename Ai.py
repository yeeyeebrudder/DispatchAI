from datetime import datetime
from datetime import timedelta
from pytz import timezone
import pytz


def main():
    print('Hello! I am your AI dispatcher for today.\n')
    beginingPrompt()
    
def beginingPrompt():
    print('Please type a command:\n\"Run to _\",\n\"Complete\",\n\"Break\",\n\"Lunch\",\n\"End\",\n\"Help\",\nor \"rep\" if you need a human.')

main()
value = input()
value = value.lower()
currentTime = datetime.now(timezone('America/Chicago'))
if 'run to' in value:
    startRun()
elif 'complete' in value or "10-24" in value:
    print('all done')
elif 'thank you' in value:
    print('My pleasure')
elif 'end' in value:
    print('Goodbye! It was my pleasure to serve you today' )
elif 'break' in value:
    print('Enjoy!')
elif 'lunch' in value:
    lunch = currentTime+ timedelta(minutes=30)
    print('See you back at '+ lunch.strftime("%H:%M") + ', Enjoy!' )
elif 'help' in value:
    beginingPrompt()
    print('Would you like me to contact a dispatcher?')
    if input().lower == 'yes':
        getRep()
elif 'rep' in value:
    getRep()
else:
    print('I\'m sorry, I am not understanding your request.\n')
    beginingPrompt()
    
def getRep():
    #notify rep
    print('I\'m Fetching a dispatcher for you right now.')
def startRun():
    print()