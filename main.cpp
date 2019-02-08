#include <iostream>
#include <bitset>
#include <chrono>

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    union Num {
        struct reim{
            double re;
            double im;
        } part;
        double pair[2];
    } num;
    num.part.re = 4;
    num.part.im = 3;

    std::cout << num.pair[0] << " " << num.pair[1] << std::endl;
    auto duration = std::chrono::high_resolution_clock::now() - start;
    long long   microseconds = std::chrono::duration_cast<std::chrono::nanoseconds>(duration).count();
    std::cout << microseconds;



    return 0;
}