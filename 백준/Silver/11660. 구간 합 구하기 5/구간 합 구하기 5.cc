#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

//    N, M 입력
    int N, M;
    cin >> N, cin >> M;

//    N * N 배열 입력
    vector<vector<int>> arr(N + 1, vector<int>(N + 1, 0));

    for (int i = 1; i < N + 1; ++i) {
        for (int j = 1; j < N + 1; ++j) {
            cin >> arr[i][j];
            arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1];
        }
    }

    for (int i = 0; i < M; ++i) {
        int x1, y1, x2, y2;
        cin >> x1, cin>> y1, cin>> x2, cin>> y2;
        cout << arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1] << '\n';
    }
}
