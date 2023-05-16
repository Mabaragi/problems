import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] arr = new String[N];
        for (int i = 0; i < N; i++) {
            arr[i] = br.readLine();
        }

        Set<String> set = new HashSet<>(Arrays.asList(arr));

        String[] arr2 = set.toArray(new String[0]);

        Arrays.sort(arr2, new Comparator<String>() {
            @Override
            public int compare(String str1, String str2) {
                if (str1.length() != str2.length()) {
                    return Integer.compare(str1.length(), str2.length());
                } else {
                    return str1.compareTo(str2);
                }
            }
        });
        for (int i = 0; i < arr2.length; i++) {
            System.out.println(arr2[i]);
        }
    }
}