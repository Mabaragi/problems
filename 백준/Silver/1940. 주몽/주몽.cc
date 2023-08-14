#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    int N, M; cin >> N >> M;
    static int arr[10000000];
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }
    sort(arr, arr + N);

    int start = 0, end = N - 1, answer = 0;

    while (start < end) {
        int val = arr[start] + arr[end];
        if (val == M) {
            answer++;
            end--;
        } else if (val < M) {
            start++;
        } else {
            end--;
        }
    }
    cout << answer << '\n';
}
