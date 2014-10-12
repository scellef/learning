// ch0202.cpp
// Write a C++ program that asks for a distance in furlongs and converts it to yards (One furlong is 220 yards).

#include <iostream>

int main()
{
  using namespace std;

  cout << "Enter the number of furlongs:  ";
  int furlongs;
  cin >> furlongs;
  int yards = furlongs * 220;
  cout << furlongs << " is equal to " << yards << " yards." << endl;

  return 0;
}
