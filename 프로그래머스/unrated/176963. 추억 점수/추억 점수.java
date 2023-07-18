import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photos) {
        int N = name.length;
        int M = photos.length;
        HashMap<String, Integer> dct = new HashMap<>();
        
        for (int i = 0; i < N; i++) {
            dct.put(name[i], i);
        }
        
        int[] answer = new int[M];
        for (int i = 0; i < M; i ++) {
            for (String photoName : photos[i]) {
                if (dct.get(photoName) != null) {
                    answer[i] += yearning[dct.get(photoName)];    
                }                
            }
        }
        return answer;
    }
}