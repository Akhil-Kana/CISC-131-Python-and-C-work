#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
    if (argc == 1) {
        printf("Hello World!");
    }
    else {
       printf("Hello, %s!", argv[1]); 
    }
}
