//Nicholas Lui
//Udemy coding problem section 8
//date modified - 1/20/2022 

#include <iostream>
using namespace std;

int main(){
    //create variable
    int userInput{}, dollarCount{}, quarterCount{}, dimeCount{}, nickelCount{}, pennyCount{};
    cout << "Please enter how many cents you have." << endl;
    cin >> userInput;
    cout << userInput << "\n";

    //op1
    dollarCount = userInput / 100;
    userInput = userInput % 100;

    //op2
    quarterCount = userInput / 25;
    userInput = userInput % 25;

    //op3
    dimeCount = userInput / 10;
    userInput = userInput % 10;

    //op4
    nickelCount = userInput / 5;
    userInput = userInput % 5;

    //op5
    pennyCount = userInput / 1;
    userInput = userInput % 1;

    cout << "There are " << dollarCount << " dollars." << endl;
    cout << "There are " << quarterCount << " quarters." << endl;
    cout << "There are " << dimeCount << " dimes." << endl;
    cout << "There are " << nickelCount << " nickels." << endl;
    cout << "There are " << pennyCount << " pennies." << endl;
    
    return 0;
}