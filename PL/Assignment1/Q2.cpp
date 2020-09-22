//Accept 3 Numbers
#include<bits/stdc++.h>
using namespace std;
class Numbers{
public:
    int a[3];

    void input()
    {
        cout<<"Enter the Numbers: \n";
        for(int i=0; i<3; i++)
            cin>>a[i];
    }

    void values()
    {
        sort(a, a+3);
        cout<<"\n";
        cout<<"Largest Number: "<<a[2]<<"\n";
        cout<<"Second Largest Number: "<<a[1]<<"\n";
        cout<<"Smallest Number: "<<a[0]<<"\n";
    }
};

int main()
{
    Numbers n;
    n.input();
    n.values();
}