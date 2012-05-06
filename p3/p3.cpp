#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    vector<int> values;

    int thisValue;

    while(!cin.eof()){
        cin >> thisValue;
        if(!cin.eof()) values.push_back(thisValue);
    }
    
    unsigned s = values.size();

    int maxLocalDif, maxLocalDifPos, localDif;
    int globalDif = 0, globalDifStart = 0, globalDifEnd = 0;

    int minimumFound = 9999999;

    for (unsigned i = 0; i < s; ++i)
    {
        maxLocalDif = 0;
        maxLocalDifPos = 0;

        if(values[i] > minimumFound){
            continue;
        } else{
            minimumFound = values[i];
        }

        for (unsigned j = i + 1; j < s; ++j){
            localDif = values[j] - values[i];
            if (localDif > maxLocalDif){
                maxLocalDif = localDif;
                maxLocalDifPos = j;
            }
        }

        if (maxLocalDif > globalDif){
            globalDif = maxLocalDif;
            globalDifStart = i;
            globalDifEnd = maxLocalDifPos;
        }


    }

    cout << (globalDifStart * 100) << " ";
    cout << (globalDifEnd * 100) << " ";
    cout << globalDif << endl;
//*/
    return 0;
}
