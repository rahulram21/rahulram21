#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int size;
    cin>>size;
    vector<int> vec1(size);
    for(int i=0; i<size; i++){
        cin>>vec1[i];
    }
    int eraseElm;
    cin>>eraseElm;
    //1 4 6 2 8 9
    vec1.erase(vec1.begin()+eraseElm-1);
    for(int i=0; i<vec1.size(); i++){
        cout<<vec1[i]<<endl;
    }
    //1 6 2 8 9
    int range1, range2;
    cin>>range1;
    cin>>range2;
    vec1.erase(vec1.begin()+range1-1, vec1.begin()+range2-1);
    for(int i=0; i<vec1.size(); i++){
        cout<<vec1[i]<<" ";
    }
    cout<<endl;
    //
    cout<<vec1.size()<<endl;
}