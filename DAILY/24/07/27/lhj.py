import sys
input = sys.stdin.readline

n=int(input())
num = list(map(int, input().split()))

# # trial 1 => 시간 오류
# result=-1000        # -1000 이상
# for i in range(n):
#     sum=0
#     for j in range(i,n):
#         sum+=num[j]
#         result = max(result, sum)
# print(result)

# trial 2 
# dp
dp=[0]*n        # 해당 idx까지 최대 합 저장
dp[0]=num[0]

for i in range(1,n):
    dp[i] = max(dp[i-1]+num[i], num[i])
print(max(dp))