#include <iostream>
using namespace std;

int main() {

    //method1
    int arr1[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    //method 2
    int arr2[3][4];
    arr2[0][0] = 1;
    arr2[0][1] = 2;
    arr2[0][2] = 3;
    arr2[0][3] = 4;
    arr2[1][0] = 5;
    arr2[1][1] = 6;
    arr2[1][2] = 7;
    arr2[1][3] = 8;
    arr2[2][0] = 9;
    arr2[2][1] = 10;
    arr2[2][2] = 11;
    arr2[2][3] = 12;

    //printing 2D array
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << arr1[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}