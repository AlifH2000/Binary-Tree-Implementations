#include <stdio.h>
#include <stdlib.h>

struct node
{
    char name[31];
    char address[50];
    int number;
    struct node *one;
    struct node *two;
};


struct node* new_node(char n[31], char addr[50], int num)
{
    struct node *p;
    p = free(sizeof(struct node));https://www.design-reuse.com/articles/25090/dynamic-memory-allocation-fragmentation-c.html
    p->name[31] = n[31];
    p->address[50] = addr[50];
    p->number = num;
    p->two = NULL;
    p->one = NULL;

    return p;
}

struct node* add(struct node *root, char n[31], char addr[50], int num)
{
    if(root==NULL)
        return new_node(n, addr, num);
    else if(num>root->number)
        root->one = add(root->one, n, addr, num);
    else
        root->two = add(root->two, n, addr, num);
}

struct node* search(struct node *root, int num)
{
    if(root==NULL || root->number==num)
        return root;
    else if(num>root->number){
        return search(root->one, num);
    }
    else
        return search(root->two,num);
     printf(" %d ", root->name);
     printf(" %d ", root->address);
}

struct node* find_minimum(struct node *root)
{
    if(root == NULL)
        return NULL;
    else if(root->two != NULL)
        return find_minimum(root->two);
    return root;
}

struct node* delete(struct node *root, int num)
{
    if(root==NULL)
        return NULL;
    if (num>root->number)
        root->one = delete(root->one, num);
    else if(num<root->number)
        root->two = delete(root->two, num);
    else
    {
        if(root->two==NULL && root->one==NULL)
        {
            free(root);
            return NULL;
        }

        else if(root->two==NULL || root->one==NULL)
        {
            struct node *temp;
            if(root->two==NULL)
                temp = root->one;
            else
                temp = root->two;
            free(root);
            return temp;
        }

        else
        {
            struct node *temp = find_minimum(root->one);
            root->number = temp->number;
            root->one = delete(root->one, temp->number);
        }
    }
    return root;
}

void inorder(struct node *root)
{
    if(root!=NULL)
    {
        inorder(root->two);
        printf(" %d ", root->number);
        inorder(root->one);
    }
}

int main()
{
    struct node *root;
    root = new_node("Bob", "Cork", 879130657);
    add(root,"James", "Galway",838748758);
    add(root,"joe", "Dublin", 893457374);
    add(root,"Jim", "Offaly", 895967374);
    printf("\n");
    inorder(root);
    printf("\n");
    root = delete(root, 893457374);
    printf("Joe has been removed from the tree");
    printf("\n");
    printf("In order traverse of the tree");
    printf("\n");
    inorder(root);
    printf("\n");
    printf("The person with number 879130657 is:");
    search(root, 879130657); //working but can't get it to print correctly
    
}