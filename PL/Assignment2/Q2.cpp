//Department Class Parameterized Constructor
#include<bits/stdc++.h>
using namespace std;

class Department{
private:
    string Dname;
    int no_of_emp, averageSalary;
public:
    Department(string departmentName, int employees, int avgSalary){
        Dname = departmentName;
        no_of_emp = employees;
        averageSalary = avgSalary;
    }
    void display()
    {
        cout<<"\n--Department Details: --\n";
        cout<<"Department Name: "<<Dname<<"\n";
        cout<<"Number of Employees: "<<no_of_emp<<"\n";
        cout<<"Average Salary: "<<averageSalary<<"\n";
    }
};

int main()
{
    cout<<"--Enter Department Details: --\n";
    int avSal, empNo;
    string name;
    cout<<"Enter Department Name: ";
    getline(cin, name);
    cout<<"Enter Number of Employees: ";
    cin>>empNo;
    cout<<"Enter Average Salary: ";
    cin>>avSal;
    Department d(name, empNo, avSal);
    d.display();
}

