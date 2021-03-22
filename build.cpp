#include <stdlib.h>
#include <iostream>
#include <string>

int main(int argc, char** argv){
    if(argc == 1){
        std::cerr << "Error: need build parameters!!" << std::endl;
    }
    std::string s = "g++ ";

    for(int i = 1; i < argc; i++){
        s += std::string(argv[i]) + " ";
    }
    s += "2>&1 | cpppp.py";
    system(s.c_str());
}