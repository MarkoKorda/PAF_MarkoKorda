#include <iostream>
#include <math.h>

void ispitivanje_odnosa_tocke_i_kruznice(float xr,float yr,float r,float x,float y){
    float d = sqrt((x-xr)*(x-xr)+(y-yr)*(y-yr));
    if (d <= r){
        std::cout<< "Tocka je unutar kruznice!"<<std::endl;
    }
    else{
        std::cout<< "Tocka nije unutar kruznice!"<<std::endl;
    }
}

int main(){
    ispitivanje_odnosa_tocke_i_kruznice(4,7,11,9,13);
    return 0;
}