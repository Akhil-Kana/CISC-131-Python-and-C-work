#include<stdio.h>

int num = 87;
char toLetterGrade(int num);
char toLetterGrade2(int num);

int main(){
    printf("Grade: %c", toLetterGrade(num));
    return 0;
}

char toLetterGrade(int num){
    if (num >= 90){
        return 'A';
    }
    else if (num < 60){
        return 'F';
    }
    else if (num >= 80){
        return 'B';
    }
    else if (num >= 70){
        return 'C';
    }
    else{
        return 'D';
    }
}

char toLetterGrade2(int num){
    if (num < 60){
        return 'F';
    }
    else{
        int ten_digit = num/10;
        int ascii_val = 74 - ten_digit;
        return ascii_val;
    }
}