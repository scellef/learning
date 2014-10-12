// ch0204.cpp
// Write a program that has main() call a user-defined function that takes a Celsius temperature value as an argument and then returns the equivalent Fahrenheit value.  The program should request the Celsuis value as input from the user and display the result, as shown in the following code:
//   Please enter a Celsius value: 20
//   20 degrees Celsius is 68 degrees Fahrenheit. 
// For reference, here is the formula for making the conversion:
// Fahrenheit = 1.8 * degrees Celsius + 32.0

#include <iostream>

float ftoc(float f);

int main()
{
  using namespace std;
  float celsius;

  cout << "Please enter a Celsius value:  ";
  cin >> celsius;
  cout << celsius << " degrees Celsius is " << ftoc(celsius) << " degrees Fahrenheit." << endl;

  return 0;
}

float ftoc(float f)
{
  return f * 1.8 + 32.0;
}
