// ch0203.cpp
// Write a C++ program that uses three user-defined functions (counting main() as one) and produces the following output:
//
// Three blind mice
// Three blind mice
// See how they run
// See how they run

#include <iostream>

void mice();
void run();

int main()
{
  mice();
  mice();
  run();
  run();

  return 0;
}

void mice()
{
  using namespace std;  
  cout << "Three blind mice" << endl;
}

void run()
{
  using namespace std;  
  cout << "See how they run" << endl;
}
