#include <iostream>

void rjesi_sustav(float a1, float b1, float c1, float a2, float b2, float c2){
    float k1 = a1/a2;
    float b = b1 - k1*b2;
    float c = c1 - k1*c2;
    float y = c/b;
    float x = (c1 - b1*y)/a1;
    std::cout << "x: " << x << "     y: " << y <<std::endl;
};

int main(){
    rjesi_sustav(2,4,10,1,1,3);
    return 0;
};