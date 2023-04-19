import java.util.Scanner;

class Main {
  public static void main(String args[]) throws Exception {
      
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    sc.nextLine();

    String nums = sc.nextLine();
    String arr[] = nums.split(" ");
    double sum = 0;
    double max = 0;
    for (int i = 0; i < N; i++) {
      float num = Float.parseFloat(arr[i]);
      sum += num;
      if (max < num) {
        max = num;
      }
    }
    System.out.println(sum / N * 100 / max);
  }
}