package NandM;

import java.util.*;

public class Four {

	static int n, m;
	static int[] arr;
	static StringBuilder sb;
	
	public static void main(String[] args) {


		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[n];
		sb = new StringBuilder();
		
		sc.close();
		sort(1,0);
		
		System.out.print(sb.toString());
		
	}
	
	public static void sort(int a, int b) {
		if ( b == m) {
			for(int i = 0; i<m; i++) {
				sb.append(arr[i]+" ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i = a; i<=n; i++) {
			arr[b] = i;
			sort(i,b+1);
		}
	}

}
