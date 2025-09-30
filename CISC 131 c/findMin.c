#include<stdio.h>

int findMin(int arr[], int length);
int findMin2(int arr[], int length);

int arr[] = {3, 4, -10, 7, 8, 10};
int length = 6;

int main(){
    printf("The array: [");
    for (int i = 0; i < arr[length]; i++){
        if (i == length-1){
            printf("%i]\n", arr[i]);
        }
        else{
        printf("%i, ", arr[i]);
        }
    }
    printf("The minimum: %i", findMin2(arr, length));
    return 0;
}

int findMin(int arr[], int length){
    if (length == 1){
        return arr[0];
    }
    else{
        int _min = findMin(arr, length-1);
        if (arr[length] < _min){
            return arr[length];
        }
        else{
            return _min;
        }
    }
}

int findMin2(int arr[], int length){
    int _min = arr[0];
    for (int i = 0; i < length; i++){
        if (_min > arr[i]){
            _min = arr[i];
        }
    }
    return _min;
}