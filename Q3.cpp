#include<bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin>>n;

    if (n==1) cout<<"-1"<<endl;

    else{
        vector<int>f;
        vector<int>::iterator itr;
        for (int i=1; i<=n; i++) {
            f.push_back(i);
        }
        sort (f.begin(), f.end(), greater<int>());
        f.pop_back();

        sort (f.begin(), f.end());
        f.push_back(1);
        
        for (int i=0; i<f.size(); i++) {
            cout<<f[i]<<" ";
        }
    }
    return 0;
}