#include <stdio.h>

#define N=100;
typedef int semaphores;
semaphores mutex = 1;
semaphores full = 0;
semaphores empty = N;

void producer(void){
    int item;
    while(true){
        item = produce_items();
        down($mutex);
        down($empty);
        insert_item(item);
        up($mutex);
        up($full);
    }
}
void consumer(void){
    int item;
    while(true){
        item = item_remove();
        down(mutex);
        down(full);
        up(mutex);
        up(empty);
        consume_items(item);
    }
}