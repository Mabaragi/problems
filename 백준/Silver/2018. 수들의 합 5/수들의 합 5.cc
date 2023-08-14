#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    int number; cin >> number;
    int answer = 0;

    for (int i = 1; (i + 1) * i / 2 <= number; ++i) {
        if (number % i == i * (i + 1) / 2 % i) {
            answer ++;
        }
    }
    cout << answer;
}