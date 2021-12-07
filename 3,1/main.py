from tabulate import tabulate
from math import fabs as n


# Решить систему линейных уравнений методом скалярной трехточечной прогонки.
# Выполнить оценку погрешности полученного решения по правой части.
# Вариант 8: 9.64 0.83 0 0 0                  1.885
#             -0.193 -7.07 0.684 0 0          1.257
#    A=       0 0.203 5.65 0.53 0         d = 2
#             0 0 0.354 3.142 0.094           15
#             0 0 0 0.86 4.709                9

class matrix:
    def __init__(self, a, b):
        self.matrixX = a
        self.glavediagonal = []
        self.nizdiagonal = []
        self.verhdiagonal = []
        self.b = b
        self.alfa = []
        self.betta = []
        self.x = []
        self.nedovolnoeB = []
        self.pogreshnost = []
        self.vectorpogreshnosti = [['вектор погрешности']]
        self.table = [['aльфа', 'бетта', 'x', 'погрешность']]

    def algoritm(self):
        # задает нижнюю, верхнюю и главную диагональ
        for i in range(len(self.matrixX)):
            self.glavediagonal.append(self.matrixX[i][i])
            if i + 1 < 5:
                self.verhdiagonal.append(self.matrixX[i][i + 1])
            else:
                self.verhdiagonal.append(self.matrixX[i][0])
            if i - 1 >= 0:
                self.nizdiagonal.append(self.matrixX[i][i - 1])
            else:
                self.nizdiagonal.append(self.matrixX[i][0])
        # вычисляет альфа и бетта
        for i in range(len(self.nizdiagonal)):
            if i == 0:
                self.alfa.append(-1 * (self.verhdiagonal[i] / self.glavediagonal[i]))
                self.betta.append(self.b[i] / self.glavediagonal[i])
                self.table.append([self.alfa[i], self.betta[i]])
            else:
                self.alfa.append(-1 * (self.verhdiagonal[i] /
                                       (self.nizdiagonal[i] * self.alfa[i - 1] + self.glavediagonal[i])))
                self.betta.append((self.b[i] - self.nizdiagonal[i] * self.betta[i - 1])
                                  / (self.nizdiagonal[i] * self.alfa[i - 1] + self.glavediagonal[i]))
                self.table.append([self.alfa[i], self.betta[i]])
        # вычисляет x
        for i in range((len(self.alfa)) - 1, -1, -1):
            if i == ((len(self.alfa)) - 1):
                self.x.append((self.b[i] - self.nizdiagonal[i] * self.betta[i - 1]) /
                              (self.nizdiagonal[i] * self.alfa[i - 1] + self.glavediagonal[i]))
            else:
                self.x.append(self.alfa[i] * self.x[len(self.x) - 1] + self.betta[i])
        self.x = list(reversed(self.x))
        for i in range(len(self.x)):
            self.table[i + 1].append(self.x[i])
        print(self.nizdiagonal,self.glavediagonal,self.verhdiagonal)

    def bags(self):
        # метод вычисляет вектор погрешностей
        x = 0
        for i in range(len(self.matrixX)):
            for j in range(len(self.matrixX[i])):
                x += self.x[j] * self.matrixX[i][j]
            self.nedovolnoeB.append(x)
            x = 0
        for i in range(len(self.nedovolnoeB)):
            self.pogreshnost.append(n(self.nedovolnoeB[i] - self.b[i]) / n(self.b[i]))
        for i in range(len(self.x)):
            self.table[i + 1].append(self.pogreshnost[i])
        print(tabulate(self.table, tablefmt='pipe', stralign='center',
                       headers='firstrow', floatfmt=('', '.3f', "")))


# задайте матрицу
a = [[9.64, 0.83,  0, 0, 0],
     [-0.193, -7.07, 0.684, 0, 0],
     [0, 0.203, 5.65, 0.53, 0],
     [0, 0, 0.354, 3.142, 0.094],
     [0, 0, 0, 0.86, 4.709]]
b = [1.885, 1.257, 2, 15, 9]
q = matrix(a, b)
q.algoritm()
q.bags()