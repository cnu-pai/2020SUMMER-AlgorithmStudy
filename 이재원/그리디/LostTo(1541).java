package greedy;

import java.util.*;

public class LostTo {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String input = sc.next();
		
		String[] a = input.split("\\-");
		
		int sum = 0;
		
		for(int i = 0; i<a.length; i++) {
			String[] b = a[i].split("\\+");
			for(int j = 0; j<b.length;j++) {
				if( i ==0 && input.charAt(0)!='-') {
					sum += Integer.parseInt(b[j]);
				}else {
					sum -= Integer.parseInt(b[j]);
				}
			}
		}
		System.out.println(sum);
		sc.close();
		
		

	}

}
