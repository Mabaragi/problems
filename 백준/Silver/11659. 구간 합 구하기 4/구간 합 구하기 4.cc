#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
    int N; int M;
    cin >> N; cin >> M;
    int arr[100000];
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }
    int sumArr[100001];
    sumArr[0] = 0;
    for (int i = 1; i < N + 1; i++)
    {
        sumArr[i] = sumArr[i - 1] + arr[i - 1];
    }
    for (int i = 0; i < M; i++)
    {
        int a; int b;
        cin >> a; cin >> b;

        cout << sumArr[b] - sumArr[a - 1] << '\n';
    }
    return 0;
}