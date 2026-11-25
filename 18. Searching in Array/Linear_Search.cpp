#include <iostream>
using namespace std;

struct Array {
    int *A;
    int size;
    int length;
};

void display(struct Array arr) {
    cout << "Elements are: ";
    for (int i = 0; i < arr.length; i++) {
        cout << arr.A[i] << " ";
    }
    cout << endl;
}

void linearSearch(struct Array arr, int key) {
    for (int i = 0; i < arr.length; i++) {
        if (arr.A[i] == key) {
            cout << "Element found at index: " << i << endl;
            return;
        }
    }
    cout << "Element not found in the array." << endl;
}

int main() {
    struct Array arr;
    arr.size = 10;
    arr.length = 5;
    arr.A = new int[arr.size];
    arr.A[0] = 1;
    arr.A[1] = 2;
    arr.A[2] = 3;
    arr.A[3] = 4;
    arr.A[4] = 5;
    display(arr);
    linearSearch(arr, 2);
    delete[] arr.A;
    return 0;
}