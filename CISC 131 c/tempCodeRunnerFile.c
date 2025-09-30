#include<stdio.h>

float wallis(int iteration);

int main(){
    printf("Estimate: %f", wallis(10000000));
    return 0;
}

float wallis(int iteration){
    float estimate = 2.0;
    for (double i = 1.0; i < iteration; i++){
        float n = (2.0 * i) / (2.0 * i - 1.0);
        float d = (2.0 * i) / (2.0 * i + 1.0);
        estimate *= (n * d);
    }
    return estimate;
}
