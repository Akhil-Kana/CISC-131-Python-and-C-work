#include <stdio.h>
int main(){
    int l = 0;
    int w = 0; 
    printf("What size LxW board would you like? (Length): ");
    scanf(" %i", &l);
    printf("What size LxW board would you like? (Width): ");
    scanf(" %i", &w);
    char board[l][w];
    /** Fill in the board **/
    int i = 0;
    int j = 0;
    while(i < l) /** Rows **/
    {
         j = 0;
        while(j < w) /** Cols **/
        {
            if( (i+j)%2 == 0) /** Even **/
            {
                 board[i][j] = 'O';
            }
            else /** Odd **/
            {
                board[i][j] = 'X';
            }
            j++; 
        } 
        i++;
    } 
    /** ADD YOUR PRINT CODE HERE **/
    i = 0;
    while (i<l){
        j = 0;
        while (j<w){
            printf("%c", board[i][j]);
            j++;
        }
        i++;
        printf("\n");
    }
    return 0; 
} 