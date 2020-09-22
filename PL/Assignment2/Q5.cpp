//Area of the Box
#include<bits/stdc++.h>
using namespace std;

class BoxArea{
public:
    static int height;
    int length, breadth;
    int area;

    BoxArea(int l, int b)
    {
        length = l;
        breadth = b;
    }

    static int getHeight()
    {
        return height;
    }

    void Area()
    {
        area = length*breadth + length*height + breadth*height;
        area *= 2;
    }

    void display()
    {
        cout<<"\nArea of the Box is: "<<area<<"\n";
    }
};

//static variable height
int Height = 3;
int BoxArea::height = Height;

int main()
{
    cout<<"\n--Calculate Box1 Area: --\n";
    int l1, b1;
    cout<<"Enter Box1 Length: ";
    cin>>l1;
    cout<<"Enter Box1 Breadth: ";
    cin>>b1;

    BoxArea box1(l1, b1);
    box1.Area();
    box1.display();
    int box1Height = box1.getHeight();
    cout<<"Height of the Box is: "<<box1Height<<"\n";

    cout<<"\n--Calculate Box2 Area: --\n";
    int l2, b2;
    cout<<"Enter Box2 Length: ";
    cin>>l2;
    cout<<"Enter Box2 Breadth: ";
    cin>>b2;

    BoxArea box2(l2, b2);
    box2.Area();
    box2.display();
    int box2Height = box2.getHeight();
    cout<<"Height of the Box is: "<<box2Height<<"\n";
}