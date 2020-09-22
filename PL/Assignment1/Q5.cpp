//Factorial
#include<bits/stdc++.h>
using namespace std;
long long int factorial(int n)
{
    if(n == 0)
        return 1;
    else
        return factorial(n-1)*n;
}
int main()
{
    int n;
    cout<<"Enter the Number: ";
    cin>>n;
    cout<<"Factorial of the Number is: "<<factorial(n);
}