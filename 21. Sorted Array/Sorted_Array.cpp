#include <iostream>
using namespace std;

struct Array{
    int A[10];
    int size;
    int length;
};

void display(struct Array arr){
    for(int i=0; i<arr.length;i++){
        cout<<arr.A[i]<<" ";
    }
}

bool check(struct Array arr){
    for (int i=1;i<arr.length;i++){
        if (arr.A[i-1]>arr.A[i]){
            return false;
        }
    }
    return true;
}

int main() {
    struct Array arr={{1,2,3,6,5},10,5};
    if(check(arr)){
        cout<<"The array is sorted";
    }
    else{
        cout<<"The array is not sorted";
    }
    return 0;
}