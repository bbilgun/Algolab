#include <iostream>
#include <vector>

using namespace std;

int countPrimes(int n) {
    if (n <= 1) return 0;

    vector<bool> isPrime(n, true);
    isPrime[0] = isPrime[1] = false;  

    for (int i = 2; i * i < n; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }
    }

    int count = 0;
    for (int i = 2; i < n; ++i) {
        if (isPrime[i]) {
            ++count;
        }
    }

    return count;
}

int main() {
    int n = 18;
    cout << "Анхны тоо нь: " << countPrimes(n) << endl;  // Output: 7
    return 0;
}
