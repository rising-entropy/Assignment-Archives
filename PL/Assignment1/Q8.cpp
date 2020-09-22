//Frequency of Characters in String
#include<bits/stdc++.h>
using namespace std;

void frequencyOfChars(string s)
{
    //Uppercase Letters
    int a[26] = {};
    for(int i=0; i<s.length(); i++)
    {
        a[int(s[i])-65]++;
    }

    cout<<"\n";

    //Lowercase Letters
    int b[26] = {};
    for(int i=0; i<s.length(); i++)
    {
        b[int(s[i])-97]++;
    }

    for(int i=0; i<26; i++)
    {
        if(a[i]>0)
        {
            cout<<char(65+i)<<": "<<a[i]<<"\n";
        }
    }

    for(int i=0; i<26; i++)
    {
        if(b[i]>0)
        {
            cout<<char(97+i)<<": "<<b[i]<<"\n";
        }
    }




}

int main()
{
    string s;
    cout<<"Enter the String: ";
    cin>>s;
    frequencyOfChars(s);
}