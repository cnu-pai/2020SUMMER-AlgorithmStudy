package greedy;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int []arr = new int[n];
		long count = 0;
		
		for(int i =0; i<arr.length; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr);
		
		for(int i = 0; i<arr.length; i++) {
			count += Math.abs(arr[i]-(i+1));
		}
		
		System.out.println(count);
		sc.close();
		
	}

}
