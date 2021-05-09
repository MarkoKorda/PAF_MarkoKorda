#include <iostream>
#include <math.h>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

class HarmonicOscillator{
    private:
        float x0;
        float v0;
        float k;
        float m;
        float x;
        float v;
        float a;
        float t;

        void move(float dt){
            a = -(k/m)*x;
            v = v + a * dt;
            x = x + v * dt;
            t = t + dt;
            xlist.push_back(x);
            vlist.push_back(v);
            alist.push_back(a);
            tlist.push_back(t);
        };

    public:
        vector<float> xlist;
        vector<float> vlist;
        vector<float> alist;
        vector<float> tlist;

        HarmonicOscillator (float a, float b, float c, float d){
            x0 = a;
            v0 = b;
            k = c;
            m = d;
            x = x0;
            v = v0;
            a = -(k/m)*x;
            t = 0;
            xlist.push_back(x);
            vlist.push_back(v);
            alist.push_back(a);
            tlist.push_back(t);
        };

        void run_event(float T, float dt){
            while(t < T){
                move(dt);
            };
        };
};

int main(){
    HarmonicOscillator h1(5.0,0.0,10.0,50.0);
    h1.run_event(50,0.01);
    int n = h1.tlist.size();
    string xstring;
    string vstring;
    string astring;
    string tstring;
    float x = h1.xlist[0];
    float v = h1.vlist[0];
    float a = h1.alist[0];
    float t = h1.tlist[0];
    xstring = to_string(x);
    vstring = to_string(v);
    astring = to_string(a);
    tstring = to_string(t);
    for (int i = 1; i < n; i++){
        xstring = xstring + "," + to_string(h1.xlist[i]);
        vstring = vstring + "," + to_string(h1.vlist[i]);
        astring = astring + "," + to_string(h1.alist[i]);
        tstring = tstring + "," + to_string(h1.tlist[i]);
    };
    ofstream myfile;
    myfile.open ("x.txt");
    myfile << xstring;
    myfile.close();
    myfile.open ("v.txt");
    myfile << vstring;
    myfile.close();
    myfile.open ("a.txt");
    myfile << astring;
    myfile.close();
    myfile.open ("t.txt");
    myfile << tstring;
    myfile.close();
    return 0;
}

