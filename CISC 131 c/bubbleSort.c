#include<stdio.h>

void bubbleSort(float arr[], int size);

float arr[] = {1,5,23,6,23,11,9,10};
int size = 5;

int main(){
    bubbleSort(arr, size);
    for (int i = 0; i < size; i++){
        if (i == size-1){
            printf("%f]\n", arr[i]);
        }
        else{
        printf("%f, ", arr[i]);
        }
    }
}

void bubbleSort(float arr[], int size){
    for (int i = 0; i < size; i++){
        for (int j = i + 1; j <= size; j++){
            if (arr[j] < arr[i]){
                float tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
}