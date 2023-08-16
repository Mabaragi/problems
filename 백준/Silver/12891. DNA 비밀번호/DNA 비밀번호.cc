#include <iostream>
#include <unordered_map>

using namespace std;

int checkArr(const int * arr, const int * arr2, const int * arr3, int d){
    for (int i = 0; i < 4; ++i) {
        if (arr[i] - arr2[i] < arr3[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    int N, M; cin >> N >> M;
    string str;

    cin.ignore();
    getline(cin, str);

    int check[4];
    for (int i = 0; i < 4; ++i) {
        cin >> check[i];
    }

    unordered_map<char, int> dct;
    dct['A'] = 0; dct['C'] = 1 ;dct['G'] = 2; dct['T'] = 3;
    static int arr[10000001][4];
    for (int i = 1; i < N + 1; ++i) {
        arr[i][dct[str[i-1]]]++;
        for (int j = 0; j < 4; ++j) {
            arr[i][j] += arr[i-1][j];
        }
    }
//    for (int i = 0; i < N + 1; ++i) {
//        for (int j = 0; j < 4; ++j) {
//            cout << arr[i][j] << ' ';
//        }
//        cout << '\n';
//    }

    int answer = 0;
    for (int i = 0; i < N + 1 - M; ++i) {
        if (checkArr(arr[i + M], arr[i], check, M)){
            answer++;
        }
    }
    cout << answer;
}
