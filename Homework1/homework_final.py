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
        self.color = False  # если false то чёрный иначе красный


class BlackRedTree:

    def __init__(self):
        self.root = None
        self.N = 0  # глубина дерева

    def size(self):  # функция вызова глубины дерева
        return self.N

    def is_red(self, node):  # функция получения цвета узла
        return str(node.color).lower() == 'red' if node else False

    def left_turn(self, node):

        """метод левостороннего поворота """

        new_node = node.right_descendant  # создаём указатель на новый узел
        node.right_descendant = new_node.left_descendant  # передаём значение  правому потомку родителя
        # значение  левого потомка  нынешнего правого потомка родителя
        new_node.left_descendant = node  # передаём левому потомку нового корня значение родителя
        new_node.color = node.color
        node.color = 'red'
        return new_node  # возвращаем узел

    def right_turn(self, node):

        """метод правостороннего поворота с обработкой случая пустой ноды для двух красных нод"""

        new_node = node.right_descendant  # создаём указатель на новый узел
        node.left_descendant = new_node.right_descendant  # передаём значение  левому потомку родителя
        # значение  правого потомка  нынешнего левого потомка родителя
        new_node.right_descendant = node  # передаём правому потомку нового корня значение старго корня
        new_node.color = node.color
        node.color = True
        return new_node  # возвращаем узел

    def swap_color(self, node):

        """Метод смены цвета"""

        node.color = 'Red'  # меняем цвет родителя
        node.right_descendant.color = 'Black'  # меняем цвет правого потомка на черный
        node.left_descendant.color = 'Black'  # меняем цвет левого  потомка на черный

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
                node.color = True
                return node

            if self.is_red(node.right_descendant) and not self.is_red(node.left_descendant):
                # Rotate left
                self.left_turn(node)

            if self.is_red(node.left_descendant) and self.is_red(node.left_descendant.left_descendant):
                # Rotate right
                self.right_turn(node)

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


# Проверка

t = BlackRedTree()  # создаём экземпляр класса
t.insert_node(5)  # добовляем узлы в кчд
t.insert_node(2)

print(t.size())  # размер дерева
print(t.root.value, t.root.color)  # цвет корня
