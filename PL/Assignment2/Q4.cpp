//Sports and Object Count
#include<bits/stdc++.h>
using namespace std;

int objectCount = 0;

class Sports{
public:
    string name, country;
    int noOfPlayers;

    Sports()
    {
        objectCount++;
    }

    void insert()
    {
        cout<<"--Enter Sport Data: --\n";
        cout<<"Enter the Name of the Sport: ";
        getline(cin, name);
        cout<<"Enter the Number of Players: ";
        cin>>noOfPlayers;
        cout<<"Enter the Country of Origin: ";
        getline(cin, country); //input buffer
        getline(cin, country);
        cout<<"\n\n";
    }
    void display()
    {
        cout<<"--Sport Data: --\n";
        cout<<"Name of the Sport: "<<name<<"\n";
        cout<<"Number of Players: "<<noOfPlayers<<"\n";
        cout<<"Country of Origin: "<<country<<"\n\n";
    }
};

int main()
{
    Sports s1, s2, s3;
    s1.insert();
    s2.insert();
    s3.insert();
    s1.display();
    s2.display();
    s3.display();
    cout<<"Total Number of Objects: "<<objectCount;
}
