package NandM;

import java.util.*;

public class one {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int[] a = new int[m];
		
		sc.close();
		
		dfs(a,0,n);
		
	}
	
	public static boolean judge(int a[], int x, int y) {
		for(int i = 0; i<y; i++) {
			if(a[i] == x) {
				return true;
			}
		}
		return false;
	}

	
	public static void dfs(int a[], int i, int n) {
		if (a.length == i) {
			for(int j =0; j< a.length; j++) {
				System.out.print(a[j]+" ");
			}
			System.out.println(" ");
		}
		else {
			for(int j =1; j<n; j++) {
				if(!judge(a,j,i)) {
					a[i] = j;
					dfs(a,i+1,n);
				}
				
				
			}
		}
	}
}
