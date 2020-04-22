class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None # Why not :-)

    def addToBack(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            return self
        else:
            runner = self.head

            while runner.next != None:
                runner = runner.next
            runner.next = newnode
            self.tail = newnode
        return self

    def display(self):
        runner = self.head
        output = ""
        while (runner != None):
            output += f"{runner.value}-->"
            # print(runner.next)
            runner = runner.next
        print (output)
        return self

#*****************My Code******************************************
#   4/16/2020
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
            print(f'sll contains {val}: False')
            return False
        else:
            runner = self.head
            while runner.next != None:
                if runner.value == val:
                    print(f'sll contains {val}: True')
                    return True
                else:
                    runner = runner.next
            if runner.value == val:
                    print(f'sll contains {val}: True')
                    return True
            else:
                print(f'sll contains {val}: False')
                return False
#*************
#   4/15/2020
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

    def removeFront(self):
        sllLength = self.length()
        if sllLength == 0:
            return self
        elif sllLength == 1:
            self.head = None
            return self
        else:
            runner = self.head
            self.head = runner.next
            runner = None
            return self

    def removeBack(self):
        sllLength = self.length()
        if sllLength == 0:
            return self
        elif sllLength == 1:
            self.head = None
            return self
        else:
            runner = self.head.next
            prevNode = self.head
            while runner.next != None:
                runner = runner.next
                prevNode = prevNode.next
            runner = None
            self.tail = prevNode
            self.tail.next = None
            return self

#*************
#   4/16/2020
    def minListValue(self):
        sllLength = self.length()
        if sllLength == 0:
            return None
        elif sllLength == 1:
            return self.head.value
        else:
            runner = self.head
            minValue = self.head.value
            while runner.next != None:
                if runner.value < minValue:
                    minValue = runner.value
                runner = runner.next
            if runner.value < minValue:
                    minValue = runner.value
        print (minValue)
        return minValue

    def maxListValue(self):
        sllLength = self.length()
        if sllLength == 0:
            return None
        elif sllLength == 1:
            return self.head.value
        else:
            runner = self.head
            maxValue = self.head.value
            while runner.next != None:
                if runner.value > maxValue:
                    maxValue = runner.value
                runner = runner.next
            if runner.value > maxValue:
                    maxValue = runner.value
        print (maxValue)
        return maxValue

    def minToFront(self):
        if self.length() <= 1:
            return self
        else:
            minValue = self.minListValue()
            runner = self.head.next
            prevNode = self.head
            while runner.next != None:
                if runner.value == minValue:
                    prevNode.next = runner.next
                    runner.next = self.head
                    self.head = runner
                    runner = prevNode.next
                    continue
                runner = runner.next
                prevNode = prevNode.next
            if runner.value == minValue:
                    prevNode.next = None
                    runner.next = self.head
                    self.head = runner
        return self

    def maxToBack(self):
        sllLength = self.length()
        maxValue = self.maxListValue
        if sllLength <= 1: # If the sll is empty or contains 1 node there is nothing to organize 
            return self
        elif sllLength == 2 and self.head.value > self.head.next.value: # If there are two nodes and the first is greater than the second reverse them
            self.tail.next = self.head
            self.head.next = None
            self.head = self.tail
            self.tail = self.tail.next
            return self
        else:
            runner = self.head.next
            prevNode = self.head
            firstMoved = None
            while runner.next != None and runner != firstMoved:
                if runner.value == maxValue:
                    if firstMoved == None:
                        firstMoved = runner 
                    prevNode.next = runner.next
                    self.tail.next = runner
                    self.tail = runner
                    runner = prevNode.next
                    self.tail.next = None
                    continue
                runner = runner.next
                prevNode = prevNode.next
            return self

#*************
#   4/17/2020

    def appendVal(self, inputValue, after=None):
        if after == None or self.head == None:
            self.addToBack(inputValue)
        else:
            newNode = Node(inputValue)
            runner = self.head
            while runner.next != None:
                if runner.value == after:
                    newNode.next = runner.next
                    runner.next = newNode
                    return self
                runner = runner.next
            self.addToBack(inputValue)
            return self

                
#******************************************************************
#   Code to test the functions
        
newSLL = SLL()
newSLL.addToBack(5).addToBack(6).addToBack(3).addToBack(8).addToFront(20).addToFront(-1).display()
newSLL.appendVal(31, 3)
newSLL.display()

