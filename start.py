logo = '''
                                                   Welcome to the coding buddha

                        _ooOoo_
                       o8888888o
                       88" . "88
                       (| -_- |)
                       O\  =  /O          All that we are is the result of what we have thought.
                    ____/`---'\____       The mind is everything.
                  .'  |\|     |//  `.     What we think we become.”
                 /    |||  :  |||//  |                                     Buddha
               /  _||||| -:- |||||_  |
                |   | |\|  -  /'| |   |
                | \_|  `\`---'//  |_/ |
                \  .-\__ `-. -'__/-.  /                 Its time to code some shit up baby :)
              ___`. .'  /--.--\  `. .'___
           ."" '<  `.___\_<|>_/___.' _> |"".
          | | :  `- \`. ;`. _/; .'/ /  .' ; |
          \  \ `-.   \_\_`. _.'_/_/  -' _.' /
===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
                        `=--=-'                       
'''

print(logo)

def menu():
    while True:
        inp = input("Select task: 1  \nGo back: b \n >>> ")

        if inp == '1':
            print('Oh no, it seems like i forgot my bycicle at the Bodhi tree! Can you help me and bring it to me? \nIts locked with a special lock that anyone can open if they have a few hours to spare. The lock has four cells, each one can be a number from 0 to 9.\n It has an electronic terminal too, so if u can code a lil bit you can use your computer to make it faster! It takes in a string of four characters as an input! \n Good luck!\n\n (Go to levels >> lvl 1)')
            break
        elif inp == 'b':
            start_button()
            break

def start_button():
    while True:
        inp = input("To start please type 'start' >> ")
        if inp == 'start':
            menu()
        break



start_button()









