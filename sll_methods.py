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
            return self
        else:
            runner = self.head

            while runner.next != None:
                runner = runner.next
            newnode = Node(value)
            runner.next = newnode
        return self

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
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
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

    def length(self):
        if self.head == None:
            print(f'SLL length = 0')
            return 0
        else:
            cntr = 0
            runner = self.head
            if runner.next != None:
                while runner.next != None:
                    cntr += 1
                    runner = runner.next
                print(f'SLL length = {cntr + 1}')
                return cntr + 1
            print(f'SLL length = 1')
            return 1

#*****************************************************************
        
newSLL = SLL()
newSLL.append(5).append(6).append(3).append(8).addToFront(20).addToFront(-1)
newSLL.display()
# newSLL.contains(3)
# newSLL.contains(18)
newSLL.length()