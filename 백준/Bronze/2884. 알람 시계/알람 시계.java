import java.util.Scanner;

class Main
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    int min = a * 60 + b - 45;
    if (min < 0) {
      min += 1440;
    }
    int h = min / 60;
    int m = min % 60;
    System.out.println(h + " " +  m);
	}
}