import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("./input.txt"));
        // Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
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