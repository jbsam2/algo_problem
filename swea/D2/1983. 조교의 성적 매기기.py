t = int(input())

for tc in range(1,t+1):
    n, k = list(map(int,input().split()))
    scores = []
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(n):
        mid, fin, assign = map(int, input().split())
        score = 0.35*mid + 0.45*fin + assign*0.2
        scores.append(score)
    k_score = scores[k-1]
    scores.sort(reverse = True)
    rank_div = scores.index(k_score)//(n/10)
    k_grade = grades[int(rank_div)]
    print(f'#{tc} {k_grade}')