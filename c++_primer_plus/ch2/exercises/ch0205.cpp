// ch0205.cpp
// Write a program that has main() call a user-defined function that 
// takes distance in light years as an argument and then returns the 
// distance in astronomical units.  The program should request the light
// year value as input from the user and display the result, as shown in
// the following code:
//   Enter the number of light years: 4.2
//   4.2 light years = 265608 astronomical units
//   1 light year = 63,240 astronomical units

#include <iostream>
double lightyrstoau(double lightyrs);

int main()
{
  using namespace std; 

  cout << "Enter the number of light years:  ";
  double lightyrs;
  cin >> lightyrs;
  cout << lightyrs << " light years = " << lightyrstoau(lightyrs) 
       << " astronomical units" << endl;
}

double lightyrstoau(double lightyrs)
{
  return lightyrs * 63240;
}
