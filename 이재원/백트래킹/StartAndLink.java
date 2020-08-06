package NandM;

import java.util.*;

public class StartAndLink {

	static int n;
	static int[][] all;
	static int[] team1,team2;
	static int min = Integer.MAX_VALUE;
	
	public static void main(String[] args) {


		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		all = new int[n][n];
		team1 = new int [n/2];
		team2 = new int [n/2];
		
		for(int i =0; i<all.length; i++) {
			for(int j =0; j<all.length; j++) {
				all[i][j] =sc.nextInt(); 
						}
		}
		
		dfs(0);
		System.out.print(min);
	

	}
	public static void dfs(int count) {
		if(count == all.length/2) {
			for(int i=0,j=0,k=0;i<all.length;i++) {
				if(j<all.length/2 && team1[j]==i) {
					j++; 
					continue;
				}
				if(k<all.length/2)
					team2[k++] = i;
			}
			
			int team1Sum =0, team2Sum =0;
			for(int i =0; i<team1.length; i++) {
				for(int j =0; j<team2.length; j++) {
					if(i!=j) {
						team1Sum += all[team1[i]][team1[j]];
						team2Sum += all[team2[i]][team2[j]];
					}
				}
			}
			
			min = Math.min(min, Math.abs(team1Sum-team2Sum));
			return;
		}
		
		for(int i =0; i<all.length; i++) {
			if(count != 0 && team1[count-1]>=i)
				continue;
			team1[count] = i;
			dfs(count+1);
		}
	}

}
