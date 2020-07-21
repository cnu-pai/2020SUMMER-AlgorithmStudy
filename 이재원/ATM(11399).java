package study01;

import java.util.*;

public class ATM {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		int[] arr = new int[n];
		int count = 0;
		int result = 0;
		
		for(int i = 0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr);
		for(int j = 0; j<n; j++) {
			count += arr[j];
			result += count;
		}
		
		System.out.println(result);
	}

}
