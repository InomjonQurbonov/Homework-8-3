class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def count_elements_by_type(self):
        counts = {'str': 0, 'int': 0, 'bool': 0, 'list': 0, 'other': 0}
        current = self.head
        while current:
            data_type = type(current.data).__name__
            if data_type == 'str':
                counts['str'] += 1
            elif data_type == 'int':
                counts['int'] += 1
            elif data_type == 'bool':
                counts['bool'] += 1
            elif data_type == 'list':
                counts['list'] += 1
            else:
                counts['other'] += 1
            current = current.next
        return counts

    def find_string(self, target):
        occurrences = []
        index = 0
        current = self.head
        while current:
            if isinstance(current.data, str) and current.data == target:
                occurrences.append(index)
            index += 1
            current = current.next
        return occurrences

    def add_list(self, data_list):
        for data in data_list:
            self.insert(data)

    def remove_duplicates(self):
        if self.head is None:
            return

        current = self.head
        seen = {current.data}

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next
