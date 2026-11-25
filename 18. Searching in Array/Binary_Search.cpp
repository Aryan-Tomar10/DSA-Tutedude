#include <iostream>
using namespace std;

struct Array{
    int A[10];
    int size;
    int Length;
};

void display(struct Array arr){
    int i;
    for(i=0;i<arr.Length;i++){
        cout<<arr.A[i]<<" ";
    }
    cout<<endl;
}

int Iterative_Binary_Search(struct Array arr,int Key){
    int l=0,r=arr.Length-1,mid;
    while(l<=r){
        mid=(l+r)/2;
        if(Key==arr.A[mid]){
            return mid;
        }
        else if(Key<arr.A[mid]){
            r=mid-1;
        }
        else{
            l=mid+1;
        }
    }
    return -1;
}

int Recursive_Binary_Search(struct Array arr,int Key,int l,int r){
    int mid=(l+r)/2;
    if(l<=r){
        if(Key==arr.A[mid]){
            return mid;
        }
        else if(Key<arr.A[mid]){
            return Recursive_Binary_Search(arr,Key,l,mid-1);
        }
        else{
            return Recursive_Binary_Search(arr,Key,mid+1,r);
        }
    }
    return -1;
}

int main() {
    struct Array arr1={{10,20,30,40,50},5,5};
    cout<<"Element found at index: "<<Iterative_Binary_Search(arr1,50)<<" through Iterative approach"<<endl;
    display(arr1);
    cout<<"Element found at index: "<<Recursive_Binary_Search(arr1,50,0,arr1.Length-1)<<" through Recursive approach"<<endl;
    display(arr1);
    return 0;
}