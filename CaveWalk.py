

"""
Copyright © (2021-present) R. James G.  Some rights reserved.


"CAVEWALK" LICENSE AGREEMENT 1.0

BY USING THE FOLLOWING SOFTWARE YOU AGREE THAT YOU MAY COPY AND/OR PUBLISH IT UNLESS THERE IS NO REFRENCE TO THE AUTHOR OF THE SOFTWARE AND THE LICENSE BEING USED IS NOT CHANGED.
YOU MAY NOT CREATE CHANGES TO THIS LICENSE UNLESS IT IS USED ON SOFTWARE OTHER THAN THE CURRENT ONE OR IS NOT BEING PUBLISHED.
IF YOU WISH TO MAKE A CHANGE TO THE SOFTWARE, YOU MUST REFRENCE THE AUTHOR.
YOU MAY USE REASOURCES INCLUDED IN THE SOFTWARE FREELY UNLESS MENTIONED OTHERWISE.

IF IN DOUGHT, PLEASE CONTACT rivetpert457@gmail.com

"""
import os
from time import sleep

clear = lambda: os.system('cls')


lives = 3
choice = 0

print('RJG Presents..')
sleep(1)

clear()
print('   ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄     ▄ ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄   ▄ ')
print('  █       █       █  █ █  █       █ █ ▄ █ █       █   █   █   █ █ █')
print('  █       █   ▄   █  █▄█  █    ▄▄▄█ ██ ██ █   ▄   █   █   █   █▄█ █')
print('  █     ▄▄█  █▄█  █       █   █▄▄▄█       █  █▄█  █   █   █      ▄█')
print('  █    █  █       █       █    ▄▄▄█       █       █   █▄▄▄█     █▄ ')
print('  █    █▄▄█   ▄   ██     ██   █▄▄▄█   ▄   █   ▄   █       █    ▄  █')
print('  █▄▄▄▄▄▄▄█▄▄█ █▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█')
print('  Copyright © (2021-present) R. James G.  Some rights reserved.')
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
input('Enter=begin')

clear()
print('                            Chapter 1')                                
sleep(2)

clear()
#walk1
print('You just woke up in a mysterious place. \nYou ask for help, but no one is there. \nThere seems to be only one path.')
print('\n\n 1 - Go through the path')
print(' 2 - Try to find an exit')
i = input('You>')
choice = int(i)

clear()    
#walk2
if choice == 1:
    print('You know there is no exit, but you walk down the path skeptically.')
    print('\n\n 1 - Search for food')
    print(' 2 - Open up your gps')
    i = input('You>')
    choice = int(i)
elif choice == 2:
    print('You look around, still, there is no exit.')
    print('\n\n 1 - Go through the path')
    i = input('You>')
    if i == '1':
        clear()
        print('You know there is no exit, but you walk down the path skeptically.')
        print('\n\n 1 - Search for food')
        print(' 2 - Open up your gps')
        i = input('You>')
        choice = int(i)
    else:
        print('Sorry, choice does not exist.')
        sleep(1)
        quit()
else:
    print('Sorry, choice does not exist.')
    sleep(1)
    quit()

clear()
#walk3
if choice == 1:
    print('As you search through the rubble, you find a moldy egg-sandwitch.')
    print('\n\n 1 - Contine walking')
    print(' 2 - Eat it')
    i = input('You>')
    choice = int(i)
elif choice == 2:
    print('You gps looks jammed.')
    print('\n\n 1 - Search for food')
    print(' 2 - Continue walking')
    i = input('You>')
    choice = int(i)
    if choice == 1:
        clear()
        print('As you search through the rubble, you find a moldy egg-sandwitch.')
        print('\n\n 1 - Contine walking')
        print(' 2 - Eat it')
        i = input('You>')
        choice = int(i)
    elif choice == 2: #continue walking - not to be confused with Eat it
        choice = 3
else:
    print('Sorry, choice does not exist.')
    sleep(1)
    quit()

clear()
#walk4
if choice == 1 or choice == 3:
    print('You continue walking down the path... Suddenly, your hear something.')
    print('\n\n 1 - Try to find the source')
    print(' 2 - Continue walking')
    i = input('You>')
    choice = int(i)
elif choice == 2:
    print('You just got poisoned.')
    sleep(1)
    quit()
else:
    print('Sorry, choice does not exist.')
    sleep(1)
    quit()

clear()
#walk5
if choice == 1:
    print('You search for it, fearing that you might get lost.')
    print('\n\n 1 - Continue')
    print(' 2 - Stop to take a rest')
    i = input('You>')
    choice = int(i)
elif choice == 2:
    print("You continue walking through what you realise is a cave. You don't know what your doing, but you keep on.")
    print('\n\n 1 - Continue')
    print(' 2 - Go back')
    i = input('You>')
    choice = int(i) + 2
else:
    print('Sorry, choice does not exist.')
    sleep(1)
    quit()

clear()
#walk6
if choice == 1:
    print('You continue looking for the source. Suddenly, its a bit quiet, a bit too quiet...')
    print('\n\n 1 - Continue')
    i = input('You>')
    choice = int(1)
elif choice == 2:
    print('You rest in the cave, but you suddenly feel a strike.')
    sleep(1)
    quit()
elif choice == 3:
    print('You continue looking through the cave, but you hear another noise.')
    print('\n\n 1 - Continue')
    i = input('You>')
    choice = int(1) + 1
elif choice == 4:
    print('As you walk back towards your starting point, you realize youve been trapped.')
    sleep(1)
    quit()
else:
    print('Sorry, choice does not exist.')
    sleep(1)
    quit()

clear()
print('Thanks for playing.')
sleep(3)
