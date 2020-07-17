import sys
sys.stdin=open("input.txt",'r')
input=sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    docu = list(map(int, input().split())) #주어진 문서들의 중요도
    rank=[0 for _ in range(n)] #순서 체크할 리스트 따로 만들기
    rank[m] = 1 # m번쨰 문서인지 판단하기 위함 (추후 순서리스트 값이 1이면 m번째 문서로 판단)
    count = 0 # m번째 문서가 몇번째로 프린터 되는지 count (추후 m번째 문서 찾으면 count 출력 후 break)
    while True:
        if docu[0] == max(docu): #첫번째가 제일 중요한 것일 때
            count += 1
            if rank[0] == 1: #순서리스트에서 값이 1이면 구하고자 했던 m번째 문서
                print(count)
                break
            else: #중요도 가장 크지만 m번째 아님 -> 바로 출력하고 빼버리기
                docu.pop(0)
                rank.pop(0)

        else: #첫번째가 제일 중요한것이 아닐 때
            docu.append(docu.pop(0))
            rank.append(rank.pop(0))
            #문서리스트,순서리스트 둘다 맨 앞의 것을 빼서 맨 뒤로 보내줌