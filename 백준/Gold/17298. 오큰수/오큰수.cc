#include <iostream>
#include <vector>
#include <deque>

using namespace std;
typedef pair<int, int> Node;

deque<Node> stk;
int arr[1000000];
vector<int> answer(1000000, -1);

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    int N; cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }
    stk.emplace_back(arr[0], 0);
    for (int i = 1; i < N; ++i) {
        int val = arr[i]; // 현재 스택에 넣을 값
        while (!stk.empty() && stk.back().first < val){
            int idx = stk.back().second;
            stk.pop_back();
            answer[idx] = val;
        }
        stk.emplace_back(val, i);
    }
    for (int i = 0; i < N; ++i) {
        cout << answer[i] << ' ';
    }
}
