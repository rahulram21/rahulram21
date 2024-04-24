#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person{
protected:

    string name;
    int age;
public:

    virtual void getdata()=0;
    virtual void putdata()=0;
};


class Professor:public Person{
public:

    int publications;
    static int countP;
    Professor(){
        countP++;
    }
    void getdata(){
        cin>>name>>age>>publications;
    };
    void putdata(){
        // cout<<"Prof name: "<<name<<", age: "<<age<<", "<<publications<<" , Count : "<<countP; 
        cout<<name<<" "<<age<<" "<<publications<<" "<<countP<<endl;
    }
};
int Professor::countP = 0;


class Student: public Person{
public:

    int marks[6];
    static int countS;
    Student(){
        countS++;
    }
    void getdata(){
        cin>>name>>age;
        int marks[6];
        int i=0;
        while(i<6){
            cin>>marks[i];
            i++;
        }
    };
    void putdata(){
        int sum=0, i=0;
        while(i<6){
            sum += marks[i];
            i++;
        }
        cout<<name<<" "<<age<<" "<<sum<<" "<<countS<<endl;
    }
};
int Student::countS = 0;


int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
