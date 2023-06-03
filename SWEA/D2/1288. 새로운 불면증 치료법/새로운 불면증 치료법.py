
import java.lang.reflect.Array;
import java.util.*;

class Solution {
  public static void main(String args[]) throws Exception {



    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();

    for (int test_case = 1; test_case < T + 1; test_case++) {
      int num = sc.nextInt();
      boolean visit[] = new boolean[10];
      int cnt = 0;
      int n = 0;
      while (cnt < 10) {
        n++;
        String stringNum = Integer.toString(num * n);
        for (int i = 0; i < stringNum.length(); i++) {
          int numStringNum = Character.getNumericValue(stringNum.charAt(i));
          if (!visit[numStringNum]) {
            cnt += 1;
            visit[numStringNum] = true;

          }
        }
      }
      System.out.println("#" + test_case + " " + n * num);
    }
  }
}