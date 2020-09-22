//LCM of 2 numbers
#include<bits/stdc++.h>
using namespace std;

int hcf(int a, int b)
{
    if(a==0)
        return b;
    else
        return hcf(b%a, a);
}
int lcm(int a, int b)
{
    //Using the Property of LCM(a, b)*HCF(a, b) = a*b
    int total = a*b;
    return total/hcf(a, b);
}
int main()
{
    int a, b;
    cout<<"Enter 2 Numbers: ";
    cin>>a>>b;
    cout<<"LCM of 2 Numbers is: "<<lcm(a, b);
}
