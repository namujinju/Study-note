# [[1],[2,4],[3,6,9],[4,8,12,16],...] 리스트를 만들어라.

n = int(input())
array = []

for k in range(1, n+1):
    array.append([k * i for i in range(1,k+1)])

print(array)
