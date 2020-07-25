package greedy;

import java.util.*;

public class Emplo {

	public static void main(String[] args) {


		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for(int i = 0; i<n; i++) {
			int x = sc.nextInt();
			int[] none = new int [x+1];
			for(int j =0 ; j<x; j++) {
				none[sc.nextInt()] = sc.nextInt(); 
			}
			
			int count = 1;
			int interview = none[1];
			
			for(int k = 2; k<=x; k++) {
				if(interview >= none[k]) {
					interview = none[k];
					count++;
				}
			}
			
			System.out.println(count);
		}
		sc.close();

	}

}
