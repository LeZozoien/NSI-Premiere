#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

double heron(double n, double p){
    double u = n;
    unsigned int i = 0;

    while((u - sqrt(n)) > p){
        u = (u+n/u)/2;
        i++;
    }

    return u;
}

int main(){

    double racine = heron(2, 0.001);

    std::cout << racine;
}