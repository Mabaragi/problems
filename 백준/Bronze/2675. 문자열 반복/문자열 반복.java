import java.util.Scanner;

class Main {
  public static void main(String args[]) throws Exception {

    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();

    for (int tc = 0; tc < T; tc++) {
      int num = sc.nextInt();
      String st = sc.nextLine().strip();
      String ans = "";
      for (int i = 0; i < st.length(); i++) {
        for (int j = 0; j < num; j++) {
          ans += st.charAt(i);
        }
      }
      System.out.println(ans);
    }
  }
}