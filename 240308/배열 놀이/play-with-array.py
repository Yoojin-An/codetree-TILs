n, q = map(int, input().split())

elements = list(map(int, input().split()))
queries = []
for i in range(q):
    queries.append(input())
for query in queries:
    clues = "".join(query.split(" "))
    classification = int(clues[0])
    a = int(clues[1])
    
    if classification == 1:
    # a번째 원소 출력
        print(elements[a - 1])
    
    
    elif classification == 2: 
    # 숫자 a가 있는지 판단해서 있다면 몇 번째 원소인지 출력
    # 있는데 2개 이상 있다면 더 작은 인덱스를 가지는 원소 출력
    # 없다면 0 출력
        if a in elements:
            print(elements.index(a) + 1)
        else:
            print(0)
    
    
    else:
        b = int(clues[2])
    # a번째 원소부터 b번째 원소까지 순서대로 공백을 사이에 두고 출력
        answer = elements[a-1:b]
        for i in answer:
            print(i, end=" ")