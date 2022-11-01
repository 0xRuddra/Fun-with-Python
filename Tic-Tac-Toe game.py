plyr1=[]
plyr2=[]
check=0
def game():

   zero='X' if plyr1[0] else('0' if plyr2[0] else '1')
   one='X' if plyr1[1] else('0' if plyr2[1] else '2')
   two='X' if plyr1[2] else('0' if plyr2[2] else '3')
   three='X' if plyr1[3] else('0' if plyr2[3] else '4')
   four='X' if plyr1[4] else('0' if plyr2[4] else '5')
   five='X' if plyr1[5] else('0' if plyr2[5] else '6')
   six='X' if plyr1[6] else('0' if plyr2[6] else '7')
   seven='X' if plyr1[7] else('0' if plyr2[7] else '8')
   eight='X' if plyr1[8] else('0' if plyr2[8] else '9')

   print(f"|----|----|----|\n"
         f"| tic--tac--toe|\n"
         f"|----|----|----|\n"
         f"| {zero}  | {one}  | {two}  |\n"
         f"|----|----|----|\n"
         f"| {three}  | {four}  | {five}  |\n"
         f"|----|----|----|\n"
         f"| {six}  | {seven}  | {eight}  |\n"
         f"|----|----|----|")

def winCheck():
    # winCondition=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    xcon1=plyr1[0]+plyr1[1]+plyr1[2]
    xcon2=plyr1[3]+plyr1[4]+plyr1[5]
    xcon3=plyr1[6]+plyr1[7]+plyr1[8]
    xcon4=plyr1[0]+plyr1[3]+plyr1[6]
    xcon5=plyr1[1]+plyr1[4]+plyr1[7]
    xcon6=plyr1[5]+plyr1[8]+plyr1[2]
    xcon7=plyr1[0]+plyr1[4]+plyr1[8]
    xcon8=plyr1[4]+plyr1[6]+plyr1[2]

    ycon1=plyr2[0]+plyr2[1]+plyr2[2]
    ycon2=plyr2[3]+plyr2[4]+plyr2[5]
    ycon3=plyr2[6]+plyr2[7]+plyr2[8]
    ycon4=plyr2[0]+plyr2[3]+plyr2[6]
    ycon5=plyr2[1]+plyr2[4]+plyr2[7]
    ycon6=plyr2[5]+plyr2[8]+plyr2[2]
    ycon7=plyr2[0]+plyr2[4]+plyr2[8]
    ycon8=plyr2[4]+plyr2[6]+plyr2[2]

    if xcon1==3:
        print("x win")
        check=1
        exit()
    elif xcon2==3:
        print("x win")
        check=1
        exit()
    elif xcon3==3:
        print("x win")
        check=1
        exit()
    elif xcon4==3:
        print("x win")
        check=1
        exit()
    elif xcon5==3:
        print("x win")
        check=1
        exit()
    elif xcon6==3:
        print("x win")
        check=1
        exit()
    elif xcon7==3:
        print("x win")
        check=1
        exit()
    elif xcon8==3:
        print("x win")
        check=1
        exit()
    elif ycon2==3:
        print("y win")
        check=1
        exit()
    elif ycon3 == 3:
        print("y win")
        check=1
        exit()
    elif ycon4 == 3:
        print("y win")
        check=1
        exit()
    elif ycon5== 3:
        print("y win")
        check=1
        exit()
    elif ycon6 == 3:
        print("y win")
        check=1
        exit()

    elif ycon7 == 3:
        print("y win")
        check=1
        exit()

    elif ycon8== 3:
        print("y win")
        check=1
        exit()







if __name__ == '__main__':
    print("Welcome to the Tic-Tac-Toe Game")
    plyr1=[0 for i in range(9)]
    plyr2=[0 for i in range(9)]

    game()

    for i in range(2,10,2):

        mark1 = int(input("X's turn :"))
        plyr1[mark1-1] = 1
        game()




        mark2 = int(input("0's turn :"))
        plyr2[mark2-1] = 1
        game()



        winCheck()
    if(check==0):
        print("draw")









