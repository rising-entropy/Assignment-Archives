//Copy Constructor Circle Triangle Square
#include<bits/stdc++.h>
using namespace std;

class Area{
public:
    double radius;
    int base, height;
    int side;
    double area;

    Area()
    {
        //initialize the area
        area=0;
    }

    void getData(double r)
    {
        radius = r;
    }

    void getData(int b, int h)
    {
        base = b;
        height = h;
    }

    void getData(int s)
    {
        side = s;
    }

    void compute(double r)
    {
        area = r*r*3.14;
    }

    void compute(int b, int h)
    {
        area = b*h;
        area /= 2;
    }

    void compute(int s)
    {
        area = s*s;
    }

    void display()
    {
        cout<<"\nRequired Area is: "<<area<<"\n";
    }
};

int main()
{
    Area circle;
    Area triangle = circle;     //invoke copy constructor
    Area square = triangle;     //invoke copy constructor

    cout<<"--Area Calculator: --\n";
    cout<<"Choose a Shape:\n";
    cout<<"1. Circle.\n2. Triangle.\n3. Square.\n\n";
    int choice;
    cout<<"Your Choice: ";
    cin>>choice;
    if(choice==1)
    {
        //circle
        double r;
        cout<<"\nEnter Radius: ";
        cin>>r;
        circle.getData(r);
        circle.compute(circle.radius);
        circle.display();
    }
    else if(choice==2)
    {
        //triangle
        int h, b;
        cout<<"\nEnter Base: ";
        cin>>b;
        cout<<"Enter Height: ";
        cin>>h;
        triangle.getData(b, h);
        triangle.compute(triangle.base, triangle.height);
        triangle.display();
    }
    else if(choice==3)
    {
        //square
        int s;
        cout<<"\nEnter Side: ";
        cin>>s;
        square.getData(s);
        square.compute(square.side);
        square.display();
    }
    else
    {
        main();
    }
}