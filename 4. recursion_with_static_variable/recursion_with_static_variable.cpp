#include<iostream>
using namespace std;

int display(int n){
    static int x=0;
    if(n>0){
        x++;
        return display(n-1)+x;
    }
    return 0;
}

int main(){
    int num = 5;
    cout<<display(num)<<endl;
}