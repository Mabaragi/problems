#include <iostream>
#include <algorithm>
using namespace std;

void twoPoint(long target, int *answerPtr, const long *arr, int size, int i) {
    int start = 0, end = size - 1;

    while (start < end) {
        int val = arr[start] + arr[end];
        if (val == target) {
            if(start != i && end != i) {
                (*answerPtr)++;
                return;
            } else if (start == i) {
                start++;
            } else {
                end--;
            }
        } else if (val <= target) {
            start ++;
        } else {
            end --;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    int N; cin >> N;
    long arr[2000];

    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }
    sort(arr, arr + N);

    int answer = 0;
    for (int i = 0; i < N; ++i) {
        long target = arr[i];
        twoPoint(target, &answer, arr, N, i);
    }
    cout << answer;
}
