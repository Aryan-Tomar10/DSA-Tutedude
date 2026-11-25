#include<iostream>
using namespace std;

void display(int n){
    if(n>0){
        display(n-1);
        cout<<n<<endl;
    }
}

int main(){
    int num = 3;
    display(num);
}