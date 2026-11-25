#include<iostream>
using namespace std;

class Node{
    public:
        struct Node *prev;
        int data;
        struct Node *next;
};

class Doubly_linked_list{
    private:
        Node *head;
    public:
        Doubly_linked_list(int A[], int n);
        int insert(int index,int x);
        int Length();
        int Delete(int index);
        void Reverses();
        void Display();
        ~Doubly_linked_list();
};

Doubly_linked_list::Doubly_linked_list(int *A, int n){
    Node *t;
    Node *last;
    head = new Node;
    head->data = A[0];
    head->prev = head->next = NULL;
    last = head;
    for (int i=1; i<n; i++){
        t=new Node;
        t->data = A[i];
        t->next = last->next;
        t->prev = last;
        last->next = t;
        last = t;
    }
}

int Doubly_linked_list :: insert(int index,int x){
    Node *t;
    t=new Node;
    t->data=x;
    t->prev = t->next = NULL;
    Node *p = head;
    if (index<1 || index>Length()){
        return -1;
    }
    if(index==1){
        t->next = head;
        head->prev = t;
        head = t;
    }
    else{
        for(int i=1; i<index;i++ ){
            p=p->next;
        }
        t->next=p->next;
        t->prev=p;
        p->next->prev=t;
        p->next=t;
    }
    return 1;
}

int Doubly_linked_list :: Length(){
    int len=0;
    Node *p = head;
    while(p){
        len++;
        p=p->next;
    }
    return len;
}

int Doubly_linked_list :: Delete(int index){
    if(index<1 || index > Length()) return -1;
    Node *p = head;
    int x;
    if(index==1){
        head = head->next;
        head->prev = NULL;
        free(p);
        return 1;
    }
    else{
        for(int i =1 ; i<index; i++){
            p=p->next;
        }
        p->prev->next = p->next;
        if(p->next) p->next->prev = p->prev;
        int x = p->data;
        free(p);
        return x;
    }
}

void Doubly_linked_list :: Reverses(){
    Node *p = head;
    Node *temp = NULL;
    
    while(p){
        temp = p->prev;
        p->prev = p->next;
        p->next = temp;
        p=p->prev;
        if(p->next == NULL){
            p->next = p->prev;
            p->prev = nullptr;
            head = p;
            break;
        }
    }if(temp) head = temp->prev;
}

void Doubly_linked_list:: Display(){
    Node *p = head;
    while(p){
        cout<<p->data;
        if(p->next!=NULL) cout<<" -> ";
        p=p->next;
    }
}

Doubly_linked_list::~Doubly_linked_list(){
    Node *p = head;
    while(head){
        head = head->next;
        free(p);
        p=head;
    }
}

int main(){
    int A[]= {1,2,3,4,5,7};
    // int A[]= {1};
    Doubly_linked_list d1(A,sizeof(A)/sizeof(A[0]));
    // d1.Display();
    // cout<<endl;
    // d1.insert(2,12);
    // d1.Display();
    // d1.Delete(7);
    // cout<<endl;
    // d1.Display();
    // cout<<endl;
    d1.Reverses();
    d1.Display();
    return 0;
}