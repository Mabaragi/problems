#include <iostream>
#include <deque>

using namespace std;

long lst[5000001];
long answer[5000001];

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    int N, M; cin >> N >> M;
    for (int i = 0; i < N; ++i) {
        cin >> lst[i];
    }

    deque<long> qu_val; deque<int> qu_index;
    qu_val.push_back(lst[0]); qu_index.push_back(0);
    answer[0] = lst[0];

    for (int i = 1; i < N; ++i) {
        int first_index = qu_index.front();
        if (first_index <= i - M){
            qu_val.pop_front(); qu_index.pop_front();
        }
        long curr_val = lst[i];
        while (!qu_val.empty() && curr_val <= qu_val.back()) {
            qu_val.pop_back(); qu_index.pop_back();
        }
        qu_val.push_back(curr_val); qu_index.push_back(i);
        answer[i] = qu_val.front();
    }
    for (int i = 0; i < N; ++i) {
        cout << answer[i] << ' ';
    }
}
