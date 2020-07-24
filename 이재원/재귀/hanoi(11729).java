package reculsive;

import java.util.*;

public class hanoi {

	static int n, count =0;
	static StringBuilder s = new StringBuilder();
	
	public static void main(String[] args) {
	
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		tower(n,1,2,3);
		System.out.println(count);
		System.out.println(s);

	}
	
	static void tower(int n, int one, int two, int three) {
		count++;
		if( n ==1) {
			s.append(one + " " +three+"\n");
			return;
		}
		else {
			tower(n-1,one,three,two);
			s.append(one+" "+three+"\n");
			tower(n-1,two,one,three);
		}
	}
	


}
