#include<iostream>
using namespace std;

class Node{
    public:
    int coeff;
    int exp;
    struct Node *next;
};

class Poly_ll{
    private:
        Node *head;
    public:
        Poly_ll();
        void create();
        void Evaluate(int x);
        void Display();
};

Poly_ll::Poly_ll(){
    head = NULL;
    Node *p;
    Node *last = NULL;
    int num, i;
    cout << "Enter the no. of terms: ";
    cin >> num;
    for(i = 0; i < num; i++){
        p = new Node;
        cout << "Enter the coeff and exp: ";
        cin >> p->coeff >> p->exp;
        p->next = NULL;
        if(head == NULL){
            head = last = p;
        } else {
            last->next = p;
            last = p;
        }
    }
}

void Poly_ll::Evaluate(int x){
    Node *p = head;
    int sum = 0;
    while(p){
        sum += p->coeff * pow(x,p->exp);
        p=p->next;
    }
    cout<<sum;
}

void Poly_ll::Display(){
    Node *p = head;
    while(p){
        cout<<p->coeff<<"x^"<<p->exp;
        if(p->next) cout<<" + ";
        p=p->next;
    }
}

int main(){
    Poly_ll p1;
    p1.Evaluate(2);
    cout<<endl;
    p1.Display();
    return 0;
}