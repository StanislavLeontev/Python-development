10class Matrix:
    def __init__(self,list):
        self.list = list

    def __str__(self):
        st = ''
        for i in self.list:
            st += f'{str(i)}\n'
        return st
    def __add__(self, other):
        new_list = []
        for i in range(len(self.list)):
            row = []
            for j in range(len(self.list[i])):
                row.append(self.list[i][j]+other.list[i][j])
            new_list.append(row)
        return new_list
matrix_1 = [[6,2,8,3],[7,1,2,5],[9,6,5,2]]
matrix_2 = [[2,5,8,9],[7,4,9,6],[1,4,7,8]]

a = Matrix(matrix_1)
b = Matrix(matrix_2)
c = Matrix(a + b)
print(a)
print(b)
print(c)