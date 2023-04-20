import java.util.Scanner;
class Main
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
    String st = sc.nextLine().trim();
    String[] arr = st.split(" ");
    int ans = arr.length;
    if (st == "") {
      ans = 0;      
    } 
    System.out.println(ans);
	}
}