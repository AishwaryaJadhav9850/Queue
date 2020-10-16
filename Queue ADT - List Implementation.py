# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 18:16:30 2020

@author: Admin
"""

class QueueList:
    CAPACITY=3
    
    def __init__(self):
        self.queue=[None] * QueueList.CAPACITY
        self.size=0
        self.rear=-1
        self.front=-1
    
    def is_empty(self):
        if self.size==0 :
            return True
        else:
            print("Queue size is ",self.size)
            self.display()
        
    def resize(self):
        temp=self.queue.copy()
        ftemp=self.front
        prev_len=len(self.queue)
        print('len is ',prev_len)
        self.queue=[None] * (2 * prev_len)
        for i in range(prev_len):
           self.queue[i]=temp[ftemp]
           ftemp=(ftemp+1)%prev_len
        self.front=0
        self.rear=prev_len
    
    def enqueue(self):
        i=int(input("Enter the element to enqueue into the Queue:-"))
        if self.rear == -1:
            self.rear+=1
            self.front+=1
        self.queue[self.rear]=i
        self.rear=(self.rear+1)%len(self.queue)
        if self.rear==self.front:
            self.resize()
        self.size+=1
        print()
    
    def display(self):
        if self.size==0 :
            print('Queue is Empty!')
            return
        print("\n")
        for i in self.queue:
            print(i ,end="-->")
            
    def dequeue(self):     
        if self.size==0 :
            print('Queue is Empty!')
            return
        print("Dequeued Item is ",self.queue[self.front])
        self.queue[self.front]=None
        self.front=(self.front+1)%len(self.queue)
        if self.front==self.rear:
            self.rear=-1
            self.front=-1
        self.size-=1
         
         
         
Q=QueueList()
while(1):    
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. isEmpty")
    print("5. EXIT")
    ch=int(input("Enter your choice:-"))
    if ch==1:
        Q.enqueue()
        Q.display()
    elif ch==2:
        Q.dequeue()
        Q.display()
    elif ch==3:
        Q.display()
    elif ch==4:
        if Q.is_empty():
            print("Queue is Empty")
        else:
            Q.display()
    elif ch==5:
        break
    else:
        print("Please enter correct choice!")       
        
        
        
        
        