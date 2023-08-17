#include <iostream>

using namespace std;

long stk[100000];
char answer[300000];

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    int N; cin >> N;
    int index = 1;
    int tail = 0; int counter = 2;
    int number; cin >> number;
    answer[0] = '+';
    stk[0] = 1;
    int answer_index = 1;
    while (index <= N && counter <= N + 1){
        if (stk[tail] == number){
            tail--;
            index++;
            answer[answer_index++] = '-';
            cin >> number;
        } else if (stk[tail] != number){
            stk[++tail] = counter++;
            answer[answer_index++] = '+';
        }
    }
    int minus_counter = 0;
    for (int i =  0; i <answer_index ; ++i) {
        if (answer[i] == '-'){
            minus_counter++;
        }
    }
    if (minus_counter == N){
        for (int i = 0; i < answer_index; ++i) {
            cout << answer[i] << '\n';
        }
    } else {
        cout <<  "NO";
    }
}
