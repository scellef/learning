// ch0206.cpp
// Write a program that asks the user to enter an hour value and a
// minute value.  The main() function should then pass these two values
// to a type void function that displays the two values in the format
// shown in the following sample run:
//    Enter the number of hours: 9
//    Enter the number of minutes; 28
//    Time: 9:28

#include <iostream>
using namespace std;

void timeformat(int hour,int minute);
int main()
{ 
  int hour;
  int minute;

  cout << "Enter the number of hours:  ";
  cin >> hour;
  cout << "Enter the number of minutes:  ";
  cin >> minute;
  timeformat(hour, minute);

  return 0;
}
  
void timeformat(int hour,int minute)
{
  cout << hour << ":" << minute << endl;
}
