class Node:
    def __init__(self, inputVal):
        self.value = inputVal
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        newnode = Node(value)
        if self.top == None: 
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
        return self

    def pop(self):
        if self.top != None:
            topvalue = self.top.value
            self.top = self.top.next
            # x = {
            #     'value': topvalue,
            #     'self': self
            # }

            return topvalue
        else:
            print("nothing to pop aka you got no pancakes")
            return self

    def size(self):
        count = 0
        if self.top == None:
            return count
        else:
            runner = self.top
            while runner != None:
                count += 1
                runner = runner.next
            print(count)
            return count

def compareStacks(stack1, stack2):
    if stack1 == None or stack2 == None:
        return False

    if stack1.size() != stack2.size():
        return False
    else:
        runner1 = stack1.top
        runner2 = stack2.top
        while runner1 != None:
            if runner1 != runner2:
                return False
            else:
                runner1 = runner1.next
                runner2 = runner2.next
        return True
