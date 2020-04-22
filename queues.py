class Node:
    def __init__(self, inputVal):
        self.value = inputVal
        self.next = None

class SLQueue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, inputVal):
        newNode = Node(inputVal)
        if self.front == None:
            self.front = newNode
            self.back = newNode
            return self
        else:
            self.back.next = newNode
            self.back = self.back.next
            return self
    
    def dequeue(self):
        returnVal = None
        if self.front == None:
            return returnVal
        if self.front.next == None:
            returnVal = self.front.value
            self.front = None
            self.back = None
            return returnVal
        else:
            returnVal = self.front.value
            self.front = self.front.next
            return returnVal
    
    def frontVal(self):
        if self.front == None:
            return None
        else:
            return self.front.value

    def contains(self, inputVal):
        if self.front == None:
            return False
        else:
            runner = self.front
            while runner != None:
                if runner.value == inputVal:
                    return True
                else:
                    runner = runner.next
            return False
    
    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    def size(self):
        nodeCnt = 0
        if self.front == None:
            return nodeCnt
        else:
            runner = self.front
            while runner != None:
                nodeCnt += 1
                runner = runner.next
            return nodeCnt
    
    

newQueue = enqueue(5).enqueue(8).enqueue(15)