package PriorityQueue;

import java.util.Scanner;

public class Main {

	static int n;
	static int[] arr;
	static int size = 0;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		arr = new int[n];
		
		for(int i =0 ; i<n; i++) {
			int a= sc.nextInt();
			
			if (a == 0) {
				pop();
			}
			else {
				push(a);
			}
		}
		sc.close();

	}
	
	static void push(int a) {
		int index = size;
		arr[size++] = a;
		while(true) {
			int p = (index-1)/2;
			if(arr[p]<arr[index]) {
				int temp = arr[p];
				arr[p] = arr[index];
				arr[index] = temp;
				index = p;
			}
			else {
				break;
			}
		}
	}
	
	static void pop() {
		if(size ==0) {
			System.out.println("0");
		}
		else {
			System.out.println(arr[0]);
			arr[0] = arr[size-1];
			size--;
		}
		int idx = 0;
		while(true) {
			int Max = idx;
			
			if((idx+(idx+1)<size) && (arr[idx+(idx+1)]>arr[Max]))
				Max = idx+(idx+1);
		
		
			if((idx+(idx+2)) <size&& (arr[idx+(idx+2)] > arr[Max]))
					Max = idx +(idx+2);
			
			if(Max == idx)
				break;
			
			else {
				int tmp = arr[Max];
				arr[Max] = arr[idx];
				arr[idx] = tmp;
				idx = Max;
			}
		}
		
		
		
		
	}

}


