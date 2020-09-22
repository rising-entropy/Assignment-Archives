//HCF of 2 numbers
#include<bits/stdc++.h>
using namespace std;

//using Euclid's GCD Algorithm
int hcf(int a, int b)
{
    if(a==0)
        return b;
    else
        return hcf(b%a, a);
}
int main()
{
    int a, b;
    cout<<"Enter the 2 Numbers: ";
    cin>>a>>b;
    cout<<"The HCF of 2 Numbers is: "<<hcf(a, b);
}