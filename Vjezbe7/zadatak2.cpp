#include <iostream>
#include <Particle.h>

using namespace std;

int main(){
    Particle p1(5,60,10,20);
    float r1 = p1.calculate_range(0.01);
    float t1 = p1.calculate_time(0.01);
    std::cout << "Domet je: " << r1 << " m" << std::endl;
    std::cout << "Vrijeme je: " << t1 << " s" << std::endl;

    Particle p2(10,45,0,0);
    float r2 = p2.calculate_range(0.01);
    float t2 = p2.calculate_time(0.01);
    std::cout << "Domet je: " << r2 << " m" << std::endl;
    std::cout << "Vrijeme je: " << t2 << " s" << std::endl;

    Particle p3(20,30,30,20);
    float r3 = p3.calculate_range(0.01);
    float t3 = p3.calculate_time(0.01);
    std::cout << "Domet je: " << r3 << " m" << std::endl;
    std::cout << "Vrijeme je: " << t3 << " s" << std::endl;
    return 0;
};
