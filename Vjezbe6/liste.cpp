#include <iostream>

int main(){
    int list[6] = {1,2,3,4,5,6};
    for(int i=0;i<6;i++){
        std::cout << list[i] << " ";
    }
    std::cout << std::endl;
    std::cout << list << std::endl;
    return 0;
}