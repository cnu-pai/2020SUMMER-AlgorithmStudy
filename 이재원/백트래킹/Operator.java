package NandM;

import java.util.*;

public class Operator {

	static int n;
	static int[] arr;
	static int[] operator = new int[4];
	static int max= Integer.MIN_VALUE, min = Integer.MAX_VALUE;
	
	public static void main(String[] args) {


		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		arr = new int[n];
		
		for(int i =0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		
		for(int i=0; i<4; i++) {
			operator[i] = sc.nextInt();
		}
		
		solve(arr[0],1);
		System.out.println(max);
		System.out.println(min);
		
		
		
		

	}
	
	public static void solve(int num, int a) {
	
		if(a==n) {
		if(num > max) {
			max = num;
		}
		if(num <min) {
			min = num;
		}
		return;
	}
	
	int result = 0; 
	for(int i = 0; i<4;i++) {
		if(operator[i]!=0) {
			operator[i]--;
			
			switch(i) {
			case 0 : result = num+arr[a];
			break;
			
			case 1: result = num - arr[a];
			break;
			
			case 2 : result = num * arr[a];
			break;
			
			case 3 : 
			
				if(num <0 && arr[a]>0) {
					num*=-1;
					result = num / arr[a];
					result*=-1;
					
					break;
				}else {
					result = num / arr[a];
				
					break;
				}
				
			}
			solve(result,a+1);
			operator[i]++;
		}
	}
	}
}
