# priority = {'*':3, '/':3,
#             '+':2, '-':2,
#             '(':1}
# expr = []
#
#
# class Stack:
#     def __init__(self):
#         self.data = []
#     def is_empty(self):
#         return len(self.data) == 0
#     def push(self, item):
#         self.data.append(item)
#     def pop(self):
#         return self.data.pop()
#     def peek(self):
#         return self.data[-1]
#
#
# operator = Stack()
# result = []
# tmp = input('식을 입력하세요: ')
#
# for i in tmp:
#     if i == ' ':
#         continue
#     expr.append(i)
#
# for i in expr:
#     if i == '(':
#         operator.push(i)
#     elif i in '+-*/':
#         if operator.is_empty():
#             operator.push(i)
#         else:
#             if priority[operator.peek()] >= priority[i]:
#                 result.append(operator.pop())
#                 operator.push(i)
#             else:
#                 operator.push(i)
#     elif i == ')':
#         while True:
#             a = operator.pop()
#             if a == '(':
#                 break
#             result.append(a)
#     else:
#         result.append(i)
#
# while not(operator.is_empty()):
#     result.append(operator.pop())
#
# print(''.join(result))



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add(self, node):
        if self.next is None:
            self.next = node
        else:
            n = self.next
            while True:
                if n.next is None:
                    n.next = node
                    break
                else:
                    n = n.next

    def select(self, idx):
        n = self.next
        for i in range(idx -1):
            n = n.next
        return n.data

    def delete(self, idx):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = t.next
        del t

    def pop(self, idx):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = t.next
        return t

    def prt(self):
        n = self.next

        while True:
            try:
                if n.next is None:
                    print(n.data, end=' ')
                    break
                else:
                    print(n.data, end=' ')
                    n = n.next
            except Exception:
                print('h')

        print()

    def insert(self, idx, node):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = node
        node.next = t

head = Node(None)

print(head.data, head.next)
head.add(Node("구독~"))
print(head.next.data)
head.add(Node("좋아요!"))
print(head.next.next.data)
head.add(Node("댓글!!"))
print(head.select(3))

head.insert(2, Node("g"))
head.prt()


