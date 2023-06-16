# Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).

class List:
    def __init__(self):
        self.head = None  # выделение памяти под начало списка

    class Node:
        def __init__(self):
            self.value = None  # значения загружаемые в список
            self.next = None  # обьект ссылки для перехода

    def pushfront(self, value):
        node = List.Node()  # создание экземпляра узла
        node.value = value  # передача значения узлу
        node.next = self.head  # передача значения ссылки
        self.head = node  # назнечение начального узла

    def popfront(self):
        if self.head != None:  # проверка пустой ли список
            self.head = self.head.next  # удаления элемента с начала списка (замена значения)

    def pushback(self, value):
        node = List.Node()  # создание экземпляра узла
        node.value = value  # передача значения узлу
        if self.head == None: # проверка на пустоту списка
            self.head = node    # в случае пустого списка добовляется элемент в список
        else:
            cur = self.head  # наличие элемента
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def popback(self):
        if self.head != None:    # проверка пустой ли список или нет
            if self.head == None:
                self.head = None
            else:
                cur = self.head
                while cur.next.next != None:
                    cur = cur.next
                cur.next = None

    def reverse(self):
        pavorius = None  # предыдущий узел
        cur = self.head  # начальный узел
        while cur.next:  # цикл работает пока в списке есть элементы
            temp = cur.next  # сохранение предыдущего узла
            cur.next = pavorius  #перезапись следующего узла
            pavorius = cur  #запись нового значения предыдущего узла
            cur = temp  # запись нового значения начального узла
        self.head = cur  # смещение начального узла
        cur.next = pavorius # замена значений cur and cur.next


    def print(self):
        cur = self.head  # назначение первого элемента списка
        while (cur != None):  # проверка на наличие элемента в переменной cur
            print(f'{cur.value}', end=' ')  # отформатированный вывод
            cur = cur.next  # переход к следующему элементу повтарение цикла


lists = List()
for i in range(1, 10):
    lists.pushfront(i)

print('Source list')
lists.print()
print('\nReverse list')
lists.reverse()
lists.print()
input("\n\n\tPress Enter to Exit")








