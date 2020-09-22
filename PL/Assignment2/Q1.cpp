//Sales Employee
#include<bits/stdc++.h>
using namespace std;

class Employee{
public:
    int emp_id, salary;
    string name, designation, dept;
    Employee(){
        dept = "Sales";
        salary = 10000;
    }
    void insertID(int id)
    {
        emp_id = id;
    }
    void insertDesignation(string desig)
    {
        designation = desig;
    }
    void enterName(string name2)
    {
        name = name2;
    }
    void display()
    {
        cout<<"Employee ID: "<<emp_id<<"\n";
        cout<<"Name: "<<name<<"\n";
        cout<<"Designation: "<<designation<<"\n";
        cout<<"Department: "<<dept<<"\n";
        cout<<"Salary: "<<salary<<"\n";
    }
};

int main()
{
    cout<<"--Enter Your Details: --\n";
    Employee e;
    int id;
    cout<<"Enter your Employee ID: ";
    cin>>id;
    string name, designation;
    cout<<"Enter Your Name: ";
    getline(cin, name); //clear Input Buffer
    getline(cin, name);
    cout<<"Enter Your Designation: ";
    getline(cin, designation);
    e.insertID(id);
    e.insertDesignation(designation);
    e.enterName(name);
    cout<<"\n--Your Details: --\n";
    e.display();
}