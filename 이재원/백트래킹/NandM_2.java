package NandM;

import java.util.*;

public class Two {

	public static int n, m;
	public static int[] arr;
	public static boolean[] visit;
	
	public static void main(String[] args) {
		
		
		
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[m];
		visit = new boolean[n+1];
		
		dfs(1,0);
	}
	
	public static void dfs(int a, int b) {
		if( b == m) {
			for(int i =0; i<arr.length; i++) {
				System.out.print(arr[i]+" ");
			}
			System.out.println("");
			return;
		}
		
		for(int i = a; i<=n; i++) {
			if(visit[i])
				continue;
			
			visit[i] = true;
			arr[b] = i;
			dfs(i,b+1);
			visit[i] = false;
		}
	}

}
