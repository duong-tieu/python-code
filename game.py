from random import randint
while True:
    print("You want to choose scissors, hammer or paper :" )
    player = input()
    computer = randint(0,2)

    if computer == 0 :
       computer = "Keo"
    if computer == 1:
       computer = "Bua"
    if computer == 2:
       computer = "Bao"

    print("-----")
    print("Ban chon " + player)
    print("May tinh chon " + computer) # type: ignore
    print("-----")   

    if player == computer:
        print("Draw")
    else : 
        if player == "Keo":
            if(computer == "Bao"):
                print("Win")
            if computer == "Bua" :
                print("Lost")    

        elif player == "Bua":
            if(computer == "Keo"):
                print("Win")
            if computer == "Bao" :
                print("Lost")  

        elif player == "Bao":
            if(computer == "Bua"):
                print("Win")
            if computer == "Keo" :
                print("Lost")  
        else :
            print("Nhap lai cho dung !")                    

    play_againt = input("Ban co muon bat dau lai cho choi khong ? (y/n): ").lower()
    if play_againt != "y":
       print("Cam on ban da choi!")
       break