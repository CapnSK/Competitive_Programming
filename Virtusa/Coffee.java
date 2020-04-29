import java.awt.Point;
import java.io.*;
import java.io.ObjectInputStream.GetField;
import java.util.*;
import java.util.logging.Level;

import javax.swing.text.MaskFormatter;

class Coffee {
    public static void main(String args[]) throws java.lang.Exception {

        Scanner sc=new Scanner(System.in);
        int t = sc.nextInt();
        while (t > 0) {
            t--;
            int n = sc.nextInt();
            int k = sc.nextInt();
            int d = sc.nextInt();
            int m = sc.nextInt();
            int[] A = new int[n + 1];
            for (int i = 1; i <= n; i++)
                A[i] = sc.nextInt();
            long[] sum = new long[n + 1];
            for (int i = 1; i <= n; i++)
                sum[i] = sum[i - 1] + A[i];
            long[][] dp = new long[n + 1][k + 1];
            int[][] index = new int[n + 1][k + 1];
            for (int i = 1; i <= n; i++) {

                dp[i][0] = sum[i];

                for (int j = 1; j <= Math.min(i, k); j++) {

                    for (int z = Math.max(j,
                            Math.max(index[i][j - 1], index[i - 1][j])); z <= i; z++) {

                        int range = Math.min(z + d, i);

                        long temp = dp[z - 1][j - 1] + (sum[range] - sum[z])
                                * m;
                        if (range != i)
                            temp += sum[i] - sum[range];

                        if (temp > dp[i][j]) {
                            dp[i][j] = temp;
                            index[i][j] = z;
                        }

                    }

                }
            }
            for(int i=0;i<=n;i++){
                for(int j=0;j<=k;j++){
                    System.out.print(dp[i][j]+" ");
                }
                System.out.println();
            }
            System.out.println(dp[n][k]);

        }
        sc.close();
    }
}