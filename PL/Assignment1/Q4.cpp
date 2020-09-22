//Palindrome or Not
#include<bits/stdc++.h>
using namespace std;

int isPalindrome(int n)
{
    int c=0;
    string s = to_string(n);
    int a[s.length()];
    for(int i=0; i<s.length(); i++)
        a[i] = s[i];
    for(int i=0; i<s.length(); i++)
    {
        if(a[i] != a[s.length()-1-i])
            c++;
    }
    if(c>0)
        return 0;
    else
        return 1;
}

int main()
{
    int n;
    cout<<"Enter the Number: ";
    cin>>n;
    int y = isPalindrome(n);
    if(y==1)
        cout<<"The Given Number is a Palindrome.";
    else
        cout<<"The Given Number is not a Palindrome.";
}