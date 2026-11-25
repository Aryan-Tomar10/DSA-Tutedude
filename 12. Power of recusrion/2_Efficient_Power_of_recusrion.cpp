#include <iostream>
using namespace std;

int pow(int m, int n){
    if (n==0){
        return 1;
    }
    if (n%2==0){
        return pow(m*m,n/2);
    }
    else{
        return pow(m*m,(n-1)/2)*m;
    }
}

int main() {
    int m=2;
    int n=5;
    cout<<pow(m,n);
    return 0;
}
