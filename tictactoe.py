board=["0","1","2","3","4","5","6","7","8"]
def player1(n):
    board[n]='X'
def player2(m):
    board[m]='O'          
def combi1(m):
    if ((board[0]==board[1]and board[1]==board[2]and board[1]==m)):
        return 1
    elif((board[3]==board[4]and board[4]==board[5]and board[4]==m)):
        return 1
    elif((board[3]==board[4]and board[4]==board[5]and board[4]==m)):
        return 1
    elif((board[0]==board[3]and board[3]==board[6]and board[3]==m)):
        return 1
    elif((board[1]==board[4]and board[4]==board[7]and board[4]==m)):
        return 1
    elif((board[2]==board[5]and board[5]==board[8]and board[5]==m)):
        return 1
    elif((board[0]==board[4]and board[4]==board[8]and board[4]==m)):
        return 1
    elif((board[2]==board[4]and board[4]==board[6]and board[4]==m)):
        return 1
    else:
        return 0
def combi2(n):    
    if ((board[0]==board[1]and board[1]==board[2]and board[1]==n)):
        return 1
    elif((board[3]==board[4]and board[4]==board[5]and board[4]==n)):
        return 1
    elif((board[3]==board[4]and board[4]==board[5]and board[4]==n)):
        return 1
    elif((board[0]==board[3]and board[3]==board[6]and board[3]==n)):
        return 1
    elif((board[1]==board[4]and board[4]==board[7]and board[4]==n)):
        return 1
    elif((board[2]==board[5]and board[5]==board[8]and board[5]==n)):
        return 1
    elif((board[0]==board[4]and board[4]==board[8]and board[4]==n)):
        return 1
    elif((board[2]==board[4]and board[4]==board[6]and board[4]==n)):
        return 1
    else:
        return 0
def status():
   print("Current Status:")
   for k in range(0,3):
       print(board[k],end=" ")
   print("\n")    
   for l in range(3,6):
       print(board[l],end=" ")
   print("\n")
   for j in range(6,9):
       print(board[j],end=" ")
        
wi1=0
wi2=0
i=0
j=0
print("player1",'X')
print("player2",'O')
while wi1==0 and wi2==0 and i!=9:
      print("\n")
      print("Player1-> ","give valid location(0 to 8)")
      status()
      a=int(input())
      if a>=0 and a<=8 and (board[a]!="X" and board[a]!="O"):
         player1(a)
         wi1=combi1('X')
         i+=1
         status()    
         if wi1==1:
           break
         if i==9:
           status()
           break
      else:
         print("..invalid location..")
         continue
      print("\n")  
      print("Player2-> ","give valid location(0 to 8)")
      print("\n")
      status()
      b=int(input())
      if b>=0 and b<=8 and (board[b]!="X" and board[b]!="O"):
         player2(b)
         wi2=combi2('O')
         i+=1
         status()
      else:
         print("..invalid location..")
         while j==0:
              print("enter again")
              c=int(input())
              if c>=0 and c<=8 and (board[c]!="X" and board[c]!="O"):
                  j=1
                  player2(c)
              else:
                  j=0
if(wi1==1):
     print("\n")
     print("**Player 1 wins**")
elif(wi2==1):
     print("**Player 2 wins**")
else:
    print("\n")
    print("**Draw**")
print(" FINAL RESULT:")
status()
