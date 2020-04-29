#include "bits/stdc++.h"
using namespace std;

long long prefix_sums[1001][1000];

long long number_of_children_fed(long long length, long long breadth)
{
    if(length == 0 || breadth == 0)
    return 0;
    long long fed = 1;
    while(length != breadth && length != 0 && breadth != 0)
    {
        fed++;
        if(length > breadth)
        length -= breadth;
        else
        breadth -= length;
    }
    return fed;
}

int main()
{
    for(int i = 1; i <= 1000; i++)
    for(int j = 1; j < i; j++)
    {
        prefix_sums[i][j] = number_of_children_fed(i, j);
        if(j != 1)
        prefix_sums[i][j] += prefix_sums[i][j-1];
    }
    
    int T;
    cin >> T;
    
    while(T--)
    {
        long long N, M, P, Q;
        cin >> N >> M >> P >> Q;
    
        long long answer = 0;
        
        for(long long i = P; i <= Q; i++)
        {
            long long q1 = N/i;
            long long q2 = M/i;
            if(q1 == q2)
            {
                answer += q1 * (M%i - N%i +1);
                answer += prefix_sums[i][M%i];
                if(N%i > 0)
                answer -= prefix_sums[i][N%i - 1];
            }
            else if(q2 == q1 + 1)
            {
                answer += q1 * (i - N%i);
                answer += prefix_sums[i][i-1];
                if(N%i != 0)
                answer -= prefix_sums[i][N%i - 1];
                answer += q2 * (M%i + 1);
                answer += prefix_sums[i][M%i];
            }
            else
            { 
                answer += q1 * (i - N%i);
                answer += prefix_sums[i][i-1];
                if(N%i != 0)
                answer -= prefix_sums[i][N%i - 1];
                answer += q2 * (M%i + 1);
                answer += prefix_sums[i][M%i];
                answer += i * (q2 - 1) * q2 / 2; 
                answer -= i * (q1 + 1) * q1 / 2;
                answer += prefix_sums[i][i-1] * (q2 - 1 - q1);
            }
        }
        cout << answer << endl;
    }
    return 0;
}