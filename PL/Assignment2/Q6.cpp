//Constructor Overloading
#include<bits/stdc++.h>
using namespace std;

//area of a Square, Triangle and Circle

class Area{
public:
    double radius;
    int side;
    int height, base;
    int area;

    //Circle
    Area(double r)
    {
        radius = r;
        area = radius*radius*3.14;
    }

    //Square
    Area(int s)
    {
        side = s;
        area = side*side;
    }

    //Triangle
    Area(int h, int b)
    {
        height = h;
        base = b;
        area = height*base;
        area /= 2;
    }

    void display()
    {
        cout<<"Area is: "<<area;
    }

};

int main()
{
    cout<<"--Area Calculator--\n\n";
    cout<<"Choose the Shape: \n";
    int choice;
    cout<<"1. Circle.\n2. Square.\n3. Triangle.\n\n";
    cout<<"Your Choice: ";
    cin>>choice;
    if(choice==1)
    {
        double r;
        cout<<"\nEnter Radius: ";
        cin>>r;
        Area a(r);
        a.display();
    }
    else if(choice==2)
    {
        int s;
        cout<<"\nEnter Side: ";
        cin>>s;
        Area a(s);
        a.display();
    }
    else if(choice==3)
    {
        int h, b;
        cout<<"\nEnter Height and Base: ";
        cin>>h>>b;
        Area a(h, b);
        a.display();
    }
    else
    {
        main();
    }
}