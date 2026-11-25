#include<iostream>
using namespace std;

int display(int n){
    if(n>0){
        return display(n-1)+n;
    }
    return 0;
}

int main(){
    int num = 10;
    cout<<display(num)<<endl;
}