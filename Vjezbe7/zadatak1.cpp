#include <iostream>
#include <math.h>

class Particle{
    private:
        float v0;
        float theta;
        float x0;
        float y0;
        float vx;
        float vy;
        float x;
        float y;
        
        void move(float dt){
            vy = vy - 9.81*dt;
            x = x + vx * dt;
            y = y + vy * dt;
        };

        void return_to_start(){
            vx = v0 * cos(theta);
            vy = v0 * sin(theta);
            x = x0;
            y = y0;
        };
    
    public:
        Particle (float a, float b, float c, float d){
            v0 = a;
            theta = (b/180)*3.14159;
            x0 = c;
            y0 = d;
            vx = v0 * cos(theta);
            vy = v0 * sin(theta);
            x = x0;
            y = y0;
        };

        float calculate_range(float dt){
            while (y >= 0){
                move(dt);
            }
            float d = x - x0;
            return_to_start();
            return d;
        };

        float calculate_time(float dt){
            float t = 0.0;
            while (y >= 0){
                move(dt);
                t = t + dt;
            }
            return_to_start();
            return t;
        };
};

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
}
