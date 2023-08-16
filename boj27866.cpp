#include <iostream>

using std::string;
using std::cin;
using std::cout;
using std::endl;

int main(void)
{
    string str;
    cin >> str;
    int index;
    cin >> index;
    cout << str[index - 1] << endl;
    return 0;
}
