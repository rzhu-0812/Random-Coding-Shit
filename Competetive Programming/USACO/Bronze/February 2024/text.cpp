#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    
    while (T--) {
        string S;
        cin >> S;
        
        if (S.back() == '0') {
            cout << "E" << endl;
        } else {
            cout << "B" << endl;
        }
    }
    
    return 0;
}
