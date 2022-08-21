import os 
import random
from queue import PriorityQueue
class Node:
    # Constructor to initialize the node object
    def __init__(self, name,address,restaraunt,order_no,order):
        self.name = name
        self.address= address
        self.restaraunt=restaraunt
        self.order_no= order_no
        self.order=order
        self.next = None
 
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def push(self,name,address,restaraunt,order_no,order):
        new_node = Node(name,address,restaraunt,order_no,order)
        new_node.next = self.head
        self.head = new_node
 
    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    def deleteNode(self, order_no):
         
        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.order_no == order_no):
                self.head = temp.next
                temp = None
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.order_no == order_no:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None

    def checkorder_ID(self):
        temp=self.head
        return temp.order_no

    def isEmpty(self):
        if self.head==None:
            return True
        return False

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        i=0
        while(temp):
            print("Order",i+1,":")
            print("Name:",temp.name)
            print("address:",temp.address)
            print("restaraunt chosen:",temp.restaraunt)
            print("Order_ID:",temp.order_no)
            print("Your order:",temp.order)
            temp = temp.next
            i+=1
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0
   
        pq = PriorityQueue()
        pq.put((0, start_vertex))
   
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)
   
            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D
#private function 
def removespace(string):
    return string.replace(" ", "")
#main
graph = Graph(9)
graph.add_edge(0,1,4)
graph.add_edge(0,7,8)
graph.add_edge(1,7,11)
graph.add_edge(1,2,8)
graph.add_edge(7,8,7)
graph.add_edge(7,6,1)
graph.add_edge(2,3,7)
graph.add_edge(2,8,2)
graph.add_edge(2,5,4)
graph.add_edge(8,6,6)
graph.add_edge(6,5,2)
graph.add_edge(3,5,14)
graph.add_edge(3,4,9)
graph.add_edge(5,4,10)
#Initialisation
dominoes=[1,4,5]
pizzahut=[0,3,6]
areas=['annanagar','ashoknagar','kodambakkam','porur','koyambedu','mylapore','t.nagar','pallavaram','kelambakkam']
oyalo=[2,7]
dist=[]
ll = LinkedList()
print("*--------------------------------------Welcome--------------------------------------*\n")
name=str(input("Enter your name:"))
adr=str(input("Enter your address:"))
os.system('cls')
oyalo_menu=[['Capsicum Tomatino',135],['Mushroom Delitto',140],['Chilli Manchurian Miso',135]]
pizzahut_menu=[['Taco Mexicana',150],['Pasta Italiono White',140],['Burger Pizza',110]]
dominoes_menu=[['Mexican Green Wave',170],['Double Cheese Margherita',120],['Pepperoni Classic',134]]
temp=adr
adr=adr.lower()
adr=removespace(adr)
for i in areas:
    if adr not in areas:
        flag=1
for i in range(len(areas)):
    if(adr==areas[i]):
        node_no=i+1
D=graph.dijkstra(node_no)
while(1):
    print("1.Order\n2.Cancel\n3.Exit        ")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        x=int(input("1.Dominoes\n2.Pizzahut\n3.Oyalo\nSelect your restaraunt:"))
        if(x==3):
            print("********Menu*********")
            i=1
            for food,price in oyalo_menu:
                print(i,food,":",price,"Rs")
                i+=1
            print("*********************")
        elif(x==2):
            print("********Menu*********")
            i=1
            for food,price in pizzahut_menu:
                print(i,food,":",price,"Rs")
                i+=1
            print("*********************")
        else:
            print("********Menu*********")
            i=1
            for food,price in dominoes_menu:
                print(i,food,":",price,"Rs")
                i+=1
            print("*********************")
        order=str(input("Enter your order:"))
        ll.push(name,temp,x,random.randint(100,220),order)
        print("********Details********\n")
        ll.printList()
        if(x==1):
            for i in dominoes:
                dist.append(D[i])
        elif(x==2):
            for i in pizzahut:
                dist.append(D[i])
        elif(x==3):
            for i in oyalo:
                dist.append(D[i])
        print("Your order will reach within",20+min(dist),"minutes")
        dist.clear()
        print("***********************\n")
    elif(ch==2):
        y=int(input("Enter your order_ID:"))
        if(ll.isEmpty()==True):
            print("No order has been placed")
        elif(y==ll.checkorder_ID()):
            a=int(input("Do you wish to proceed the cancellation\n1.YES\n2.NO\n"))
            if(a==1):
                print("Your order has been successfully cancelled")
                ll.deleteNode(y)
            else:
                print("Your order will be delivered soon")
        else:
            print("No such order was placed")
    else:
        break