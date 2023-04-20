import java.util.*;

class Main
{
	public static void main(String args[]) throws Exception
	{
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    int c = sc.nextInt();
    int[] arr = new int[10];
    int num = a * b * c;
    while (num > 0) {
      arr[num%10]++;
      num /= 10;
    }
    for (int i = 0; i < arr.length; i++) {
      System.out.println(arr[i]);
    }
}}