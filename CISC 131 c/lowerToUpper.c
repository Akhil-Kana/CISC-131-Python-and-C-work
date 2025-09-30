#include<stdio.h>

char lowerToUpper(char ltr);

int main(){
    printf("Uppercase of 'a' is '%c'.", lowerToUpper('a'));
    return 0;
}

char lowerToUpper(char ltr){
    return ltr -= 32;
}
