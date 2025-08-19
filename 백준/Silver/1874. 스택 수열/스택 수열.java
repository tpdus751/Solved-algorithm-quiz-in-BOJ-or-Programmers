import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int N = input.nextInt();
		
		Stack<Integer> stack = new Stack<>();
		
		int now = 1;
		
		boolean possible = true;
		
		for (int i = 0; i < N; i++) {
			int num = input.nextInt();
			
			while (now <= num) {
				stack.push(now++);
				sb.append("+\n");
			}
			if (stack.peek() == num) {
				stack.pop();
				sb.append("-\n");
			} else {
				possible = false;
				break;
			}
		}
		
		if (!possible) {
			System.out.println("NO\n");
		} else {
			System.out.println(sb.toString());
		}
		
	}

}