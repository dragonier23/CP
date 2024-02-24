#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>
#include <sstream>

using namespace std;

int compare(vector<string> firstHand, vector<string> secondHand){ //logic behind whether one is larger than the other
    int max11 = 1, max12 = 1, max21 = 1, max22 = 1; //trying to find the larger hand
    tuple<int> max; 
    string hand1 = firstHand[0], hand2 = secondHand[0];
    char max1 = hand1[0], max2 = hand2[0];
    char rank[] = {'2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'};
    for (int i = 0; i < 5; i++){ // we are going to iterate through the list
        int count1 = 1, count2 = 1;
        for (int j = 0; j < 5; j++){
            if (i != j){
                if (hand1[i] == hand1[j]){ count1++; }
                if (hand2[i] == hand2[j]){ count2++; } 
            }
        }
        //here we are checking if this current card has a higher max no than the others, and if it dosent, we also check if this might be a second largest card count
        if (count1 > max11){ max12 = max11;  max11 = count1; max1 = hand1[i]; } else if (count1 >= max12 && hand1[i] != max1 ) { max12 = count1 ;} //bug here --> if its the first one and it has 2 in a full house, it wont be recorded
        if (count2 > max21){ max22 = max21; max21 = count2; max2 = hand2[i]; } else if (count2 >= max22 && hand2[i] != max2) { max22 = count2 ;} 

    }
    if (max11 > max21){ return 0; }
    else if (max11 < max21){ return 1; }
    else{         
        if (max12 > max22){ return 0; }
        else if (max12 < max22) { return 1; }
        else{
            //if we reach this point, they are the same hand, so we should compare for the card strength
            for (int i = 0; i < 5; i++){
                for (int j = 0; j < 13; j++){
                    if (hand1[i] == rank[j] && hand2[i] == rank[j]){ break; }
                    if (hand1[i] == rank[j]){ return 1; }
                    if (hand2[i] == rank[j]){ return 0; }
                }
            }
        }
    }
}


int main() {
    
    string line;
    ifstream readFile("problemstatement.txt"); //"test.txt"

    //strategy: take in the list, then sort it --> subsequently multiple each by its index + 1
    vector<vector<string>> hands;
    while (getline(readFile, line)){ //this line reads each line, and stores it in the variable line
        vector<string> hand ; 
        string tmp;
        stringstream linestream(line);
        while (getline(linestream, tmp, ' ')){
            hand.push_back(tmp);
        }
        hands.push_back(hand);
    }
    /*
    vector<string> firstHand = {"23332", "765"};
    vector<string> secondHand = {"33322", "765"};
    // so at this point, we have a vector of vectors, of which we can now try to sort
    cout << compare(firstHand, secondHand);
    */
    sort(hands.begin(), hands.end(), compare);
    int sum = 0;
    for (int i = 0; i < 1000; i++){
        cout << hands[i][1] << endl << hands[i][0] << endl;
        sum += (stoi(hands[i][1]) * (i+1));
    }
    cout << sum;
    
    return 0;
}

