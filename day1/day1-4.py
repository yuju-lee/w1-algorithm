# for문 2개 쓰기 싫어서...
# 한 문장의 총 글자수: n*2개
# 별의 개수는 첫줄에서부터 2개에서 시작해 배수로 올라가 n*2개까지 증가 후 배수로 감소
# 공백의 개수는 총 글자 수에서 별의 개수를 뺀 나머지
# for문 2개 쓰기 싫으니 i값으로 조건 걸어서 n+1번째 줄부터 else구문으로 빠지게 함
# else 구문에서는 별의 개수를 총 글자수에서 i+1값을 빼어 2개씩 빠지게 함
# 공백 count는 위와 같이 전체 줄에서 별의 개수를 뺀 값

n = int(input())
for i in range(0, n*2-1): #문제에서 제시한 조건 0~n*2-1번 순회
    if i < n: #0부터 n-1번 순회 (별 개수 증가)
        star = i+1 #회차별로 별 1개 증가
        space = n*2 - ((star)*2) #한 줄의 총 글자수 n*2 에서 별 갯수*2(양쪽이라 2개)를 뺀 나머지가 공백의 개수
        print("*"*(star)+" "*(space)+"*"*(star)) #양쪽에 별 넣기
    else: #n번부터 n*2-1까지 순회 (별 개수 감소)
        star = (n*2) - (i+1) #총 글자수에서 i+1만큼씩 감소 (2개씩 빠지니깐)
        space = (n*2) - ((star)*2) #한 줄의 총 글자수 n*2 에서 별 갯수*2(양쪽이라 2개)를 뺀 나머지가 공백의 개수
        print("*"*(star)+" "*(space)+"*"*(star))
        
# for문 2개 (위와 같은 로직)
# 이게 더 나을지도?
n = int(input())
for i in range(1,n+1):
    print("*"*i+" "*(2*(n-i))+"*"*i)
for j in range(1,n):
    print("*"*(n-j)+" "*(2*j)+"*"*(n-j))