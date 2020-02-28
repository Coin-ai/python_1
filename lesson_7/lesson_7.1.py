'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.'''

import copy

class Matrix:
    def __init__(self,lists):
        self.matrix=lists
    def __str__(self):
        ma=len(str(max([max(ma) for ma in self.matrix])))
        mi=len(str(min(sum(self.matrix,[]))))
        ctn=(ma if ma>mi else mi)
        out=start='_'*((ctn+2)*len(self.matrix[0])+4)+'\n'
        for vals in self.matrix:
            out+='|  '
            for val in vals:
                out+=str(val)+(' '*(ctn+2-len(str(val))))
            out+='|\n'
        return out+'‾'*((ctn+2)*len(self.matrix[0])+4)
    def __add__(self,obj):
        mx=copy.deepcopy(self.matrix)
        if len(mx)!=len(obj.matrix):
            print('Error matrix size!')
            return
        for i in range(len(mx)):
            if len(mx[i])!=len(obj.matrix[i]):
                print('Error matrix size!')
                return
            for j in range(len(mx[i])):
                mx[i][j]+=obj.matrix[i][j]
            self.matrix=mx
        return self

matrix1=Matrix([[31,22,23],[37,43,-1],[5100,86,1]])
matrix2=Matrix([[3,5,32],[2,4,6],[-1300,64,-8]])
matrix3=Matrix([[3,5,8],[8,3,7],[3,7,1]])

print(matrix1)
print(matrix2)
print(matrix3)

matrix1+matrix2+matrix3
print(matrix1)

matrix4=Matrix([[3,5],[8,3],[3,7]])
matrix1+matrix4
print(matrix1)