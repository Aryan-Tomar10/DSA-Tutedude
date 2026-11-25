#include<iostream>
using namespace std;

class Node{
    public:
        struct Node *next;
        int data;
};

class SLL{
    private:
        Node *head;
    public:
        SLL(int A[], int n);
        int max();
        void remove_duplicate();
        void recursive_LL(Node *q, Node *p);
        void reverse(){
            recursive_LL(NULL,head);
        }
        void display();
};

SLL::SLL(int *A, int n){
    Node *t, *last;
    head = new Node();
    head -> data = A[0];
    head -> next = NULL;
    last = head;
    for(int i =1; i<n; i++){
        t= new Node();
        t->data = A[i];
        t->next = NULL;
        last->next = t;
        last = t;
    }
}

int SLL::max(){
    int max = INT_MIN;
    Node *p = head;
    while(p){
        if(p->data>max){
            max = p->data;
        }
        p=p->next;
    }
    return max;
}

void SLL::remove_duplicate(){
    Node *p = head;
    Node *q = head->next;
    while(q){
        if(p->data != q->data){
            p=q;
            q=q->next;
        }
        else{
            p->next=q->next;
            free(q);
            q=p->next;
        }
    }
}

void SLL::recursive_LL(Node *q, Node *p){
    if(p){
        recursive_LL(p,p->next);
        p->next = q;
    }else{
        head = q;
    }
}

void SLL::display(){
    Node *p = head;
    while(p){
        cout<<p->data;
        if(p->next) cout<<" -> ";
        p=p->next;
    }
    cout<<endl;
}

int main(){
    int A[]={1,2,3,4,5,6,8,9,10};
    SLL s1(A, sizeof(A)/sizeof(A[0]));
    // s1.display();
    // cout<<endl;
    // cout<<s1.max();
    // cout<<endl;
    // s1.remove_duplicate();
    s1.reverse();
    s1.display();
    return 0;
}