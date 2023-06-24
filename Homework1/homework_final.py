# Бинарное дерево
# Необходимо превратить собранное на семинаре дерево поиска в полноценное левостороннее красно-черное дерево.
# И реализовать в нем метод добавления новых элементов с балансировкой.
#
# Красно-черное дерево имеет следующие критерии:
# • Каждая нода имеет цвет (красный или черный)
# • Корень дерева всегда черный
# • Новая нода всегда красная
# • Красные ноды могут быть только левым ребенком
# • У краной ноды все дети черного цвета
#
# Соответственно, чтобы данные условия выполнялись,
# после добавления элемента в дерево необходимо произвести балансировку, благодаря
# которой все критерии выше станут валидными.
# Для балансировки существует 3 операции – левый малый поворот, правый малый поворот и смена цвета.
#
# Критерии оценивания:
# Слушатель превратить собранное на семинаре дерево поиска в
# полноценное левостороннее красно-черное дерево.
# реализовать в нем метод добавления новых элементов с балансировкой.
#



class Node:

    def __init__(self, value):
        self.value = value
        self.left_descendant = None
        self.right_descendant = None
        self.color = True  # если false то чёрный иначе красный


class BlackRedTree:

    def __init__(self):
        self.root = None
        self.N = 0  # глубина дерева

    def size(self):  # функция вызова глубины дерева
        return self.N

    def is_red(self, node):  # функция получения цвета узла
        if node:
            return node.color == True
        else:
            return False

    def left_turn(self, node):

        """метод левостороннего поворота """

        print("поворот на лево")
        new_node = node.right_descendant  # создаём указатель на новый узел
        node.right_descendant = new_node.left_descendant
        new_node.left_descendant = node  # передаём значение  левому потомку родителя
        # значение  левого потомка  нынешнего правого потомка родителя
        # передаём левому потомку нового корня значение родителя
        new_node.color = node.color
        node.color = True
        print(f"новое значение корня полсле поворота {new_node.color, new_node.value}")
        return new_node  # возвращаем узел

    def right_turn(self, node):

        """метод правостороннего поворота с обработкой случая пустой ноды для двух красных нод"""

        print('поворот на право')

        new_node = node.left_descendant  # создаём указатель на новый узел
        node.left_descendant = new_node.right_descendant  # передаём значение  левому потомку родителя
        # значение  правого потомка  нынешнего левого потомка родителя
        new_node.right_descendant = node  # передаём правому потомку нового корня значение старго корня
        new_node.color = node.color
        node.color = True
        print(f"новое значение корня после поворота {new_node.color, new_node.value}")
        return new_node  # возвращаем узел

    def swap_color(self, node):

        """Метод смены цвета"""

        print("смена цвета")

        node.color = True  # меняем цвет родителя
        node.right_descendant.color = False  # меняем цвет правого потомка на черный
        node.left_descendant.color = False  # меняем цвет левого  потомка на черный
        print(f"цвета потомков {node.left_descendant.color, node.right_descendant.color}")

    def insert_node(self, value):
        """метод Создания узла"""

        def __inserts_node(node, value):  # закрытый метод
            """Рекурсивная функция присваивания значения узла и
            создания потомков левого левого и правого """
            if not node:
                return Node(value)
            if value < node.value:  # добавление слева
                node.left_descendant = __inserts_node(node.left_descendant, value)
            elif value > node.value:  # добавление справа
                node.right_descendant = __inserts_node(node.right_descendant, value)
            else:  # Назначаем значение узла
                node.value = value
                node.color = 'Red'
                return node

            # Когда правый дочерний элемент красный а левый либо черный либо его не существует
            if self.is_red(node.right_descendant) and not self.is_red(node.left_descendant) \
                    or node.left_descendant is None:
                # Rotate left
                self.left_turn(node)

            # Когда левый ребенок и левый внук красные
            if self.is_red(node.left_descendant) and self.is_red(node.left_descendant.left_descendant):
                # Rotate right
                self.right_turn(node)

            # Смена цвета когда правый и левый потомок красные
            if self.is_red(node.left_descendant) and self.is_red(node.right_descendant):
                # Swap
                self.swap_color(node)

            self.N += 1
            return node

        self.root = __inserts_node(self.root, value)
        self.root.color = 'Black'
        return self.root

    def node_find(self, value):
        """метод поиска значения узла"""

        return self.__nodes_find(self.root, value)  # запуск рекусивной функции поиска узла

    def __nodes_find(self, root, value):  # закрытый метод
        """рекурсивные метод поиска узла"""
        if root == None:  # проверка на наличие узлов
            return None
        if root.value == value:  # проверка значения узла и значения которое ищем соответсвует оно корню или нет
            return root  # если да то возвращаем корень
        if value < root.value:  # проверяем значение меньше корня
            return self.__nodes_find(root.left_descendant, value)  # если меньше то запускаем рекурсию от левого потомка
        else:
            return self.__nodes_find(root.right_descendant,
                                     value)  # если больше то запускаем рекурсию от правого потомка
    def printing(self):
        root = self.root
        print(root.color, root.value)
        print(root.left_descendant.value.color)


# Проверка

t = BlackRedTree()  # создаём экземпляр класса

# осуществляется поворот дерева на лево как и должно
# for i in range(21):
#     t.insert_node(i)
#     print(t.size())

# Смена цвета
# t.insert_node(5)
# t.insert_node(4)
# t.insert_node(6)

#Поворот на право
# t.insert_node(7)
# t.insert_node(5)
# t.insert_node(4)

# flag = True
# while flag:
#     t.insert_node(input("Введите значение для добавления в дерево: "))
#     answer = input("если хотите продолжить нажмите y или q для выхода: ").lower()
#     if answer != 'y' and not 'q':
#         answer = input("Вы ввели не верное значение y или q для выхода: ")
#     if answer == 'q'.lower():
#             flag = False
#
# print('\n\t\tGood Bay'.upper())
