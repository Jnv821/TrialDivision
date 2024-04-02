#include <stdio.h>
#include <time.h>
#include <math.h>
#include <string.h>

const char *filename = "./result.txt";


void resetFile(){
    FILE *filePointer = fopen("./result.txt", "w");
    fclose(filePointer);
}

void addText(char *text){
    FILE *filePointer = fopen(filename, "a");
    fprintf(filePointer, text);
    fclose(filePointer);
}

void trialDivision(int n){
    if (n <= 1)
    {
        printf("false\n");   
    } else if (n <= 3)
    {
        printf("false\n");
    } else
    {
    for(size_t m = 3; m < sqrt(n); m+=2)
        {
            if(n % m == 0)
            {
               printf("false\n");
            }
        }
    }
    printf("true\n");
}

double runFunction(){
    double resultTimes[6];
    for (size_t i = 0; i < 6; i+=1)
    {
        double startTime = (double)clock()/CLOCKS_PER_SEC;
        for (size_t j = 0; j < pow(10,i+1); j+=1)
        {
            trialDivision(j);
        }
        double endTime = (double)clock()/CLOCKS_PER_SEC;
        double timeElapsed = endTime - startTime;
        resultTimes[i] = timeElapsed;
        char resultBuffer[50];
        sprintf(resultBuffer, "Result for 10^%d: %.12f\n", i+1, timeElapsed);
        addText(resultBuffer);
    }

    double *result = resultTimes;
    return *result;
}



int main() {
    resetFile();
    for (size_t i = 0; i < 5; i++)
    {
        char resultBuffer[26];
        sprintf(resultBuffer, "==== Test Number %d ====\n", i+1);
        addText(resultBuffer);
        runFunction();
        printf("Next Iteration");
    }
    
    return 0;
}

