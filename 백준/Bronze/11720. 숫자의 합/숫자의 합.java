import java.util.Scanner;

class Main {
  public static void main(String args[]) throws Exception {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    String nums = sc.next();
    String[] arr = nums.split("");
    int sum = 0;
    for (int i = 0; i < N; i++) {
      sum += Integer.parseInt(arr[i]);
    }
    System.out.println(sum);
  }
}