#include<stdio.h>

void initializeArr(float value, float arr[], int size);

float arr[] = {3.45, 23.234, 12.3, 420.69, 6.9, 97.82, 23.2, 1.4};
float value = 3.33;
int size = 5;

int main(){
    initializeArr(value, arr, size);
    printf("[");
    for (int i = 0; i < size; i++){
        if (i == size-1){
            printf("%.2f]\n", arr[i]);
        }
        else{
        printf("%.2f, ", arr[i]);
        }
    }
    return 0;
}

void initializeArr(float value, float arr[], int size){
    for (int i = 0; i < size; i++){
        arr[i] = value;
    }
}