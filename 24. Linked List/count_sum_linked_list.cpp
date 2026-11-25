#include<iostream>
using namespace std;

struct Node{
    int data;
    struct Node *next;
} *first = NULL;

struct Node *create(int A[], int n){
    int i;
    struct Node *t, *last;
    Node *head = new Node();
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
    return head;
}


int count(struct Node *p){
    int c=0;
    while(p){
        c++;
        p=p->next;
    }
    return c;
}

int sum(struct Node *p){
    int s=0;
    while(p!=NULL){
        s+=p->data;
        p=p->next;
    }
    return s;
}

int max(struct Node *p){
    int m=INT_MIN;
    while(p){
        if(p->data>m){
            m=p->data;
        }
        p=p->next;
    }
    return m;
}

int min(struct Node *p){
    int minimum = INT_MAX;
    while(p){
        if(p->data<minimum){
            minimum=p->data;
        }
        p=p->next;
    }
    return minimum;
}

// int linear_search(struct Node *p, int key){
//     while(p){
//         if(p->data == key){
//             return 1;
//         }
//         p=p->next;
//     }
//     return -1;
// }



struct Node * linear_search(struct Node *p, int key){
    struct Node *q;
    while(p){
        if(p->data == key){
            q->next = p->next;
            p->next = first;
            first = p;
            return p;
        }
        q=p;
        p=p->next;
    }
    return NULL;
}

// int insert(struct Node *p, int index, int x){
//     struct Node *t;
//     if (index<0 || index>count(p))
//         return 0;
//     t=new Node[sizeof(struct Node)];
//     t->data = x;
//     if(index==0){
//         t->next = first;
//         first = t;
//     }
//     else{
//         for(int i=1; i<index-1; i++){
//             p=p->next;
//         }
//         t->next = p->next;
//         p->next = t;
//     }
//     return 1;
// }

int inserting_in_sorted_array(struct Node *p, int x){
    struct Node *t, *q=NULL;
    t=new Node();
    t->data = x;
    t->next = NULL;
    if (first==NULL){
        first = t;
    }
    else{
        while(p && p->data<x){
            q=p;
            p=p->next;
        }
        if(p==first){
            t->next = first;
            first = t;
        }
        else{
            t->next = q->next;
            q->next = t;
        }
    }
    return 1;
}

int sorted_Array(struct Node *p){
    int x = INT_MIN;
    while(p){
        if (p->data<x){
            return 0;
        }
        x=p->data;
        p=p->next;
    }
    return 1;
}

int delete_from_LL(struct Node *p, int index){
    struct Node *q = NULL;
    int x=-1;
    if(index<1 || index>count(p))
        return -1;
    if(index==1){
        q=first;
        x=first->data;
        first = first->next;
        free(q);
        return x;
    }
    else{
        for(int i=0;i<index-1;i++){
            q=p;
            p=p->next;
        }
        q->next = p->next;
        x=p->data;
        free(p);
        return x;
    }
}

struct Node* reverse_LL(struct Node *p){
    struct Node *q=NULL, *r=NULL;
    while(p){
        r=p->next;
        p->next=q;
        q=p;
        p=r;
    }
    return q;
}

struct Node *concatinate(struct Node *p, struct Node *q){
    struct Node *last;
    if(p==NULL){
        return q;
    }
    if(q==NULL){
        return p;
    }
    last = p;
    while(last->next!=NULL){
        last=last->next;
    }
    last->next = q;
    return p;
}


int loop(struct Node *p){
    if(p == NULL) return 0; 
    struct Node *fast=p;
    struct Node *slow=p;
    
    while(fast && fast->next){
        slow=slow->next;
        fast=fast->next->next;
        if(slow==fast){
            return 1;
        }
    }
    return 0;
}

void display(struct Node *p){
    while(p!=nullptr){
        cout<<p->data;
        if(p->next) cout<<" -> ";
        p=p->next;
    }
    cout<<endl;
}


int main(){
    int A[]={1,2,3,4,5,6,7,8,9,10};
    // int B[]={7,8,9,10};

    struct Node *t1,*t2;
    first = create(A, sizeof(A)/sizeof(A[0]));
    // Node* firstList = create(A, sizeof(A)/sizeof(A[0]));
    // Node* secondList = create(B, sizeof(B)/sizeof(B[0]));

    // cout<<"Count of the linked list is: "<<count(first)<<endl;
    // cout<<"Sum of the linked list is: "<<sum(first)<<endl;
    // cout<<"Max value of the linked list is: "<<max(first)<<endl;
    // cout<<"Min value of the linked list is: "<<min(first)<<endl;
    // cout<<"Search 2 in the linked list is: "<<linear_search(first,2)<<endl;
    // struct Node *temp;
    // temp = linear_search(first,2);
    // cout<<"Search 2 in the linked list is: "<<temp->data<<endl;

    // insert(first,5,5);
    // inserting_in_sorted_array(first, 11);
    // cout<<sorted_Array(first);

    // cout<<delete_from_LL(first,1)<<endl;
    // first = reverse_LL(first);
    
    // first = concatinate(firstList, secondList);
    // display(first);
    
    t1=first->next->next;
    t2=first->next->next->next->next;
    t2->next = t1;
    cout<<loop(first);


    return 0;
}