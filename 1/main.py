from tabulate import tabulate
from math import log, e, fabs


# 2-x=ln(x)
class bisekta:
    # метод бисекции
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n = 0
        self.c = (self.a + self.b) / 2
        self.fa = 2 - self.a - log(self.a, e)
        self.fb = 2 - self.b - log(self.b, e)
        self.fc = 2 - self.c - log(self.c, e)
        self.mod = fabs(self.a - self.b)
        self.table = [['N', 'a(n)', 'с(n)', 'b(n)', 'f(a(n))', 'f(b(n))', 'f(c(n))']]

    def algoritm(self):
        if round(self.c, 6) != 1.557146:
            if self.fc < 0:

                if self.fa < 0 <= self.fb:

                    self.a = self.c
                    self.fa = self.fc
                    self.mod = fabs(self.a - self.b)
                    self.n += 1
                    self.c = (self.a+self.b) / 2
                    self.fc = 2 - self.c - log(self.c, e)
                    self.table.append([self.n, self.a, self.c, self.b,
                                       self.fa, self.fb, self.fc])
                    bisekta.algoritm(self)

                elif self.fb < 0 <= self.fa:
                    self.b = self.c
                    self.fb = self.fc
                    self.mod = fabs(self.a - self.b)
                    self.n += 1
                    self.c = (self.a + self.b) / 2
                    self.fc = 2 - self.c - log(self.c, e)
                    self.table.append([self.n, self.a, self.c, self.b,
                                       self.fa, self.fb, self.fc])
                    bisekta.algoritm(self)
            elif self.fc > 0:

                if self.fa > 0 >= self.fb:
                    self.a = self.c
                    self.fa = self.fc
                    self.mod = fabs(self.a - self.b)
                    self.n += 1
                    self.c = (self.a + self.b) / 2
                    self.fc = 2 - self.c - log(self.c, e)
                    self.table.append([self.n, self.a, self.c, self.b,
                                       self.fa, self.fb, self.fc])
                    bisekta.algoritm(self)

                elif self.fb > 0 >= self.fa:
                    self.b = self.c
                    self.fb = self.fc
                    self.mod = fabs(self.a - self.b)
                    self.n += 1
                    self.c = (self.a + self.b) / 2
                    self.fc = 2 - self.c - log(self.c, e)
                    self.table.append([self.n, self.a, self.c, self.b,
                                       self.fa, self.fb, self.fc])
                    bisekta.algoritm(self)
        else:
            print(tabulate(self.table, tablefmt='pipe', stralign='center',
                           headers='firstrow', floatfmt=('', '.3f', "")))


class Nuton:
    # метод Ньютона
    def __init__(self, startx:  float,
                 endx: float, eps: float):
        self.nullx = startx
        self.nestx = endx
        self.eps = eps
        self.n = 0
        self.table = [['N', 'x', 'f(x)', 'Fp(x)', '|x(n)-x(n-1)|'],
                      [self.n, self.nullx, func(self.nullx),
                       - 1 * (self.nullx + 1) / self.nullx]]
    def algoritm(self):
        if fabs(self.nestx-self.nullx) < self.eps:
            x = self.nullx
            return print(tabulate(self.table, tablefmt='pipe', stralign='center',
                           headers='firstrow', floatfmt=('', '', "")))
        else:
            self.n += 1
            self.nestx, self.nullx = self.nullx - (2 - self.nullx - log(self.nullx)) /\
                                       (- 1 * ((self.nullx + 1) / self.nullx)), self.nestx
            self.table.append([self.n, self.nullx, func(self.nullx),
                               - 1 * (self.nullx + 1) / self.nullx])
            Nuton.algoritm(self)


class Xord:
    # метод Хорд
    def __init__(self, start, end, eps):
        self.start = start
        self.end = end
        self.startstart = self.start - func(self.start) *\
                          (self.end - self.start) /\
                          (func(self.end) - func(self.start))
        self.eps = eps
        self.n = 0
        self.table = [['N', 'X(n + 1)', 'x(n-1)', 'x(n)', 'f(x(n-1))', 'f(x(n))', '|x(n)-x(n-1)|'],
                      [self.n, self.startstart, self.start,
                       self.end, func(self.start),
                       func(self.end), fabs(self.end - self.start)]]
    def algoritm(self):
        if fabs(self.startstart - self.end) < self.eps:
            self.n += 1
            self.start = self.end
            self.end = self.startstart
            self.startstart = self.start - func(self.start) * \
                              (self.end - self.start) / \
                              (func(self.end) - func(self.start))

            self.table.append([self.n, self.startstart, self.start,
                               self.end, func(self.start),
                               func(self.end), fabs(self.end - self.start)])
            return print(tabulate(self.table, tablefmt='pipe', stralign='center',
                           headers='firstrow', floatfmt=('', '', '','')))
        else:
            self.n += 1
            self.start = self.end
            self.end = self.startstart
            self.startstart = self.start - func(self.start) *\
                          (self.end - self.start) /\
                          (func(self.end) - func(self.start))

            self.table.append([self.n, self.startstart, self.start,
                               self.end, func(self.start),
                               func(self.end), fabs(self.end - self.start)])
            Xord.algoritm(self)


class Dima:
    # метод простых итераци
    def __init__(self, ladno, eps):
        self.start = ladno
        self.next = Denis(self.start)
        self.eps = eps
        self.n = 0
        self.table = [['N', 'x(n-1)', 'x(n)', '|x(n-1)-x(n)|'],
                      [self.n, self.start, self.next, fabs(self.next - self.start)]]

    def algoritm(self):

        if fabs(self.next - self.start) < self.eps:
            self.n += 1
            self.start = self.next
            self.next = Denis(self.start)
            self.table.append([self.n, self.start, self.next, fabs(self.next - self.start)])
            return print(tabulate(self.table, tablefmt='pipe', stralign='center',
                           headers='firstrow', floatfmt=('', '.3f', "")))
        else:
            self.n += 1
            self.start = self.next
            self.next = Denis(self.start)
            self.table.append([self.n, self.start, self.next, fabs(self.next - self.start)])
            Dima.algoritm(self)


def func(qq):
    a = 2 - qq - log(qq)
    return a


def Denis(qq):
    a = 2 - log(qq)
    return a


bisekta(1.4, 1.6).algoritm()
(Nuton(1.5, 1.6, 0.00001).algoritm())
(Xord(1.4, 1.6, 0.00001).algoritm())
Dima(1.6,0.000001).algoritm()