# https://www.acmicpc.net/problem/15990
# N은 10^5이하

# 뒤에 숫자가 중요. 뒤가 1을 더하는 경우 -1한 수의 2,3으로 끝나는 수, 2더하는경우 -2한수의 1,3으로 끝나는수, 3더하는경우도 마찬가지.
# index error가 뜨는데 왜 뜨는지 모르겠어요...
n = int(input())
inp = [int(input()) for _ in range(n)]
large = max(inp)

def sol(L):   #L은 가장 큰수
    ans = [[1,0,0],[0,1,0],[1,1,1]]
    MOD = 1000_000_009
    if L <= 3: return ans

    for i in range(3,L):       
        k = [0,0,0]
        k[0] = (ans[i-1][1] + ans[i-1][2]) % MOD
        k[1] = (ans[i-2][0] + ans[i-2][2]) % MOD
        k[2] = (ans[i-3][0] + ans[i-3][1]) % MOD
        ans.append(k)
    return ans

ans = sol(large)


for i in inp:
    print(sum(ans[i-1])% 1_000_000_009)