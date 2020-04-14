# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 00:28:43 2020

@author: Shannon Singh
"""


print("winning rules of rock paper scissor"
      +"\trock vs paper----> paper\n"
      +"\trock vs scissor----> rock\n"
      +"\tpaper vs scissor----> scissor")

while True:
    print("enter choice \n1.rock \n2.paper \n3.scissor")
    user_choice=input("user turn:")
    user_choice.islower()
    print ("user has choosen: ",user_choice)
    
    import random
    comp_choice=random.choice(['rock','paper','scissor'])
    
    print("\t" + user_choice + "\n V/S \n" + "\t" + comp_choice)
    
    result=None
    
    if(user_choice=="rock" and comp_choice=="paper"):
        result="paper"
    elif(user_choice=="paper" and comp_choice=="rock"):
        result="paper"
    elif(user_choice=="rock" and comp_choice=="scissor"):
        result="rock"
    elif(user_choice=="scissor" and comp_choice=="rock"):
        result="rock"
    else:
        result="scissor"
        
    
    if(user_choice==comp_choice):
        print("Draw")
    elif(result==user_choice):
        print("<---user wins--->")
    else:
        print("<---computer wins--->")
        
        
    ans=input("do you want to continue?  (y/n)")
    if(ans=="n" or ans=='N'):
            break
        
print("thanks for playing rock paper scissors")
            
    
        
        