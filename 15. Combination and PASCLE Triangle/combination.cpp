#include <iostream>
using namespace std;

int fact(int n){
    if(n==0 || n==1){
        return 1;
    }
    return n*fact(n-1);
}

int c(int n,int r){
    int a,b,c;
    a=fact(n);
    b=fact(r);
    c=fact(n-r);
    return a/(b*c);
}

int main() {
    cout<<c(5,2);
    return 0;
}