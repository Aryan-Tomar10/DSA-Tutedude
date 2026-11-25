#include <iostream>
using namespace std;

struct Array {
    int A[10];
    int size;
    int length;
};

void display(struct Array arr){
    cout<<"Elements are: ";
    for(int i=0; i<arr.length;i++){
        cout<<arr.A[i]<<" ";
    }
    cout<<endl;
}

void swap(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

int get(struct Array arr, int index){
    if(index>=0 && index<arr.length){
        return arr.A[index];
    }
    return -1;
}

void set(struct Array *arr,int index,int x){
    if(index>=0 && index<arr->length){
        arr->A[index] = x;
    }
}

int max(struct Array arr){
    int max = arr.A[0];
    for(int i=1;i<arr.length;i++){
        if(arr.A[i]>max){
            max = arr.A[i];
        }
    }
    return max;
}

int min(struct Array arr){
    int min = arr.A[0];
    for(int i=1;i<arr.length;i++){
        if(arr.A[i]<min){
            min = arr.A[i];
        }
    }
    return min;
}

int Average(struct Array arr){
    int sum = 0;
    for(int i=0;i<arr.length;i++){
        sum += arr.A[i];
    }
    return sum/arr.length;
}

int sum(struct Array arr){
    int sum = 0;
    for(int i=0;i<arr.length;i++){
        sum += arr.A[i];
    }
    return sum;
}

void reverse(struct Array *arr){
    int i,j;
    for(i=0,j=arr->length-1;i<j;i++,j--){
        swap(&arr->A[i], &arr->A[j]);
    }
}

int main() {
    struct Array arr;
    arr.size = 10;
    arr.length = 5;
    arr.A[0] = 10;
    arr.A[1] = 20;
    arr.A[2] = 30;
    arr.A[3] = 40;
    arr.A[4] = 50;
    display(arr);
    cout<<"Get element at index 2: "<<get(arr,2)<<endl;
    set(&arr,2,100);
    cout<<"After putting 100 at index 2: "<<get(arr,2)<<endl;
    cout<<"Max element: "<<max(arr)<<endl;
    cout<<"Min element: "<<min(arr)<<endl;
    cout<<"Average: "<<Average(arr)<<endl;
    cout<<"Sum: "<<sum(arr)<<endl;
    reverse(&arr);
    cout<<"After reversing: ";
    display(arr);
    return 0;
}