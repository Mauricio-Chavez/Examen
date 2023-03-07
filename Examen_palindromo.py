class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def append(self, value):
        if self.head is None:
            self.head=node(value)
            self.tail=self.head
            self.length=1
        else:
            new_nodo=node(value)
            self.tail.next=new_nodo
            new_nodo.prev=self.tail
            self.tail=new_nodo
            self.length +=1
    def palindromo(self):
        tem1=self.head
        tem2=self.tail
        c=0
        for i in range(0,self.length):
            if tem1.value==tem2.value:
                tem1=tem1.next
                tem2=tem2.prev
                c+=1
            else:
                print("Las cadena ingresada NO es palindrome")
                exit()
            if c==self.length:
                print("Las cadenas ingresadas son palindromes")
    def print_list(self,s):
        if s==1:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
        else:
            temp = self.tail
            for i in range (1,self.length+1):
                print(temp.value)
                temp=temp.prev

node1=DoublyLinkedList()
a=str(input(("Ingresa la palabra 1: ")))
a=a.replace(" ","")
a=a.lower()
for i in a:
    node1.append(i)

node1.print_list(1)
node1.palindromo()