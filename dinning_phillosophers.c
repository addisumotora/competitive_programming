#include <stdio.h>

#define N 5

void philosphers(){
    while(true){
        think();
        take_fork(i);
        take_fork((i+1)%N);
        eat();
        put_fork(i);
        put_fork((i+1)%N);
    }
}