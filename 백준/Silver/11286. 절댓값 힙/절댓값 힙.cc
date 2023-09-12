#include <iostream>
#include <queue>

using namespace std;

struct compare {
    bool operator()(int o1, int o2) {
        int first_abs = abs(o1);
        int second_abs = abs(o2);
        if (first_abs == second_abs) {
            return o1 > o2;
        }
        else {
            return first_abs > second_abs;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    int N; cin >> N;
    priority_queue<int, vector<int> ,compare> my_queue;
    for (int i = 0; i < N; ++i) {
        int request; cin >> request;

        if (request == 0) {
            if (my_queue.empty()){
                cout << "0\n";
            }
            else{
                cout << my_queue.top() << '\n';
                my_queue.pop();
            }
        } else {
            my_queue.push(request);
        }
    }
}
