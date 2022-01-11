
#задача 1

def odd_nums(max_num):
    for i in range(1,max_num+1,2):
        yield i

n = int(input('сгенерировать последовательность до '))
odd_to_n = odd_nums(n)

for i in range(n):
    print(next(odd_to_n))


#задача 3

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

t_k = ((tutors[i],None) if i >= len(klasses)
       else (tutors[i],klasses[i])
       for i in range(len(tutors)))

print(type(t_k) , *t_k)


#задача 4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[i] for i in range(1,len(src)) if src[i] > src[i-1]]

print(*result)


#задача 5

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [src[i] for i in range(len(src)) if not src.count(src[i]) > 1]

print(result)




