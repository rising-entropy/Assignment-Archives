//Bank Class
#include<bits/stdc++.h>
using namespace std;

class Bank{
public:
    int ID;
    string Name;
    string Address;
    int NoOfCustomers;

    void input()
    {
        cout<<"Enter ID: ";
        cin>>ID;
        cout<<"Enter Branch Name: ";
        cin.ignore(numeric_limits<streamsize>::max(),'\n'); //clearing input buffer
        getline(cin, Name);
        cout<<"Enter Branch Address: ";
        getline(cin, Address);
        cout<<"Enter Number of Customers: ";
        cin>>NoOfCustomers;
    }

    void display()
    {
        cout<<"Bank ID: "<<ID<<"\n";
        cout<<"Branch Name: "<<Name<<"\n";
        cout<<"Branch Address: "<<Address<<"\n";
        cout<<"Number of Customers: "<<NoOfCustomers<<"\n\n";
    }
};

int main()
{
    Bank b[5];
    for(int i=0; i<5; i++)
    {
        cout<<"Input Data for Bank #"<<i+1<<":\n";
        b[i].input();
        cout<<"\n";
    }
    for(int i=0; i<5; i++)
    {
        cout<<"\nDisplay Data For Bank #"<<i+1<<":\n";
        b[i].display();
    }

}