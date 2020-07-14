// 문제번호 1026 보물

import java.util.*;

public class Main {
	public static void main(String args[]) {
		Scanner input = new Scanner(System.in);
		int N = input.nextInt();
		int[] A = new int[N];
		int[] B = new int[N];
		
		for (int i = 0; i < N; i++) {
			A[i] = input.nextInt();
		}
		for (int i = 0; i < N; i++) {
			B[i] = input.nextInt();
		}
		
		Arrays.sort(A);
		Arrays.sort(B);
		
		int answer = 0;
		for (int i = 0; i < N; i++) {
			answer += A[i] * B[N - i - 1];
		}
		
		System.out.println(answer);
	}
}
