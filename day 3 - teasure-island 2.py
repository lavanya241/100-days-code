s=input('Do you want to Start the game: type "s" for start and "n" for no').lower()
if s=='s':
    print("You have found treasure map!!!!!!!")
    print(''' ____________________________________________________________________
            / \-----     ---------  -----------     -------------- ------    ----|
            \_/__________________________________________________________________/
            |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
            |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
            | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
            |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
            |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
            |  ~ \__ (( _( (  ))  ) _)    ((     ||//    " |   "    \_____,' | ~|
            |~~ ~   \  ( ))(_)(_)_)|  "    ))    //|| " __,---._  "  "   "  /~~~|
            |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
            | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
            |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
            |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
            | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
            |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
            | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
            |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
            | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
            |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
            | ~~ ~|__,-'~~~~~\    |"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
            |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
            |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
            / \----- ----- ------------  ------- ----- -------  --------  -------|
            \_/__________________________________________________________________/''')
    explore = input('do you want to explore the map Type"y" for yes and "n" for no')
    if explore =='y':
        print("you have arrived on island safely")
        choice1 = input("you have found a a house near the area and see a old lady waving to you."
                        "do want to hear her out type 'h' to hear her out and 'n' for no ").lower()
        if choice1 == 'h':
            print("the oldlady says: if have came to find the treasure please go back...\n "
                  "only some of them have returned "
                  "if you wish to go anyway go for it if answer the riddle you will easy go past the 1st road."
                  "\nthe riddle is What comes once in a minute, twice in a moment, but never in a thousand years?")
        else:
            print("you have started to explore the island")
        choice2 = input(" you have arrived at crossroad where one says monsoon and one says summer and one says winter "
                  "choose 'm' for monsoon and 's' for summer and 'w' for winter ").lower()
        if choice2 == 'w':
            print('You have enter the road for -25 c and frozen to death \n "Game over" ')
        elif choice2 == 'm':
            print('you have been saved and its raining and you have found an a tree and tree shows to a left mark where house been pointed')
            choice3 = input('you have entered the house and found 3 door and one is red , one in yellow and one is green. "r" for red , "y" for yellow and "g" for green ')
            print('''   ______
                      ,-' ;  ! `-.
                    / :  !  :  .   \
                    |_ ;   __:  ;  |
                    )| .  :)(.  !  |
                    |"    (##)  _  |
                    |  :  ;`'  (_) (
                    |  :  :  .     |
                    )_ !  ,  ;  ;  |
                    || .  .  :  :  |
                    |" .  |  :  .  |
                    |mt-2_;----.___|''')
            if choice3 == 'r':
                print("game over you have fell into lava")
            elif choice3 == 'y':
                print("you win!!! you have found the treasure")
            else:
                print("game over you have beenbitten by zombie")
        else:
            print('you have entered a dry land with out water and you have walked and walked without water you have died "Game over"')

    else:
        print("oh noo if can't explore you can't go further")
else:
    print("hope to see to again")
