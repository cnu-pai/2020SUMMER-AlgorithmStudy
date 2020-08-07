package greedy;

import java.util.*;

public class Plumber {

	static int n, l;
	static int[] arr;
	static int count = 0;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		l = sc.nextInt();
		arr = new int[n];
		
		for(int i =0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr);
		
		solve(l);
		sc.close();
		
		System.out.println(count+1);

	}
	
	public static void solve(int L) {
		int a = arr[0] + l-1;
		for(int i =0; i<arr.length; i++) {
			if(arr[i]>a) {
				a = arr[i]+l-1;
				count++;
			}
		}
	}

}
