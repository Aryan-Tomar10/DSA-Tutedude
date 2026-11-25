#include<iostream>
#include<queue>
#include<stack>

using namespace std;

class Node{
    public:
        Node *lchild;
        int data;
        Node *rchild;
};

class Trees{
    private:
        Node *root;
    public:
        Trees();
        void CreateTree();
        void Inorder(Node *p);
        void Inorder(){Inorder(root);}
};

Trees::Trees(){
    root = nullptr;
}

void Trees::CreateTree(){
    Node *p;
    Node *t;
    int x;
    queue<Node*>q;

    root = new Node;
    cout<<"Enter root data : "<<flush;
    cin>>x;
    root->data = x;
    root->lchild = nullptr;
    root->rchild = nullptr;
    q.emplace(root);

    while(!q.empty()){
        p = q.front();
        q.pop();

        cout<<"Enter the left chid data : "<<p->data<<" : "<<flush;
        cin>>x;
        if(x != -1){
            t = new Node;
            t->data = x;
            t->lchild = nullptr;
            t->rchild = nullptr;
            p->lchild = t;
            q.emplace(t);
        }

        cout<<"Enter the right chid data : "<<p->data<<" : "<<flush;
        cin>>x;
        if(x != -1){
            t = new Node;
            t->data = x;
            t->lchild = nullptr;
            t->rchild = nullptr;
            p->rchild = t;
            q.emplace(t);
        }
    }
}
void Trees::Inorder(Node *p){
    if(p){
        Inorder(p->lchild);
        cout<<p->data<<" , "<<flush;
        Inorder(p->rchild);
    }
}

int main(){
    Trees bt;

    bt.CreateTree();
    cout<<endl;
    
    cout<<"Inorder : "<<flush;
    bt.Inorder();
    cout<<endl;
    return 0;
}