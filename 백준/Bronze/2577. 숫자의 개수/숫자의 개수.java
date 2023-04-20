import java.util.*;
class Main
{
	public static void main(String args[]) throws Exception
	{
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    int c = sc.nextInt();
    String st = Integer.toString(a * b * c);
    int[] arr = new int[10];
    for (int i = 0; i < st.length(); i++) {
      int num = st.charAt(i) - '0';
      arr[num] += 1;
    }
    for (int i = 0; i < arr.length; i++) {
      System.out.println(arr[i]);
    }
}}