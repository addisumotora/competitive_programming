#include <stdio.h>

#define N = 100
int count = 0

void producer(void){
    while(true){
        item = produce_items()
        if(count == N) sleep();
        insert_item(item);
        count = count + 1;
        if(count == 1) wakeup(consumer);
    }
}

void consumer(void){
    int item;
    while(true){
        if(count == 0) sleep();
        item = item_remove();
        count = count-1;
        if(count == N-1) wakeup(producer);
        consume_items(item);
    }
}