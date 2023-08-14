#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
    int N, M;
    cin >> N >> M;
    static long arr[1000001];
    for (int i = 1; i < N + 1; ++i) {
        long temp;
        cin >> temp;
        arr[i] = arr[i - 1] + temp;
    }

    static long arr2[1000];
    long result = 0;
    for (int i = 1; i < N + 1; ++i) {
        int remainder = arr[i] % M;
        if (remainder == 0) {
            result += 1;
        }
        arr2[remainder]++;
    } 

    for (int i = 0; i < M; ++i) {
        if (arr2[i] > 1) {
            result = result + (arr2[i] * (arr2[i] - 1) / 2);
        }
    }
    cout << result << '\n';
}
