/*
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520) and Abigail McNosky (mcno4197)
Date: 12/12/2023
This program simulates the probability of 100 prisoners with two distinct strategies
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fillDrawers(int drawers[], int length);
int randInt(int min, int max);
void shuffle(int list[], int length);
double strategy1(int numTimes);
double strategy2(int numTimes);
int playGame(int prisoner);


int main()
{
    /*
        This function contains some test code for your 3 functions.
        You will want to create additional test cases!
    */

    // initialize random number generator
    srand(time(0));

    //Test the fillDrawers function
    printf("fillDrawers: ");
    int drawers[10];
    fillDrawers(drawers,10);

    int index = 0;
    while(index < 10){
        printf("%d ", drawers[index]);
        index = index + 1;
    }
    printf("\n");

    //Test the strategy1 and strategy2 functions.
    printf("Strategy 1: %.2f\n", strategy1(10000));
    printf("Strategy 2: %.2f\n", strategy2(10000));
    return 0;
}

//Fill the drawers array.
//After this function is run the drawers array should contain
//a random shuffling of the integers from 0 to length-1 (inclusive)
void fillDrawers(int drawers[], int length){
    //ADD YOUR CODE HERE
    //Hint: you'll want to call the shuffle function written below

    for (int i = 0; i < length; i++){
        drawers[i] = i;
    }
    shuffle(drawers, length);
}

// generate a random number between min (inclusive) and max (exclusive)
int randInt(int min, int max)
{
    return (rand() % (max - min)) + min;
}

//Implement strategy 1 (prisoners randomly open 50 drawers).
//This function should return the percentage of times the 
//prisoners succeeded after simulating the game numTimes.
double strategy1(int numTimes){
    //ADD YOUR CODE HERE
    double correct_count = 0.0;
    double win_count = 0.0;

    for (int i = 0; i < numTimes; i++){
        correct_count = 0.0;
        for (int j = 0; j < 100; j++){
            int win = playGame(j);
            if (win == 1){
                correct_count++;
            }
            if (correct_count == 0.0){
                j = 100;
            }
            else if (correct_count == 100.0){
                win_count++;
            }
        }
    }
    return (double)win_count/numTimes * 100.0;
}

//Implement strategy 2 (the optimal strategy).
//This function should return the percentage of times the 
//prisoners succeeded after simulating the game numTimes.
double strategy2(int numTimes){
    //ADD YOUR CODE HERE
    double correct_count = 0.0;
    double win_count = 0.0;

    for (int i = 0; i < numTimes; i++){
        int drawers[100];
        fillDrawers(drawers, 100);
        correct_count = 0.0;
        for (int j = 0; j < 100; j++){
            int guess = drawers[j];
            for (int k = 0; k < 50; k++){
                if (j == guess){
                    correct_count++;
                    k = 50;
                }
                guess = drawers[guess];
            }
            if (correct_count == 0.0){
                j = 100;
            }
            else if (correct_count == 100.0){
                win_count++;
            }
        }
    }
    return (double)win_count/numTimes * 100.0;
}

// shuffle an array of numbers
void shuffle(int list[], int length)
{
    int i;
    for (i = 0; i < length - 1; i++) 
    {
        int j = i + randInt(0, length - i);
        int temp = list[j];
        list[j] = list[i];
        list[i] = temp;
    }
}

// prisoner randomly picks a randomly shuffled drawer until 50 attempts or they get their number
int playGame(int prisoner){
    int drawers[100];
    fillDrawers(drawers, 100);
    int guess = randInt(0, 100);
    int attempts = 0;
    while (drawers[guess] != prisoner && attempts < 50){
        if (drawers[guess] == -1){
            guess = randInt(0, 100);
        }
        else{
            drawers[guess] = -1;
            guess = randInt(0, 100);
            attempts++;
        }
    }
    return attempts < 50;
}
