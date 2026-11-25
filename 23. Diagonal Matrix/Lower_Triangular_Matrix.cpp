#include <iostream>
using namespace std;

class LTMatrix{
    private:
        int *A; //Array to store non-zero elements of the lower triangular matrix
        int n;  //Size of the matrix
    public:
        //Constructor to initialize the matrix
        LTMatrix(int n){
            this->n = n;
            A = new int[n*(n+1)/2];
        }
        
        //Destructor deallocate memory
        ~LTMatrix(){ 
            delete []A;
        }
        void Display(bool row=true);
        void setRowMajor(int i, int j, int x);
        void setColMajor(int i, int j, int x);
        int getRowMajor(int i, int j);
        int getColMajor(int i, int j);
        int getN(){  //Return size of matrix 
            return n; 
        }
};

void LTMatrix::setRowMajor(int i, int j, int x){
    if(i >= j){
        int index =i*(i-1)/2 + j-1;
        A[index] = x;
    }
}

void LTMatrix::setColMajor(int i, int j, int x){
    if (i>=j){
        int index = (n*(j-1)-(((j-2)*(j-1))/2))+(i-j);
        A[index] = x;
    }
}

int LTMatrix::getRowMajor(int i, int j){
    if(i>=j){
        int index = ((i*(i-1))/2)+j-1;
        return A[index];
    }else{
        return 0;
    }
}

int LTMatrix::getColMajor(int i, int j){
    if(i>=j){
        int index = (n*(j-1)-(((j-2)*(j-1))/2))+(i-j);
        return A[index];
    }else{
        return 0;
    }
}

void LTMatrix::Display(bool row){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(i>=j){
                if(row){
                    cout << getRowMajor(i, j) << " ";
                }else{
                    cout << getColMajor(i, j) << " ";
                }
            }else{
                cout<<0<<" ";
            }
        }
        cout<<endl;
    }
}

int main() { 
    LTMatrix rm(4);
    rm.setRowMajor(1,1,0);
    rm.setRowMajor(2,2,9);
    rm.setRowMajor(2,3,8);
    rm.setRowMajor(3,4,7);
    rm.setRowMajor(3,5,6);
    rm.setRowMajor(3,6,5);
    rm.setRowMajor(4,7,4);
    rm.setRowMajor(4,8,3);
    rm.setRowMajor(4,9,2);

    rm.Display();
    cout<<endl;

    LTMatrix cm(4);
    cm.setColMajor(1,1,0);
    cm.setColMajor(2,2,9);
    cm.setColMajor(2,3,8);
    cm.setColMajor(3,5,7);
    cm.setColMajor(3,5,6);
    cm.setColMajor(3,6,5);
    cm.setColMajor(4,7,4);
    cm.setColMajor(4,8,3);
    cm.setColMajor(4,9,2);

    cm.Display(false);



    return 0;
}