// File: producer_consumer.c

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5
#define ITEMS 10

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;

// Semaphores
sem_t empty;
sem_t full;
sem_t mutex;

// Producer function
void* producer(void* arg)
{
    int item;

    for(int i = 1; i <= ITEMS; i++)
    {
        item = i;

        // Wait for empty space
        sem_wait(&empty);

        // Enter critical section
        sem_wait(&mutex);

        // Add item to buffer
        buffer[in] = item;
        printf("Producer produced item %d at position %d\n", item, in);

        in = (in + 1) % BUFFER_SIZE;

        // Exit critical section
        sem_post(&mutex);

        // Signal that buffer has full slot
        sem_post(&full);

        sleep(1);
    }

    pthread_exit(NULL);
}

// Consumer function
void* consumer(void* arg)
{
    int item;

    for(int i = 1; i <= ITEMS; i++)
    {
        // Wait for available item
        sem_wait(&full);

        // Enter critical section
        sem_wait(&mutex);

        // Remove item from buffer
        item = buffer[out];
        printf("Consumer consumed item %d from position %d\n", item, out);

        out = (out + 1) % BUFFER_SIZE;

        // Exit critical section
        sem_post(&mutex);

        // Signal empty slot available
        sem_post(&empty);

        sleep(2);
    }

    pthread_exit(NULL);
}

int main()
{
    pthread_t producerThread, consumerThread;

    // Initialize semaphores
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);
    sem_init(&mutex, 0, 1);

    // Create threads
    pthread_create(&producerThread, NULL, producer, NULL);
    pthread_create(&consumerThread, NULL, consumer, NULL);

    // Wait for threads to finish
    pthread_join(producerThread, NULL);
    pthread_join(consumerThread, NULL);

    // Destroy semaphores
    sem_destroy(&empty);
    sem_destroy(&full);
    sem_destroy(&mutex);

    printf("\nExecution completed successfully.\n");

    return 0;
}