import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		int K = input.nextInt();
		
		int[] arr = new int[N];
		
		for (int i = 0; i < N; i++) {
			arr[i] = input.nextInt();
		}
		
		
		
		int count = 0;
		
		int start = 0;
		int end = K - 1;
		
		int[] satisfied = new int[N];
		
		
		for (int i = 0; i < N; i++) {
			if (arr[i] == 1) {
				satisfied[count++] = i;
			}
		}
		
		if (count - 1 < K) {
			System.out.println(-1);
		} else {
			int min = satisfied[end] - satisfied[start];
			end += 1;
			start += 1;
			
			while (true) {
				if (end == count) {
					break;
				}
				if (satisfied[end] - satisfied[start] < min) {
					min = satisfied[end] - satisfied[start];
				}
				end += 1;
				start += 1;
				}
				
			System.out.println(min + 1);
			}
			
			
		
		
		
		
		
		
		
		
		

	}

}