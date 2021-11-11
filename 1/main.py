from tabulate import tabulate
from math import log, e, fabs


# 2-x=ln(x)
class bisekta:
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
    def __init__(self, startx:  float,
                 endx: float, eps: float):
        self.nullx = startx
        self.nestx = endx
        self.eps = eps
        self.n = 0
    def algoritm(self):
        if fabs(self.nestx-self.nullx) < self.eps:
            x = self.nullx
            return print(self.nullx)
        else:
            print(self.nullx,self.nestx)
            self.nestx, self.nullx = self.nullx - (2 - self.nullx - log(self.nullx)) /\
                                       (- 1 * ((self.nullx + 1) / self.nullx)), self.nestx
            print(self.nullx, self.nestx)
            Nuton.algoritm(self)

class Xord:
    def __init__(self, start, end, eps):
        self.start = start
        self.end = end
        self.startstart = self.start - func(self.start) *\
                          (self.end - self.start) /\
                          (func(self.end) - func(self.start))

        self.eps = eps
        self.n = 0
    def algoritm(self):
        if fabs(self.startstart - self.end) < self.eps:
            return print(self.start,self.startstart,self.end)
        else:
            self.start = self.end
            self.end = self.startstart
            self.startstart = self.start - func(self.start) *\
                          (self.end - self.start) /\
                          (func(self.end) - func(self.start))

            print(self.start, self.startstart, self.end)
            Xord.algoritm(self)
class Dima:
    def __init__(self,ladno,eps):
        self.start = ladno
        self.next = Denis(self.start)
        self.eps = eps
        self.n = 0
    def algoritm(self):
        if fabs(self.next - self.start) < self.eps:
            return print(self.start,self.next)
        else:
            self.start = self.next
            self.next = Denis(self.start)
            Dima.algoritm(self)


def func(qq):
    a = 2 - qq - log(qq)
    return a
def Denis(qq):
    a = 2 - log(qq)
    return a
bisekta(1.4, 1.6).algoritm()
#(Nuton(1.4, 1.6, 0.00001).algoritm())
#(Xord(1.4, 1.6, 0.00001).algoritm())
Dima(1.5,0.0001).algoritm()