from datetime import datetime
from datetime import timedelta
from pytz import timezone
import pytz



class Courier:
    Name = None
    courierType = None
    shift = -1
    runs = []
    done = False

    def __init__(self):
        print('hello')
        
currentCourier = Courier()

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
    currentCourier.courierType = input()
    print('Perfect! now do you mind telling me which shift you are working today?')
    currentCourier.shift = input()
    print('Just to confirm, today you are a ' + str(currentCourier.courierType) + ' courier on ' + str(currentCourier.shift) + ' shift?')
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
    currentCourier.runs.append(currentRun)
    print('Logging an entry to ' + currentRun.destination + ' starting at ' + currentRun.StartTime.strftime("%H:%M"))
def complete():
    if len(currentCourier.runs) == 0:
        print('try calling a run first.')
    else:    
        currentCourier.runs[-1].complete()
def breakentry():
    print('Enjoy!')
    currentCourier.runs.append(Entry('break'))
def lunch():
    currentTime = datetime.now(timezone('America/Chicago'))
    lunch = currentTime+ timedelta(minutes=30)
    print('See you back at '+ lunch.strftime("%H:%M") + ', Enjoy!' )
    currentCourier.runs.append(Entry('lunch'))
def help():
    instructionsPrompt()
    print('Would you like me to contact a dispatcher?')
    value = input()
    if 'yes' in value.lower():
        getRep()
    else:
        instructionsPrompt()
def getRep():
    #notify rep
    print('I\'m fetching a dispatcher for you right now.')

def main():
    print('Hello! I am your AI dispatcher for today.\n')
    beginingPrompt()    
    while not currentCourier.done:
        value = input()
        value = value.lower()
        
        if 'run to' in value:
            destination = value.replace('run to ','')
            startRun(destination)
        elif 'complete' in value or "10-24" in value:
            complete()
        elif 'break' in value:
            breakentry()
        elif 'lunch' in value:
            lunch()
        elif 'help' in value:
            help()
        elif 'rep' in value:
            getRep()
        elif 'thank you' in value:
            print('My pleasure!')
        elif 'end' in value:
            print('Goodbye! It was my pleasure to serve you today' )
            currentCourier.done = True
        else:
            print('I\'m sorry, I am not understanding your request.\n')
            instructionsPrompt()

main()
    