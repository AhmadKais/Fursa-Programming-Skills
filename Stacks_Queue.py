from distutils.command.check import check
from queue import Queue

class StackWithTwoQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.elements_num = 0

    def insert(self,element):
        self.queue1.put(element)
        self.elements_num+=1

    def pop(self):
        if self.elements_num == 0:
            return None
        while self.elements_num != 1:
            self.queue2.put(self.queue1.get())
            self.elements_num -=1

        pop_value = self.queue1.get()
        self.elements_num-=1

        while not self.queue2.empty():
            self.queue1.put(self.queue2.get())
            self.elements_num +=1

        return pop_value


class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):

        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop element from stack2 for dequeue
        return self.stack2.pop()

# for the third function i will be using a stack
def check_parentheses(string):
    string = list(string)
    stack = []
    for item in string:
        if not stack:
            stack.append(item)
        else:
            if stack[-1] == "{" and item == "}":
                stack.pop()
            else:
                stack.append(item)
    if not stack:
        return True
    return False

if __name__ == "__main__":
    # Test the stack implementation
    stack = StackWithTwoQueues()
    stack.insert(1)
    stack.insert(2)
    stack.insert(3)

    print(stack.pop())  # Should print 3
    print(stack.pop())  # Should print 2
    print(stack.pop())  # Should print 1

    # Test the queue implementation
    queue = QueueWithTwoStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.dequeue())  # Should print 1
    print(queue.dequeue())  # Should print 2
    print(queue.dequeue())  # Should print 3
    print(queue.dequeue())  # Should print None (queue is empty)

    #third function tests
    print(check_parentheses("{{}}{"))
    print(check_parentheses("}}{{"))
    print(check_parentheses("{{}}"))
