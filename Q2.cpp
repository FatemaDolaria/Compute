#include<bits/stdc++.h>

using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    
    sort (a.begin(), a.end());
    sort (b.begin(), b.end());
    for (int i=0; i<max(a.length(),b.length()); i++) {
        if (a[i] != b[i]) {
            if(a.length()>b.length()) {
                cout<< a[i] <<endl;
                break;
            }
       
            else {
                cout<< b[i] <<endl;
                break;
            }
        }
    }
    return 0;
}