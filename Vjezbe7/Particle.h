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
        
        void move(float dt);

        void return_to_start();
    
    public:
        Particle (float a, float b, float c, float d);
        ~Particle();

        float calculate_range(float dt);

        float calculate_time(float dt);
};