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
    sort(vec1.begin(), vec1.end());
    for(int i=0; i<size; i++){
        cout<<vec1[i]<<" ";
    }
}