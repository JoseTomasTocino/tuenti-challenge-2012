#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    unsigned numCases;
    cin >> numCases;

    while(numCases > 0){
        unsigned liters = 0;

        double numberOfRaces;
        unsigned numberOfKarts;
        unsigned numberOfGroups;

        cin >> numberOfRaces >> numberOfKarts >> numberOfGroups;

        // cout << "Number of races: " << numberOfRaces << endl
        //      << "Number of karts: " << numberOfKarts << endl
        //      << "Number of groups: " << numberOfGroups << endl;

        unsigned * membersOfGroups = new unsigned[numberOfGroups];
        unsigned thisGroupMembers;

        for (unsigned i = 0; i < numberOfGroups; ++i)
            cin >> membersOfGroups[i];

        unsigned currentGroup = 0;

        unsigned localNumberOfKarts;

        bool     fullCycleCompleted = false;
        unsigned fullCycleLiters    = 0;
        unsigned fullCycleRaces     = 0;
        unsigned fullCycleGroups    = 0;

        while(numberOfRaces > 0){

            // Reset the local amount of karts
            localNumberOfKarts = numberOfKarts;

            for(unsigned i = 0; i < numberOfGroups; ++i){
                if (membersOfGroups[currentGroup] <= localNumberOfKarts){

                    thisGroupMembers = membersOfGroups[currentGroup];

                    localNumberOfKarts -= thisGroupMembers;

                    liters += thisGroupMembers;

                    if (!fullCycleCompleted){
                        fullCycleLiters += thisGroupMembers;
                        fullCycleGroups += 1;
                    }

                    currentGroup = (currentGroup + 1) % numberOfGroups;
                } else {
                    break;
                }
            }

            if (!fullCycleCompleted){
                fullCycleRaces += 1;
            }

            numberOfRaces--;
            
            if(currentGroup == 0){
                // cout << "Full cycle completed" << endl;
                // cout << "NumRaces:" << numberOfRaces << endl;
                // cout << "Liters: " << fullCycleLiters << endl;
                // cout << "Groups: " << fullCycleGroups << endl;
                // cout << "Races: " << fullCycleRaces << endl;
                
                fullCycleCompleted = true;

                unsigned remainingFullCycles = numberOfRaces / (float) fullCycleRaces;

                numberOfRaces -= remainingFullCycles * fullCycleRaces;
                liters += remainingFullCycles * fullCycleLiters;
                currentGroup = (currentGroup + fullCycleGroups) % numberOfGroups;
                //*/
            }
        }

        delete [] membersOfGroups;

        cout << liters << endl;
        numCases --;
    }

    return 0;
}
