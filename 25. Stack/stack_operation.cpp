#include<iostream>
using namespace std;

class Stack{
    private:
        int size;
        int top;
        int *s;
    public:
        Stack(int size);
        ~Stack();
        void push(int x);
        int pop();
        int peek(int index);
        bool isFull();
        bool isEmpty();
        void display();
        int stackTop();
};

Stack::Stack(int size){
    this->size = size;
    top = -1;
    s = new int[size];
}

Stack::~Stack(){
    delete []s;
}

void Stack::push(int x){
    if(isFull()){
        cout<<"Stack Overflow"<<endl;
    }
    else{
        top++;
        s[top] = x;
    }
}

int Stack::pop(){
    int x = 1;
    if(isEmpty()){
        cout<<"Stack Underflow"<<endl;
    }
    else{
        x = s[top];
        top--;
    }
    return x;
}

int Stack::peek(int index){
    int x = -1;
    if(top-index+1 < 0 || top-index+1 == size){
        cout<<"Stack Underflow"<<endl;
    }
    else{
        x = s[top-index+1];
    }
    return x;
}

bool Stack::isFull(){
    if(top == size-1){
        return true;
    }
    return false;
}

bool Stack::isEmpty(){
    if(top == -1){
        return true;
    }
    return false;
}

void Stack::display(){
    if(isEmpty()){
        cout<<"Stack Underflow"<<endl;
    }
    else{
        for(int i=top; i>=0; i--){
            cout<<s[i]<<" ";
        }
        cout<<endl;
    }
}

int Stack::stackTop(){
    return s[top];
}

int main(){
    int A[] = {1,3,5,7,9};
    Stack s(sizeof(A)/sizeof(A[0]));
    for(int i = 0; i<sizeof(A)/sizeof(A[0]); i++){
        s.push(A[i]);
    }
    s.push(11);

    cout<<"Stack Full : "<<s.isFull()<<endl;

    //Display stack;
    cout<<"Stack: "<<flush;
    s.display();
    
    //Peek
    cout<<"Peek at 0th : "<<s.peek(0)<<endl;
    cout<<"Peek at 3st : "<<s.peek(3)<<endl;
    cout<<"Peek at 10st : "<<s.peek(10)<<endl;
    
    //Top element
    cout<<"Top element : "<<s.stackTop()<<endl;
    
    //Pop
    cout<<"Pop : "<<flush;
    for(int i = 0; i<sizeof(A)/sizeof(A[0]); i++){
        cout<<s.pop()<<" ";
    }
    cout<<endl;
    s.pop();

    cout<<"Stack enpty : "<<s.isEmpty()<<endl;

    return 0; 
}