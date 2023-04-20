import java.util.*;


class Main
{
	public static void main(String args[]) throws Exception
	{
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < N; i++) {
        for (int j = N - 1 - i; j > 0; j--) {
            sb.append(' ');
        }
        for (int j = 0; j < i + 1; j++) {
            sb.append('*');
        }
        if (i < N - 1) {
            sb.append('\n');
        }
    }
    System.out.println(sb);
}
}