//Array ADT
#include<bits/stdc++.h>
using namespace std;

void display(int a[], int n)
{
    cout<<"\n";
    for(int i=0; i<n; i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<"\n";
}

void insert(int a[], int n, int index, int value)
{
    int b[n-index-1];
    for(int i=index; i<n-1; i++)
    {
        b[index-i] = a[i];
    }
    a[index] = value;
    for(int i=index; i<n-1; i++)
    {
        a[i+1] = b[i-index];
    }
}

void deleteElement(int a[], int n, int index)
{
    int b[n-index-1];
    for(int i=index+1; i<n; i++)
    {
        b[index+1-i] = a[i];
    }
    for(int i=index; i<n; i++)
    {
        a[i] = b[i-index];
    }
}

void sort(int a[], int n)
{
    //bubblesort
    int temp;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n-1-i; j++)
        {
            if(a[j]>a[j+1]) {
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
}

void search(int a[], int n, int value)
{
    int index=-1;
    for(int i=0; i<n; i++)
    {
        if(a[i] == value)
        {
            index = i;
            break;
        }
    }
    if(index == -1)
    {
        cout<<"\nElement Does Not Exist in the Array.\n";
    }
    else
    {
        cout<<"\nElement Exists at Index "<<index<<" in the Array.\n";
    }
}

int main()
{
    cout<<"-- Array ADT --\n";
    cout<<"Enter Number of Elements of Array: ";
    int n;
    cin>>n;
    int a[n+1];
    cout<<"Enter the Array Elements: ";
    for(int i=0; i<n; i++)
        cin>>a[i];
    int choice;
    cout<<"\nOptions: \n";
    cout<<"1. Display.\n2. Insert.\n3. Delete.\n4. Search.\n5. Sort.\n\n";
    cout<<"Your Choice: ";
    cin>>choice;
    cout<<"\n";
    if(choice==1)
    {
        cout<<"Display Array: ";
        display(a, n);
    }
    else if(choice==2)
    {
        int val, index;
        cout<<"Enter Value of Element to Insert: ";
        cin>>val;
        cout<<"Enter Index of Array where to Insert: ";
        cin>>index;
        insert(a, n+1, index, val);
        cout<<"\nArray After Insertion: ";
        display(a, n+1);
    }
    else if(choice==3)
    {
        int index;
        cout<<"Enter Index of Element to Delete: ";
        cin>>index;
        deleteElement(a, n, index);
        cout<<"\nArray After Deletion: ";
        display(a, n-1);
    }
    else if(choice==4)
    {
        int k;
        cout<<"Enter The Element to Search: ";
        cin>>k;
        search(a, n, k);
    }
    else if(choice==5)
    {
        cout<<"Sorted Array: ";
        sort(a, n);
        display(a, n);
    }
    else
    {
        cout<<"Invalid Choice. Sending you back.";
        main();
    }
}