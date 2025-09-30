#include<stdio.h>

void to133t(char _string[]);

int main(){
    char _string[] = "hello"; //{'h', 'e', 'l', 'l', 'o', '\0'};
    to133t(_string);
    printf("hello : %s", _string);
    return 0;
}

void to133t(char _string[]){
    int index = 0;
    while (_string[index] != '\0'){
        if (_string[index] == 'e' || _string[index] == 'E'){
            _string[index] = '3';
        }
        else if (_string[index] == 's' || _string[index] == 'S'){
            _string[index] = '5';
        }
        else if (_string[index] == 'o' || _string[index] == 'O'){
            _string[index] = '0';
        }
        index++;
    }
}
