//Tower Of Hanoi

/*
 * Basic Algo:
 * To All the Discs from A to C using B:
 * 1) Get the n-1 discs from A to B using C
 * 2) Get the Largest disc to C
 * 3) Get the n-1 discs from B to C using A
 */

/*
 * It Takes 2^n - 1 steps with this approach.
 * We use Tree Recursion For the Coding.
 */

#include<bits/stdc++.h>
using namespace std;

//Function Syntax: n Discs from a to c Using b

void towerOfHanoi(int n, int a, int c, int b)
{
    //Base Case till n=0
    if(n>0) {
        //Step 1
        towerOfHanoi(n - 1, a, b, c);

        //Step 2
        cout << "Disc " << n << " from " << a << " to " << c << ".\n";

        //Step 3
        towerOfHanoi(n - 1, b, c, a);
    }
}

int main()
{
    cout<<"--Tower Of Hanoi--\n\n";
    int n;
    cout<<"Number of Discs: ";
    cin>>n;

    int a=1, b=2, c=3;

    towerOfHanoi(n, a, c, b);
}