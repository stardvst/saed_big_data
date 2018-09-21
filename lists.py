print("x = ", end='')
x = int(input())
if x & 1:
    print("odd")
else:
    print("even")

lst = []
print("lst size: ", len(lst))

lst = [1, "2", "text", 6]
print("new list: ", lst)

print("Enter n: ", end='')
n = int(input())
lst = []
for idx in range(n):
    print("Enter x: ", end='')
    lst.append(int(input()))

lst_sq = [x**2 for x in lst]
for el in lst_sq:
    print("New el: ", el)

L = [[1, 2], [3, 4], [5, 6]]
for i, j in L:
    print(i, j)