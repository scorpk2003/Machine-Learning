#include<iostream>
#include"input.h"
#include"Calculate.h"

using namespace std;

int main(){
    string titanicFilePath = "E:\\asus\\Machine Learning\\Decision Tree\\house-prices.csv";
    map<string, vector<string>> input = readCSV(titanicFilePath);
    map<string, map<string, int>> spl_data;
    map<string, float> ent_val;
    for(auto k = input.begin(); k != input.end(); k++){
        spl_data[k->first] = Split_Data(k->second);
    }
    for(auto k = spl_data.begin(); k != spl_data.end(); k++){
        ent_val[k->first] = Entropy(k->second);
    }
    for(auto val : ent_val){
        cout<<"\t\t\tKey: "<<val.first<<endl;
        cout<<"\t\t\tEntropy: "<<val.second<<endl;
        cout<<endl;
    }
}