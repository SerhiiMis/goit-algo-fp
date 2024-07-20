class Node:
    def __init__(self, data=None):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Creating a new node
        new_node.next = self.head  
        self.head = new_node  # The head of the list points to the new node

    def insert_at_end(self, data):
        new_node = Node(data)  
        if self.head is None:
            self.head = new_node  
        else:
            cur = self.head
            while cur.next:
                cur = cur.next  
            cur.next = new_node  # Вставка нового вузла в кінець списку

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)  
        new_node.next = prev_node.next  
        prev_node.next = new_node  

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next  # Якщо головний вузол містить ключ, видаляємо його
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next  # Пошук вузла за ключем
        if cur is None:
            return
        prev.next = cur.next  # Виключення вузла з ланцюга
        cur = None

    def search_element(self, data: int) -> Node or None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur  # Повернення вузла, якщо дані співпадають
            cur = cur.next
        return None  # Повернення None, якщо вузол не знайдено

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Виведення даних вузла
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Збереження наступного вузла
            current.next = prev  # Реверсування поточного вузла
            prev = current  # Перехід до наступного вузла
            current = next_node
        self.head = prev  # Оновлення голови списку

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head  # Базовий випадок рекурсії

        middle = self.get_middle(head)  # Знаходження середини списку
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)  # Рекурсивне сортування лівої половини
        right = self.merge_sort(next_to_middle)  # Рекурсивне сортування правої половини

        sorted_list = self.sorted_merge(left, right)  # Злиття двох відсортованих половин
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next  

        return slow  # Повернення середнього вузла

    def sorted_merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result

    def sort(self):
        self.head = self.merge_sort(self.head)  # Виклик сортування злиттям для голови списку

def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)  # Створення тимчасового вузла
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next  # Перехід до наступного вузла

    if l1:
        tail.next = l1  # Додавання залишків l1
    if l2:
        tail.next = l2  # Додавання залишків l2

    return dummy.next  # Повернення голови об'єднаного списку

# Приклад використання
llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

merged_list = LinkedList()
merged_list.head = merge_two_sorted_lists(llist1.head, llist2.head)

print("Об'єднаний відсортований зв'язний список:")
merged_list.print_list()

llist = LinkedList()
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Зв'язний список до реверсування:")
llist.print_list()

llist.reverse()

print("Зв'язний список після реверсування:")
llist.print_list()

print("Зв'язний список до сортування:")
llist.print_list()

llist.sort()

print("Зв'язний список після сортування:")
llist.print_list()
