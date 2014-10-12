// sqrt.cpp - using the sqrt() function

#include <iostream>
#include <cmath>

int main()
{
  using namespace std;

  double area;
  cout << "Enter the floor area, in square feet, of your home:  ";
  cin >> area;
  double side;
  side = sqrt(area);
  cout << "That's the equivalent of a square " << side
       << " feet to the side." << endl
       << "How fascinating!" << endl;

  double side2;
  side2 = std::sqrt(area);
  cout << endl << endl << side2;
  return 0;
}

