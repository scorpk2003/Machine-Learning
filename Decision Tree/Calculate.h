#include<iostream>
#include<cmath>
#include<vector>
#include<string>
#include<map>

using namespace std;

//      Decision Tree
struct Node{
    string Labels;
    vector<Node>* Child;
}typedef node;

struct DecisionTree{
    node* root;
}typedef tree;
//      End

map<string, int> Split_Data(vector<string> Ent){
    map<string, int> ent;
    for(string attr : Ent){
        ent[attr]++;
    }
    return ent;
}

float Entropy(map<string, int> attributes){
    int count = 0;
    for(auto att : attributes){
        count += att.second;
    }
    float entropy = 0.0;
    for(auto att : attributes){
        float ent = (float) att.second / count;
        entropy += (float) ent * log2 (ent);
    }
    return -entropy;
}

// void Decision_Tree(){
//     float root = Entropy();
// }

// float Information_Gain(Entropy res, vector<string> attributes){
//     return 0.0;
// }