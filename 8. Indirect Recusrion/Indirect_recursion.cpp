#include<iostream>
using namespace std;

//Function Prototyping
void B(int);
void A(int);

void A(int n){
    if(n>0){
        cout<<n<<" ";
        B(n-1);
    }
}

void B(int n){
    if(n>0){
        cout<<n<<" ";
        A(n/2);
    }
}

int main(){
    A(20);
}