#include <iostream>
using namespace std;

long factorial(long n){
    if (n==0){
        return 1;
    }
    else{
        return factorial(n-1)*n; 
    }
}

int main() {
    long n=65;
    cout<<"Factorial of "<<n<<" is "<<factorial(n)<<endl;
    return 0;
}