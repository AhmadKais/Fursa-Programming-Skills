class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

    def reverse(self):
        if not self.head or not self.head.next_node:
            return

        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def find_middle(self):
        middle = self.head
        iterator = self.head.next_node
        while iterator:
            if not iterator.next_node:
                break
            iterator = iterator.next_node.next_node
            middle = middle.next_node

        return middle.data

    def has_cycle(self):
        if not self.head:
            return False

        slow = self.head
        fast = self.head.next_node  # Move fast by 2 steps initially

        while fast and fast.next_node:
            if slow == fast:
                return True  # Cycle detected

            slow = slow.next_node
            fast = fast.next_node.next_node

        return False  # No cycle found

    def connect_list(self):
        head = self.head
        itr = head
        cycle_begin = head.next_node
        while itr.next_node:
            itr = itr.next_node
        itr.next_node = cycle_begin
        return

if __name__ == "__main__":
    linkList = LinkedList()
    linkList.append(5)
    linkList.append(4)
    linkList.append(3)
    linkList.append(2)
    linkList.append(1)
    linkList.display()
    linkList.reverse()
    linkList.display()
    print(linkList.find_middle())
    print(linkList.has_cycle())
    linkList.connect_list()
    print(linkList.has_cycle())




