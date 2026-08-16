#include <iostream>

//typedef bool gate_t;
using gate_t = bool;

int main()
{
    gate_t open = true;

    if ( open )
    {
        std::cout << "the people can come in\n";
    }
    else
    {
        std::cout << "the people can't come in\n";
    }
}