#include<stdio.h>

double wallis(int iteration);

int main(){
    printf("Estimate: %f", wallis(10000000));
    return 0;
}

double wallis(int iteration){
    double estimate = 2.0;
    for (int i = 1; i < iteration; i++){
        double n = (2.0 * i) / (2 * i - 1);
        double d = (2.0 * i) / (2 * i + 1);
        estimate *= (n * d);
    }
    return estimate;
}
