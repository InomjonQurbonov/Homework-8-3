from main import Node, LinkedList

misollar = LinkedList()

misollar.insert(1)
str_ing = 'hello world'
list_el = ['hello world', 'hello world', 'hello world']
misollar.insert(49646)
misollar.insert(True)
misollar.insert(5)
misollar.insert(7.124)
misollar.insert(8)
misollar.insert(9)
misollar.insert(10)

element_counts = misollar.count_elements_by_type()
print(element_counts)

target_string = input('Enter a string: ')
misollar.insert(str_ing)
occurrences = misollar.find_string(target_string)
if occurrences:
    print(f"The string '{target_string}' is found at indexes: {occurrences}")
else:
    print(f"The string '{target_string}' is not found in the linked list.")

new_list = list_el
misollar.add_list(new_list)

print("Linked list before removing duplicates:")
current = misollar.head
while current:
    print(current.data)
    current = current.next

misollar.remove_duplicates()

print("\nLinked list after removing duplicates:")
current = misollar.head
while current:
    print(current.data)
    current = current.next