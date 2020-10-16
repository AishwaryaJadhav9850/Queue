# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:55:00 2020

@author: Admin
"""

class DeQueueList:
    """ Circular Double Ended Queue Implementation using List"""
    
    CAPACITY=3
    
    def __init__(self):
        self.queue=[None] * DeQueueList.CAPACITY
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
        self.rear=prev_len-1
    
    def enqueueRear(self):
        i=int(input("Enter the element to enqueue into the Queue:-"))
        if self.rear == -1:
            self.rear+=1
            self.front+=1
            self.queue[self.rear]=i       
            self.size+=1
            return
        if ((self.rear+1)%len(self.queue))==self.front:
            self.resize()
        self.rear=(self.rear+1)%len(self.queue)
        self.queue[self.rear]=i       
        self.size+=1
    
    
    def enqueueFront(self):
        i=int(input("Enter the element to enqueue into the Queue:-"))
        l=len(self.queue)
        if self.rear == -1:
            self.rear+=1
            self.front+=1
        if ((self.rear+1)%l)==self.front:
            self.resize()
        self.front=((self.front-1)+l)%l
        self.queue[self.front]=i
        self.size+=1
    
        
        
    
    def display(self):
        if self.size==0 :
            print('Queue is Empty!')
            return
        print("\n")
        for i in self.queue:
            print(i ,end="-->")
            
    def dequeueFront(self):     
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
     
    def dequeueRear(self):
        if self.size==0 :
            print('Queue is Empty!')
            return
        l=len(self.queue)
        print("Dequeued Item is ",self.queue[self.rear])
        self.queue[self.rear]=None
        self.rear=((self.rear-1)+l)%l
        self.size-=1
        
         
         
Q=DeQueueList()
while(1):    
    print("\n1. Enqueue at Rear")
    print("2. Enqueue at Front")
    print("3. Dequeue at Rear")
    print("4. Dequeue at Front")
    print("5. Display")
    print("6. isEmpty")
    print("7. EXIT")
    ch=int(input("Enter your choice:-"))
    if ch==1:
        Q.enqueueRear()
        Q.display()
    elif ch==2:
        Q.enqueueFront()
        Q.display()
    elif ch==3:
        Q.dequeueRear()
        Q.display()
    elif ch==4:
        Q.dequeueFront()
        Q.display()
    elif ch==5:
        Q.display()
    elif ch==6:
        if Q.is_empty():
            print("Queue is Empty")
        else:
            print("Queue is NOT Empty")
    elif ch==7:
        break
    else:
        print("Please enter correct choice!")       
        
        
        
        
        