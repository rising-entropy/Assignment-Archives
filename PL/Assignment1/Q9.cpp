//Frequency of Characters in String
#include<bits/stdc++.h>
using namespace std;

class Ticket{
public:
    // Name, Address, Age, Gender, FromStation, ToStation, Price
    string name;
    string address;
    int age;
    string gender;
    string fromStation;
    string toStation;
    int price;

    void book()
    {
        cout<<"\n--Book Your Ticket--\n\n";
        cout<<"Enter Your Name: ";
        getline(cin, name);
        cout<<"Enter Your Address: ";
        getline(cin, address);
        cout<<"Enter Your Age: ";
        cin>>age;
        cout<<"Enter Your Gender: ";
        getline(cin, gender);
        getline(cin, gender);
        cout<<"Enter Your Starting Station: ";
        getline(cin, fromStation);
        cout<<"Enter Your Final Station: ";
        getline(cin, toStation);
        cout<<"Enter Price: ";
        cin>>price;
    }

    void display()
    {
        cout<<"\n--Your Ticket Information.--"<<"\n\n";
        cout<<"Name: "<<name<<"\n";
        cout<<"Address: "<<address<<"\n";
        cout<<"Age: "<<age<<"\n";
        cout<<"Gender: "<<gender<<"\n";
        cout<<"From "<<fromStation<<" Station."<<"\n";
        cout<<"To "<<toStation<<" Station."<<"\n";
        cout<<"Ticket Price: "<<price<<"\n";
    }

    void discount()
    {
        if(price > 2000)
        {
            price = 80*price;
            price = price/100;
        }
    }

    void displayWithDiscount()
    {
        cout<<"\n--Your Ticket Information After Applying Discount.--"<<"\n\n";
        cout<<"Name: "<<name<<"\n";
        cout<<"Address: "<<address<<"\n";
        cout<<"Age: "<<age<<"\n";
        cout<<"Gender: "<<gender<<"\n";
        cout<<"From "<<fromStation<<" Station."<<"\n";
        cout<<"To "<<toStation<<" Station."<<"\n";
        cout<<"Ticket Price: "<<price<<"\n";
    }

};

int main()
{
    Ticket t;
    t.book();
    t.display();
    t.discount();
    t.displayWithDiscount();
}