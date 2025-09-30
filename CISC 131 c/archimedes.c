#include <math.h>
#include <stdio.h>
#define degToRad(angleInDegrees)((angleInDegrees) * M_PI / 180.0)

double archimedes(int num_sides);
void printArchimedes(int low, int high);

int main(){
    printArchimedes(2, 12);
    return 0;
}

double archimedes(int num_sides){
    if (num_sides < 3){
        return 0;
    }
    else{
        double half_angle = 360.0/num_sides/2;
        double s_len = 2*sin(degToRad(half_angle));
        double perimeter = s_len*(num_sides);
        double pi = perimeter/2.0;
        return pi;
    }
}

void printArchimedes(int low, int high){
    printf("n  |  pi\n");
    printf("--------\n");
    for (int i = low; i <= high; i++){
        printf("%2d |  %f\n", i, archimedes(i));
    }
}