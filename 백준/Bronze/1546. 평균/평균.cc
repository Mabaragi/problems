#include <iostream>;
using namespace std;

int main() 
{    
    int N;
    cin >> N;
    int A[1000];
    
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    
    long sum = 0;
    long max = 0;

    for (int i = 0; i < N; i++)
    {   
        sum += A[i];
        if (max < A[i]) {
            max = A[i];
        }
    }
    double result = sum * 100.0 / max / N;

    cout << result;
    return 0;
}