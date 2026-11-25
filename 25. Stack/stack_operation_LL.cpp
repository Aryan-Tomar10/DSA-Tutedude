#include<iostream>
using namespace std;

class Node{
    public:
        int data;
        struct Node *next;
};

class Stack_operations{
    private:
        Node *head;
    public:
        Stack_operations();
        void push(int x);
        int pop();
        int peek(int index);
        bool isFull();
        bool isEmpty();
        void display();
        int stackTop();
};

Stack_operations::Stack_operations(){
    head = NULL;
}

void Stack_operations::push(int x){
    Node *temp = new Node();
    temp->data = x;
    temp->next = head;
    head = temp;
}


int Stack_operations::pop(){
    int x = -1;
    if(head == NULL){
        cout<<"Stack Underflow"<<endl;
    }
    else{
        Node *temp = head;
        x = temp->data;
        head = temp->next;
        delete temp;
    }
    return x;
}

int Stack_operations::peek(int index){
    int x = -1;
    if(head == NULL){
        cout<<"Stack Underflow"<<endl;
    }
    else{
        for(int i = 1; i<index;i++){
            head = head->next;
        }
        x = head->data;
    }
    return x;
}

bool Stack_operations::isEmpty(){
    if(head == NULL){
        return true;
    }
    return false;
}

void Stack_operations::display(){
    if(head == NULL){
        cout<<"Stack Underflow"<<endl;
    }else{
        Node *temp = head;
        while(temp!=NULL){
            cout<<temp->data<<" ";
            temp = temp->next;
        }
    }
}

int main(){
    Stack_operations s1;
    s1.push(1);
    s1.push(2);
    s1.push(3);
    s1.push(4);
    s1.push(5);
    s1.display();

    cout<<endl;
    // cout<<s1.pop()<<endl;
    // cout<<s1.pop()<<endl;
    // cout<<s1.pop()<<endl;
    // cout<<s1.pop()<<endl;
    cout<<s1.peek(3)<<endl;
    

    return 0;

}