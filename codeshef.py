t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    if n<k:
        print(-1)
    else:
        a = [i for i in list(map(int, input().split()))]
        b = [i for i in list(map(int, input().split()))]
        ab = [(a[i], b[i]) for i in range(n)]
        ab = sorted(ab, key=lambda x:x[0])
        ab = sorted(ab, key=lambda x:x[1])
        cats = set(a)
        # print(ab)
        # print(cats)
        time = 0
        for i in range(k):
            ofun = []
            for i in cats:
                for j in range(n):
                    if ab[j][1] == i:
                        ofun.append(ab[j][1])
                        break
            time += ofun[0]
        print(time)
