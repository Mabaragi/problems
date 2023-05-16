import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            String st = br.readLine();
            char start = st.charAt(0);
            int M = st.length();
            Set<Character> set = new HashSet<>();
            set.add(start);
            boolean found = true;
            for (int j = 0; j < M; j++) {
                if (st.charAt(j) != start) {
                    if (set.contains(st.charAt(j))) {
                        found = false;
                        break;
                    } else {
                        set.add(st.charAt(j));
                    }
                    start = st.charAt(j);
                }
            }
            if (found) {
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}