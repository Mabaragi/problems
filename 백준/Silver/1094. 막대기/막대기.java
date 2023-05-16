import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int num = 64;
        int remainder = 0;
        int cnt = 1;
        while (num + remainder != N) {
            if (num + remainder > N) {
                num = num / 2;
            }
            if (num + remainder < N) {
                remainder += num;
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}