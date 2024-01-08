import java.util.*;

public class walking {

	public static void main(String[] args) {
	
		Scanner stdin = new Scanner(System.in);
		int nC = stdin.nextInt();
		for (int loop=0; loop<nC; loop++) {
		
			int n = stdin.nextInt();
			int k = stdin.nextInt();
			char[][] grid = new char[n][];
			for (int i=0; i<n; i++)
				grid[i] = stdin.next().toCharArray();
				
			int[][][][] dp = new int[n][n][2][k+1];
			
			for (int i=0; i<n; i++) {
				if (grid[i][0] == 'H') break;
				dp[i][0][1][0] = 1;
			}

			for (int j=0; j<n; j++) {
				if (grid[0][j] == 'H') break;
				dp[0][j][0][0] = 1;
			}
		
			for (int i=1; i<n; i++) {
				for (int j=1; j<n; j++) {
			
					if (grid[i][j] == 'H') continue;
					
					for (int z=0; z<=k; z++)
						dp[i][j][0][z] += dp[i][j-1][0][z];
				
					for (int z=0; z<=k; z++)
						dp[i][j][1][z] += dp[i-1][j][1][z];
						
					for (int z=1; z<=k; z++)
						dp[i][j][0][z] += dp[i][j-1][1][z-1];

                    
					for (int z=1; z<=k; z++)
						dp[i][j][1][z] += dp[i-1][j][0][z-1];
				}
			}
			
			// Print the result.
			int res = 0;
			for (int dir=0; dir<2; dir++)
				for (int z=0; z<=k; z++)
					res += dp[n-1][n-1][dir][z];
			System.out.println(res);
		
		}
	}
}