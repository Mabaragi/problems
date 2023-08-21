#include <iostream>
#include <deque>

using namespace std;

deque<int> cards;

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    int N; cin >> N;
    for (int i = 0; i < N; ++i) {
        cards.push_back(i + 1);
    }
    int i = 0;
    while (cards.size() != 1){
        if (i % 2) { // 홀수 번째 때
            cards.push_back(cards.front());
        }
        cards.pop_front();
        i++;
    }
    cout << cards[0];
}
