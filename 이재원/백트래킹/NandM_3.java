package NandM;

import java.util.*;
import java.io.*;

public class Three {

	static int n,m;
	static int[] arr;
	static StringBuilder sb;
	
	public static void main(String[] args) {


		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[n];
		sb = new StringBuilder();
	
		sort(0);
		System.out.print(sb.toString());
	
	}
	
	public static void sort(int a) {
		if(a == m) {
			for(int i =0; i<m; i++) {
				sb.append(arr[i]+" ");
			}
			sb.append("\n");
		}else {
			for(int i =1; i<=n; i++) {
				arr[a] = i;
				sort(a+1);
			}
		}
	
	}

}
