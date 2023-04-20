import java.util.*;
import java.io.FileInputStream;

class Main
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    String ans = "";
  
    for (int i = 0; i < N; i++) {
      for (int j = N - 1 - i; j > 0; j--) {
        ans += ' ';
      }
      for (int j = 0; j < i + 1; j++) {
        ans += '*';
      }
      if (i < N - 1) {
        ans += '\n';  
      }
    }
    System.out.println(ans);
}}