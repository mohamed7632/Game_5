c=[]
import random
arrayOfletters=["A","B","C","D","E","F","G","H","I","J","A","B","C","D","E","F","G","H","I","J"]
random.shuffle(arrayOfletters)
arrayOfnums=["1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0"]
array=["1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0"]
score1=0
score2=0
counter=0
W=1
b=True
while b:
    print("Window: ",end=" ")
    for i in range (0,20):
        print(arrayOfnums[i],end=" ")
    print()
    if(W%2==1):
        print("Player#1_ score",score1,":",end=" ")
    elif(W%2==0):
        print("Player#2_ score",score2,":",end=" ")
    nums=input()
    a=nums.split(", ")
    num1=int(a[0])
    num2=int(a[1])
    if(num1 <= 20 and num2 <= 20 and num1>0 and num2>0 and num1!=num2) :
            arrayOfnums[num1-1]=arrayOfletters[num1-1]
            arrayOfnums[num2-1]=arrayOfletters[num2-1]
            print("Window: ",end=" ")
            for i in range (0,20):
                print(arrayOfnums[i],end=" ")
            if (arrayOfnums[num1-1]!=arrayOfletters[num2-1]):
                arrayOfnums[num1-1]=array[num1-1]
                arrayOfnums[num2-1]=array[num2-1]    
            if(arrayOfletters[num1-1] == arrayOfletters[num2-1]):
                arrayOfnums[num1-1]="*"
                arrayOfnums[num2-1]="*"
                counter+=1
                if(W%2 == 1):
                        score1+=1
                elif(W%2 == 0):
                        score2+=1
            print()    
            print("screen is cleared ")
    else:
        print("please enter a number between 1:20 ")
        W-=1
    print()
    W+=1
    if(counter==10):
            b=False
print()
if(score1 > score2 ):
    print(" Player 1 wins the game ")
elif(score2 > score1 ):
    print(" Player 2 wins the game ")
else:
    print(" It is a draw :( ")

