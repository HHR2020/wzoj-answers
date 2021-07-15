N=int(input())
d={}
for _i in range(N):
    word=input()
    page=int(input())
    d[word]=page
M=int(input())
for _i in range(M):
    print(d[input()])