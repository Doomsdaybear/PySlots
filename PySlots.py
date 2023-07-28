import os
import time as t
import colorama as c
import random as r
def clear() :
    os.system('cls')
def main(cash) :
    clear()
    print(c.Fore.WHITE, "Please enter the number of the machine you would like to play: \n")
    print(c.Fore.WHITE, """
    [1] Standard Python Cabinet (1, 11, 111 for reel pictures. Simple 3 reel, 1 frame cabinet)

    """)
    cab_choice = input("")
    if cab_choice == "1" or "[1]" :
        clear()
        print(c.Fore.GREEN, "Alright! Please select your betting amount (Total cash:  ", cash, ")")
        be = input("")
        bet = int(be)
        if bet > cash :
            clear()
            print(c.Fore.RED, "Let's try that again...")
            t.sleep(4)
            main(cash)
        if bet < 0 :
            clear()
            print(c.Fore.RED, "Let's try that again...")
            t.sleep(4)
            main(cash)
        clear()
        print(c.Fore.GREEN, "Is this your final bet? (y/n) \n")
        finale = input("")
        if finale == "n" or "N" :
            main(cash)
        if finale == "y" or "Y" :
            clear()
            print(c.Fore.GREEN, "Alright, starting spin...\n")
            t.sleep(4)
            reelone = r.randint(0,4)
            if reelone == 1 :
                print(c.Fore.RED, "[1]")
                reeltwo = r.randint(0,4)
                if reeltwo == 1 :
                    print(c.Fore.RED, "[1]")
                    reelthree = r.randint(0,4)
                    if reelthree == 1 :
                        print(c.Fore.RED, "[1]")
                        print(c.Fore.GREEN, "You win! You're bet has been doubled and returned to you.") # [1][1][1]
                        t.sleep(3)
                        cash += bet * 2
                        main(cash)
                    if reelthree == 2 :
                        print(c.Fore.YELLOW, "[11]")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[1][1][11]
                        cash -= bet
                        t.sleep(3)
                        main(cash)

                    if reelthree == 2 :
                        print(c.Fore.GREEN, "[111]")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[1][1][111]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                if reeltwo == 2 :
                    print(c.Fore.YELLOW, "[11]")
                    reelthree = r.randint(0,4)
                    if reelthree == 1 :
                        print(c.Fore.RED, "[1] \n")
                        print("Sorry, no cash this time. Bet has been subtracted from your account.") #[1][11][1]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    if reelthree == 2 :
                        print(c.Fore.YELLOW, "[11] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") # [1][11][11]
                        cash -= bet
                        t.sleep(3)
                        main(cash)


                    if reelthree == 3 :
                        print(c.Fore.GREEN, "[111] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[1][11][111]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                if reeltwo == 3 :
                    print(c.Fore.GREEN, "[111]")
                    reelthree = r.randint(0,4)
                    if reelthree == 1 :
                        print(c.Fore.RED, "[1] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") # [1] [111] [1]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    if reelthree == 2 :
                        print(c.Fore.YELLOW, "[11] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[1][111][11]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    if reelthree == 3 :
                        print(c.Fore.GREEN, "[111] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") # [1] [111] [111]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
            if reelone == 2 :
                print(c.Fore.YELLOW,"[11]")
                reeltwo = r.randint(0,4)
                if reeltwo == 1 :
                    print(c.Fore.RED, "[1]")
                    reelthree = r.randint(0,4)
                    if reelthree == 1 :
                        print(c.Fore.RED, "[1] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[11] [1] [1]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    if reelthree == 2 :
                        print(c.Fore.YELLOW, "[11] \n") #[11][1][11]
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.")
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    if reelthree == 3 :
                        print(c.Fore.GREEN, "[111] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[11][1][111]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                if reeltwo == 2 :
                    print(c.Fore.YELLOW, "[11]")
                    reelthree = r.randint(0,4)
                    if reelthree == 1 :
                        print(c.Fore.RED, "[1] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[11][11][1]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    if reelthree == 2 :
                        print(c.Fore.YELLOW, "[11] \n")
                        print(c.Fore.GREEN, "You win! You're bet has been tripled and returned to you.") #[11][11][11]
                        cash += bet * 3
                        t.sleep(3)
                        main(cash)
                    if reelthree == 3 :
                        print(c.Fore.GREEN, "[111] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[11][11][111]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                if reeltwo == 3 :
                    print(c.Fore.GREEN, "[11]")
                    reelthree = r.randint(0,4)
                    if reelthree == 1 :
                        print(c.Fore.RED, "[1] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[11][111][1]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    if reelthree == 2 :
                        print(c.Fore.YELLOW, "[11] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[11][111][11]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    if reelthree == 3 :
                        print(c.Fore.GREEN, "[111] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.")#[11][111][111]
            if reelone == 3 :
                print(c.Fore.RED, "[1]")
                reeltwo = r.randint(0,4)
                if reeltwo == 1 :
                    print(c.Fore.RED, "[1]")
                    reelthree = r.randint(0,4)
                    if reelthree == 1 :
                        print(c.Fore.RED, "[1] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.")#[111][1][1]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    if reelthree == 2 :
                        print(c.Fore.YELLOW, "[11] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.")#[111][1][11]
                        cash -= bet
                        t.sleep(3)
                        main(cash)

                    if reelthree == 3 :
                        print(c.Fore.GREEN, "[111] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.")#[111][1][111]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                if reeltwo == 2 :
                    print(c.Fore.YELLOW, "[11]")
                    reelthree = r.randint(0,4)
                    if reelthree == 1 :
                        print(c.Fore.RED, "[1] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[111][11][1]
                        cash -= bet
                        t.sleep(3)
                        main(cash)

                    if reelthree == 2 :
                        print(c.Fore.YELLOW, "[11] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.")#[111][11][11]
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    if reelthree == 3 :
                        print(c.Fore.GREEN, "[111] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.")#[111][11][111]

                if reeltwo == 3 :
                    print(c.Fore.GREEN, "[111]")
                    reelthree = r.randint(0,4)
                    if reelthree == 1 :
                        print(c.Fore.GREEN, "[1] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.") #[111][111]#[1]

                    if reelthree == 2 :
                        print(c.Fore.YELLOW, "[11] \n")
                        print(c.Fore.RED, "Sorry, no cash this time. Bet has been subtracted from your account.")
                        cash -= bet
                        t.sleep(3)
                        main(cash)
                    
                    if reelthree == 3 :
                        print(c.Fore.GREEN, "[111] \n")
                        print(c.Fore.GREEN, "You win! You're bet is now x15 and returned to you")
                        cash += bet * 15
                        t.sleep(3)
                        main(cash)

                
main(cash=100)