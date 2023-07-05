import java.util.*;
import java.io.*;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");

    // st = new StringTokenizer(br.readLine(), " ");
    int T = Integer.parseInt(st.nextToken());
    for (int tc = 0; tc < T; tc++) {
      st = new StringTokenizer(br.readLine(), " ");
      int N, M, K;
      N = Integer.parseInt(st.nextToken());
      M = Integer.parseInt(st.nextToken());
      K = Integer.parseInt(st.nextToken());

      int[][] array = new int[N][M];
      boolean[][] visit = new boolean[N][M];
      for (int i = 0; i < K; i++) {
        st = new StringTokenizer(br.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        array[a][b] = 1;
      }

      int[] dx = { 1, -1, 0, 0 };
      int[] dy = { 0, 0, 1, -1 };
      int cnt = 0;

      for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
          if (array[i][j] == 1 && !visit[i][j]) {
            cnt++;
            Queue<int[]> queue = new ArrayDeque<>();
            int[] arr = { i, j };
            queue.add(arr);
            while (!queue.isEmpty()) {
              int[] numbers = queue.remove();
              int ci = numbers[0];
              int cj = numbers[1];

              for (int l = 0; l < 4; l++) {
                int ni = ci + dx[l];
                int nj = cj + dy[l];

                if (0 <= ni && ni < N && 0 <= nj && nj < M && !visit[ni][nj] && array[ni][nj] == 1) {
                  int[] nextArray = { ni, nj };
                  queue.add(nextArray);
                  visit[ni][nj] = true;
                }
              }
            }
          }
        }
      }
      System.out.println(cnt);
    }
  }
}
