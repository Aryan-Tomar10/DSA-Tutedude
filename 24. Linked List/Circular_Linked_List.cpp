#include<iostream>
using namespace std;

class Node{
    public:
    int data;
    struct Node *next;
};

class Circular_linked_list{
    private:
        Node *head;
    public:
        Circular_linked_list(int A[],int n); //constructor to initialise the CLL
        void Display(); //it will display CLL
        int Length();
        int delete_LL(int index);
        Node *getHead(){ return head;} //it will basically return the head
        ~Circular_linked_list(); //this is destructor
};


Circular_linked_list::Circular_linked_list(int *A, int n){
    Node *t;
    Node *tail;

    head = new Node;
    head->data = A[0];
    head->next = head;
    tail = head;

    for(int i=1;i<n;i++){
        t=new Node;
        t->data=A[i];
        t->next = tail->next;
        tail->next = t;
        tail = t;
    }
}

void Circular_linked_list::Display(){
    Node *p = head;
    do{
        cout<<p->data<<" -> "<<flush;
        p=p->next;
    }while(p!=head);
}

Circular_linked_list::~Circular_linked_list(){
    Node *p = head;
    while(p->next!=head){
        p=p->next;
    }
    while(p!=head){
        p->next = head->next;
        delete head;
        head = p->next;
    }

    if(p==head){
        delete head;
        head = NULL;
    }
}

int Circular_linked_list::Length(){
    int len=0;
    Node *p = head;
    do{
        len++;
        p=p->next;
    }while(p!=head);
    return len;
}


int Circular_linked_list::delete_LL(int index){
    Node *p = head;
    Node *q;
    int i, x = -1;
    if(index < 1 || index > Length())
        return -1;
    if(index == 1){
        while(p->next != head) p = p->next;
        x = head->data;
        if(head == p){
            free(head);
            head = NULL;
        }
        else{
            p->next = head->next;
            free(head);
            head = p->next;
        }
    }
    else{
        for(i = 0; i < index - 2; i++){
            p = p->next;
        }
        q = p->next;
        p->next = q->next;
        x = q->data;
        free(q);
    }
    return x;
}


int main(){
    int A[] = {1,3,5,7,9};
    Circular_linked_list c1(A,sizeof(A)/sizeof(A[0]));
    
    c1.delete_LL(2);
    c1.Display(); 
    return 0;
}