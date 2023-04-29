import java.util.Scanner;

class Main {
  public static void main(String args[]) throws Exception {

    Scanner sc = new Scanner(System.in);
    int mx = 0;
    int order = 0;

    for (int i = 0; i < 9; i++) {
      int num = sc.nextInt();
      if (mx < num) {
        mx = num;
        order = i + 1;
      }
    }
    System.out.println(mx);
    System.out.println(order);
  }
}