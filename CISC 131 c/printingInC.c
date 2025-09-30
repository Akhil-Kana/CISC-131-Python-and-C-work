#include<stdio.h>

int main(){
    int fav_num = 100;
    char fav_char = 's';
    char lst[3][3];
    
    for (int i = 0; i <= 2; i++){
        for (int j = 0; j <= 2; j++){
            if (i % 2 == 0){
                if (j % 2 == 0){
                    lst[i][j] = fav_num;
                }
                else{
                    lst[i][j] = fav_char;
                }
            }
            else{
                if (j % 2 == 0){
                    lst[i][j] = fav_char;
                }
                else{
                    lst[i][j] = fav_num;
                }
            }
        }
    }
    for (int k = 0; k < 3; k++){
        for (int l = 0; l < 3; l++){
            if (k % 2 == 0){
                if (l % 2 == 0){
                    printf("%4d", lst[k][l]);
                }
                else{
                    printf("%4c", lst[k][l]);
                }
            }
            else{
                if (l % 2 == 0){
                    printf("%4c", lst[k][l]);
                }
                else{
                    printf("%4d", lst[k][l]);
                }
            }
        }
        printf("\n");
    }
    return 0;
}
