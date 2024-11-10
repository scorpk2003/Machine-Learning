#include<iostream>
#include<fstream>
#include<vector>
#include<sstream>
#include<string>
#include <map>

using namespace std;

map<string, vector<string>> readCSV(const string &filePath){

    // Create output
    map<string, vector<string>> output;

    vector<string> labels;

    // Read File
    ifstream file(filePath);

    // Check File Open or Exsits
    if(!file.is_open()){
        cout<<"file can not open or file not exists: "<<filePath<<endl;
        return output;
    }

    // Read line by lines
    string line;

    // Read first line(label)
    getline(file, line);
    stringstream ss(line);
    string token;

    while(getline(ss,token,',')){
        labels.push_back(token);
    }

    while(getline(file, line)){
        stringstream ss(line);
        int index = 0;
        while(getline(ss, token, ',')){
            output[labels[index]].push_back(token);
            index++;
        }
        ss.clear();
        ss.str("");
    }
    return output;
}