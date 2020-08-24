package MovePlan;

import java.util.*;

public class Podo_2156{
 
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] d = new int[10001][3];
        int[] a = new int[10001];
 
        for(int i=1; i<=n; i++){
            a[i]=sc.nextInt();    
        }
    
        d[1][0]=0;
        d[1][1]=a[1];
        d[1][2]=a[1];
        
        for(int i=2; i<=n ; i++){

            d[i][0] = Math.max(d[i-1][2], Math.max(d[i-1][1], d[i-1][0]));
            d[i][1] = d[i-1][0]+a[i];
            d[i][2] = d[i-1][1]+a[i];
        }
 
        System.out.println(Math.max( d[n][0], Math.max( d[n][1], d[n][2]) ));
        sc.close();
    }  
}
 
