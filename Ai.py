from datetime import datetime
from datetime import timedelta
from pytz import timezone
import pytz

courierType = None
shift = -1
runs = []
done = False

class Entry:
    destination = ''
    StartTime = '' 
    EndTime = ''
    
    def __init__(self, dest):
        self.destination = dest
        self.StartTime = datetime.now(timezone('America/Chicago'))
    def complete(self):
        self.EndTime = datetime.now(timezone('America/Chicago'))
        print('Completing your ' + self.StartTime.strftime("%H:%M") + ' ' + self.destination + ' entry at ' + self.EndTime.strftime("%H:%M"))
        
def beginingPrompt():
    print('Hey there! Before we get started, can you tell me if you are on Lab or Pharmacy?')
    courierType = input()
    print('Perfect! now do you mind telling me which shift you are working today?')
    shift = input()
    print('Just to confirm, today you are a ' + str(courierType) + ' courier on ' + str(shift) + ' shift?')
    if 'yes' in input():
        print('You\'re good to go!\n')
        instructionsPrompt()
    else:
        print('Hmm. Let\'s try that again.\n')
        beginingPrompt()
    
def instructionsPrompt():
    print('Please type a command:\n\"Run to _\",\n\"Complete\",\n\"Break\",\n\"Lunch\",\n\"End\",\n\"Help\",\nor \"rep\" if you need a human.')
    
def startRun(destination):
    currentRun = Entry(destination)
    runs.append(currentRun)
    print('Logging an entry to ' + currentRun.destination + ' starting at ' + currentRun.StartTime.strftime("%H:%M"))

def main():
    print('Hello! I am your AI dispatcher for today.\n')
    beginingPrompt()
    
def getRep():
    #notify rep
    print('I\'m fetching a dispatcher for you right now.')
    
main()
    
while not done:
    value = input()
    value = value.lower()
    currentTime = datetime.now(timezone('America/Chicago'))
    if 'run to' in value:
        destination = value.replace('run to ','')
        startRun(destination)
    elif 'complete' in value or "10-24" in value:
        if len(runs) == 0:
            print('try calling a run first.')
        else:    
            runs[-1].complete()
    elif 'thank you' in value:
        print('My pleasure!')
    elif 'end' in value:
        print('Goodbye! It was my pleasure to serve you today' )
        done = True
    elif 'break' in value:
        print('Enjoy!')
        runs.append(Entry('break'))
    elif 'lunch' in value:
        lunch = currentTime+ timedelta(minutes=30)
        print('See you back at '+ lunch.strftime("%H:%M") + ', Enjoy!' )
        runs.append(Entry('lunch'))
    elif 'help' in value:
        instructionsPrompt()
        print('Would you like me to contact a dispatcher?')
        value = input()
        if 'yes' in value.lower():
            getRep()
        else:
            instructionsPrompt()
    elif 'rep' in value:
        getRep()
    else:
        print('I\'m sorry, I am not understanding your request.\n')
        instructionsPrompt()