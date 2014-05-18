
from time import sleep

#add two numbers
def add(x,y):
    #i see why variables defined within functions dont get "exported"
    #its too useful to keep reusing namespace like x and y over & again
    #or too easy to run into namespace problems with "exporting" them
    z = int(x) + int(y)
    return z

#subtract two numbers
def subtract(x,y):
    z= int(x) - int(y)
    return z

#multiplies two numbers
def multiply(x,y):
    z= int(x) * int(y)
    return z

#divides two numbers
def divide(x,y):
    z= int(x) / int(y)
    return z

#i experimented with input over raw_input as a sanitization device, and had
#to put these arguments within int() - they may be causing problems below
#with rounding down floats, just something to consider when rewriting the
#code for sanitizing input to only accept numbers, maybe inc. floats...?

def main():
    #creating a cli UI, which prompts for user inputs and calls functions to compute them
    #serious abuse of sleep() ahead, sorry for your eyes.
    print 'Welcome to the Steam-powered Calculatron Contraption...'
    sleep(1.0)
    print '*Pssssst Chooooof*'
    sleep(1.0)
    print '\n''This State Of The Art Mechanical Computer takes your 2 Numbers and'
    sleep(0.5)
    print '*Pssssst Chooooof*'
    sleep(1)
    print 'either adds(A), subtracts(S), multiplies(M) or divides(D) them so that'
    sleep(0.5)
    print '*Pssssst Chooooof*'
    sleep(1)
    print 'the machine returns you the result of that operation on your 2 Numbers.'
    sleep(0.5)
    print '*Pssssst Chooooof*'
    sleep(1)
    print '*tsssssssssssssssssssssss*'
    sleep(2)

    print '\n''And now for the magic of Steam Power!'
    sleep(0.5)
    print '*Pssssst Chooooof*'
    sleep(1)
    print '*tsssssssssssssssssssssss*'
    sleep(0.5)

    First=raw_input('Please enter your first Natural Number: ')
    if First >= 0:
        FirstNumber=First
    else:
        print 'Please enter Natural Numbers only'
    print '*Pssssst Chooooof*'
    sleep(0.5)
    print 'Your first Number is %s' % FirstNumber
    sleep(1)
#these numbers no longer handle floats i think. i tried various things, and
#they went from rounding down to next integer, to breaking the machine.
#yep! see notes above regarding expecting integers as functions arguments
    Second=raw_input('Please enter your second Natural Number: ')
    if Second >= 0:
        SecondNumber=Second
    else:
        print 'Please enter Natural Numbers only'
    print '*Pssssst Chooooof*'
    sleep(0.5)
    print 'Your second Number is %s' % SecondNumber
    sleep(0.5)

    Operator=raw_input('Please Enter the Mechanical Operator: ')
    print '*Pssssst Chooooof*'
    sleep(0.5)
    print '*Pssssst Chooooof*'
    sleep(0.5)
#i rewrote this code, so the functions got called here and output later
#deal with it B)
#you probably will have to deal with it, it seems to work worse than originally
    if Operator == 'A':
        A=add(FirstNumber,SecondNumber)
        Answer=A
    elif Operator == 'S':
        S=subtract(FirstNumber,SecondNumber)
        Answer=S
    elif Operator == 'M':
        M=multiply(FirstNumber,SecondNumber)
        Answer=M
    elif Operator == 'D':
        D=divide(FirstNumber,SecondNumber)
        Answer=D
    else:
        print '*CRUNK CRUNK CRRRRRRRRNK*'
        print 'The machine only accepts "A" "S" "M" or "D" inputs!'
#THE MACHINE BREAKS IF YOU ENTER A UNICODE CHARACTER LIKE "/"
#also else doesnt stop you putting in lower case letters like "d", and doesnt
#restart you back at IF again dummy, put this is in a while 1: LOOP of some
#sort perhaps... does it still work if you put a letter other than A/S/M/D?
#NOPE, this seems to be ENTIRELY broken now, accepts exact matches only.
#have a look at the bottom, where the sanitizer works.
    print 'Your mechanical operator is %s' % Operator
    sleep(1)
    print '*tsssssssssssssssssssssss*'
    sleep(2)
#be aware of any better formatters that could be used here to handle unicode?
    sleep(1)
    print '*CHHHHHHHHHHHHHHSSSSSS*'
    sleep(1)
    print '*Pssssst Chooooof*'
    sleep(1.5)
    print '\n''The Calculatron Steampowered Calculator reads your answer as: \n'
    sleep(1)
    print '*crunk* *crunk* *crunk* *crunk* *crunk* *crunk*'
    sleep(0.5)
    print '*PSSSSSSSSSSSssssssssssssssst*'
    sleep(1.5)

    print 'Patented Steam Powered Digital Display (c)1894 Flim&Flam Bros: ~<{{{  %d  }}}>~' % Answer

    sleep(1)
    print '*clunk*'
    sleep(0.5)
    print '*tsccch*'
    sleep(1)

if __name__ == '__main__':
    main()
    while 1:
        print 'Thank you for using the Time Saving Steam Powered Calculatron!'
        yn=raw_input('Would you like to Compute more arithmetic? Enter "Y" or "N" ')
        if yn == 'Y':
            main()
        elif yn == 'N':
            break
        else:
            print 'Enter Upper-Case "Y" or "N" to proceed!'
