import random
l=["Rock","Paper","Scissor"];
while True:
    ccnt=0;
    ucnt=0;
    uc=int(input('''
     Game Start.....
     1.Yes
     2.No | Exit
        '''));
    if uc==1:
           for i in range(1,6):
            a=int(input('''
           1.Rock
           2.Scissor
           3.Paper\nYour choice: '''))
            if a==1:
               ch="Rock";
            elif a==2:
                ch="Scissor";
            elif a==3:
               ch="Paper";
            else:
               print("invalid input");
               break;    
            c=random.choice(l);
            if(c==ch):
               print("Your pick : ",ch);
               print("Computer pick : ",c);
               print("Draw\n")
               ccnt=ccnt+1;
               ucnt=ucnt+1;
            elif(ch=="Rock" and c=="Scissor") or (ch=="Scissor" and c=="Paper") or (ch=="Paper"and c=="Rock"):
               print("Your pick : ",ch);
               print("Computer pick : ",c); 
               print("You won\n");
               ucnt=ucnt+1;
            else:
               print("Your pick : ",ch);
               print("Computer pick : ",c); 
               print("Computer won\n");
               ccnt=ccnt+1;          
           print("Your score : ",ucnt,"\nComputer Score : ",ccnt);
           if(ccnt>ucnt):
            print("You Lose");
           elif(ccnt<ucnt):
             print("You Won");
           else:
            print("Game Draw");                            
    else:
           break;
