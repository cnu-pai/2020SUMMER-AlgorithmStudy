package greedy;

import java.util.*;

public class Matrix {

	static int n, m;
	static int [][] a;
	static int [][] b;
	
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int count = 0;
		 n = sc.nextInt();
		 m = sc.nextInt();
		
		a = new int [n][m];
		b = new int [n][m];
		
		for(int i = 0; i<n; i++) {
			String s = sc.next();
			for(int j =0; j<m; j++) {
				a[i][j] = s.charAt(j)-'0';
			}
		}
		for(int i =0; i<n; i++) {
			String s= sc.next();
			for(int j =0; j<m; j++) {
				b[i][j] = s.charAt(j)-'0';
			}
		}
		
		for(int i = 0; i<n-2; i++) {
			for(int j =0; j<m-2; j++) {
				if(a[i][j] != b[i][j]) {
					count++;
					change(a,i+1,j+1);
					
				}
			}
		}
		
		for( int i = 0; i<n; i++) {
			for(int j = 0; j<m; j++) {
				if(a[i][j] != b[i][j]) {
					System.out.println(-1);
					return;
				}
			}
		}
		
		System.out.println(count);

	}
	
	public static void change(int[][] a, int row, int col) {
		for(int i = row-1; i<=row+1; i++) {
			for( int j = col-1; j<=col+1; j++) {
				a[i][j] = 1-a[i][j];
			}
		}
	}
}
