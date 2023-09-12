#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    int N; cin >> N;

    vector<pair<int, int>> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i].first; // 첫번째 값에 value
        arr[i].second = i;   // 두번째 값에 index
    }
    sort(arr.begin(), arr.end());

    int max = -1;
    for (int i = 0; i < N; ++i) {
        int val = arr[i].second - i;
        if (max < val){
            max = val;
        }
    }
    cout << max + 1;
}
