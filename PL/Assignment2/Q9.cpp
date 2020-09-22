//Function Overloading
#include<bits/stdc++.h>
using namespace std;

class Result{
public:
    int a[5];
    int sum;
    double percent;

    void score(int score[5])
    {
        for(int i=0; i<5; i++)
            a[i] = score[i];
    }

    void score()
    {
        sum=0;
        for(int i=0; i<5; i++)
            sum += a[i];
    }

    void score(int sum)
    {
        percent = sum/5;
    }

    void display()
    {
        cout<<"\n--Your Result is: --\n";
        cout<<"Total Marks: "<<sum<<"\n";
        cout<<"Percentage: "<<percent<<"\n";
    }
};

int main()
{
    cout<<"--Score Calculator: --\n";
    cout<<"Enter the Score for 5 Subjects: \n";
    int a[5];
    for(int i=0; i<5; i++)
        cin>>a[i];
    Result r;
    r.score(a);             //insert scores
    r.score();              //gets the sum
    r.score(r.sum);         //gets percentage
    r.display();
}