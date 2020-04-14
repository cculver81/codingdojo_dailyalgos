class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def append(self,value):

        if self.head == None:
            newnode = Node(value)
            self.head = newnode

        else:
            runner = self.head

            while runner.next != None:
                runner = runner.next
            newnode = Node(value)
            runner.next = newnode

    def display(self):
        runner = self.head
        output = ""
        while (runner != None):
            output += f"{runner.value}-->"
            print(runner.next)
            runner = runner.next
        print (output)
        return self

#*****************My Code******************************************
    def addToFront(self, val):
        if self.head == None:
            self.head = newNode
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        return self

    # def contains(self, val):
    #     if self.head == None:
    #         return False
    #     elif self.head.value == val:
    #         return True
    #     elif self.head.next == None:
    #         return False
    #     else:
    #         runner = self.head
    #         while runner.next != None:
    #             runner = runner.next
    #             if runner.value == val:
    #                 return True
    #     if runner.value == val:
    #         return True
    #     else:
    #         return False

    def contains(self, val): # refactor
        if self.head == None:
            return False
        else:
            runner = self.head
            while runner.next != None:
                if runner.value == val:
                    return True
                else:
                    runner = runner.next
            if runner.value == val:
                    return True
            else:
                return False
#*****************************************************************
        
newSLL = SLL()
newSLL.append(5)
newSLL.append(6)
newSLL.append(3)
newSLL.append(8)
newSLL.display()

newSLL.addToFront(20)
newSLL.display()
newSLL.addToFront(-1)
newSLL.display()
newSLL.contains(3)
newSLL.contains(18)