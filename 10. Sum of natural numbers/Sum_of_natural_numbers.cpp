#include <iostream>
using namespace std;

int sum(int n){
    if(n==0){
        return 0;
    }
    else{
        return sum(n-1)+n;
    }
}

int main() {
    int n=5;
    cout<<"Using Recusrion the sum of first n natural numbers is: "<<sum(n)<<endl;
    int sum1=n*(n+1)/2;
    cout<<"Using Formula the sum of first n natural numbers is: "<<sum1;
    return 0;
}