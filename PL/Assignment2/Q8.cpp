//Powers Function Overload
#include<bits/stdc++.h>
using namespace std;

class Exponence{
public:
    int n;
    double m;
    double result;

    void power(double a, int b=2)
    {
        m = a;
        n = b;
    }

    void power(int a, int b=2)
    {
        a = double(a);
        m = a;
        n = b;
    }

    void answer()
    {
        result = 1;
        for(int i=0; i<n; i++)
        {
            result *= m;
        }
    }

    void display()
    {
        cout<<"\nResult is: "<<result;
    }
};

int main()
{
    cout<<"-- Power Calculator --\n\n";
    Exponence e;
    cout<<"Choose an Option: \n";
    int choice;
    cout<<"1. Double Power Int.\n2. Double Power Default.\n3. Int Power Int.\n4. Int Power Default.\n\n";
    cout<<"Your Choice: ";
    cin>>choice;
    cout<<"\n";
    if(choice==1)
    {
        cout<<"Enter Base: ";
        cin>>e.m;
        cout<<"Enter Power: ";
        cin>>e.n;
        e.power(e.m, e.n);
        e.answer();
        e.display();
    }
    else if(choice==2)
    {
        cout<<"Enter Base: ";
        cin>>e.m;
        e.power(e.m);
        e.answer();
        e.display();
    }
    else if(choice==3)
    {
        cout<<"Enter Base: ";
        cin>>e.m;
        cout<<"Enter Power: ";
        cin>>e.n;
        int temp;
        temp = e.m;
        e.power(temp, e.n);
        e.answer();
        e.display();
    }
    else if(choice==4)
    {
        cout<<"Enter Base: ";
        cin>>e.m;
        int temp = e.m;
        e.power(temp);
        e.answer();
        e.display();
    }
    else
    {
        main();
    }
}