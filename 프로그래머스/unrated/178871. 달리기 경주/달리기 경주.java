import java.util.HashMap;

class Solution {
    public static String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> dct = new HashMap<String, Integer>();
        for (int i = 0; i < players.length; i++) {
            dct.put(players[i], i);
        }

        for (String calling : callings) {
            int currentIndex = dct.get(calling);
            int desiredIndex = currentIndex - 1;
            String temp = players[currentIndex];
            players[currentIndex] = players[desiredIndex];
            players[desiredIndex] = temp;
            dct.put(players[currentIndex], currentIndex);
            dct.put(players[desiredIndex], desiredIndex);
        }
        return players;
    }
}