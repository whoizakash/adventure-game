
# adventure game
# still in development.

print('*********************************')
print('Welcome to Adventure Guild! ')
print('*********************************')


# emojies
# ...............................
emojies ={'devil':'\U0001F608','msg':'\U0001F4AC','cngrts':'\U0001F44F','player':'\U0001F977','food':'\U0001F371','gold':'\U0001F4B0','weapon':'\U0001F3F9','weapon2':'\U0001F5E1','bruh':'\U0001F5FF','des':'\U0001F6A9','dead':'\U00002620','tree':'\U0001F332','herb':'\U0001F33F','bear':'\U0001F43B'}
# ................................

player_name=input('Please register your name: ')

print(f'Greetings {player_name}')

# ..........................................................................
answer=input(f'{emojies["msg"]} You got a quest, Ready to accept? (yes/no)').lower()

# main loop
if answer =='yes':
    answer=input(f'Bring Valerian herbs{emojies["herb"]} from the forest{emojies["tree"]}, Do you want to (accept/quit) ').lower()

# 2nd loop
    if answer == 'accept':
        answer=input(f'You start walking into the forest{emojies["tree"]}, you find a bear{emojies["bear"]}, Do you sneak past it or try to kill it?(sneak/kill). ').lower()
        # 3rd loop
        if answer =='sneak':
            print(f'You snuck past the bear{emojies["bear"]},')
            answer =input(f'Now you find A narrow river, you can swim through or cross the river by a plank.(swim/cross) ').lower()

            # 4th loop

            if answer == 'cross':
                print(f'You crossed the river, There is fairy waiting!')
                answer=input('The fairy is wounded ,Do you want to help or go find the herb?(help/ignore) ')


                # 5th loop
                if answer == 'help':
                    print(f'You patched up the wounds and helped the fairy, In return the fairy gave you a bag of gold{emojies["gold"]} and the valieran herbs ,You won!{emojies["des"]}')
                elif answer == 'ignore':
                    print(f'You dint have a good heart, You went into a mist and dissapeared!, You lost!{emojies["dead"]}')
                else:
                     print('Invalid answer!')
                # 5th loop
                

            # 4th loop
            elif answer == 'swim':
                print(f'You died swimming because the river was full of phiranas {emojies["dead"]}')

            else :
                print('Invalid answer!')


        # 3rd loop
        elif answer =='kill':
             print (f'You died killing the bear without weapons{emojies["weapon"]}!,You lose!') 
        else :
            print('Invalid answer!')


# 2nd loop
    elif answer =='quit':
        print(f'You decided to quit {emojies["bruh"]}')
    
    else :
        print('Invalid answer!')


# main loop
elif answer =='no':
    print (f'{player_name} see you soon {emojies["bruh"]}!')

else:
    print('Invalid option!')


print(f'Thank you for your precious time in the adventure guild!')