cal[1501][1500]

def children_num(length, breadth):
    if(length == 0 or breadth == 0):
    	return 0
    fed = 1
    while(length != breadth and length != 0 and breadth != 0):
        fed++;
        if(length > breadth):
        	length -= breadth
        else:
        	breadth -= length
    return fed


for(int i = 1; i <= 1500; i++):
  for(int j = 1; j < i; j++):
      cal[i][j] = children_num(i, j)
      if(j != 1):
      	cal[i][j] += cal[i][j-1];

lmin = int(input())
lmax = int(input())
bmin = int(input())
bmax = int(input())
answer = 0

for i in range(bmin, bmax + 1):
  q1 = lmin/i
  q2 = lmax/i
  if(q1 == q2):
    answer += q1 * (lmax%i - lmin%i +1)
    answer += cal[i][lmax%i]
    if(lmin%i > 0):
      answer -= cal[i][lmin%i - 1]
  else if(q2 == q1 + 1):
    answer += q1 * (i - lmin%i)
    answer += cal[i][i-1]
    if(lmin%i != 0):
      answer -= cal[i][lmin%i - 1]
    answer += q2 * (lmax%i + 1)
    answer += cal[i][lmax%i]
  else:
    answer += q1 * (i - lmin%i)
    answer += cal[i][i-1]
    if(lmin%i != 0):
      answer -= cal[i][lmin%i - 1]
    answer += q2 * (lmax%i + 1)
    answer += cal[i][lmax%i]
    answer += i * (q2 - 1) * q2 / 2
    answer -= i * (q1 + 1) * q1 / 2
    answer += cal[i][i-1] * (q2 - 1 - q1)

print(answer)