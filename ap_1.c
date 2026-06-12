#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int constantTime(int arr[])
{
    return arr[0];
}

int linearSearch(int arr[], int n, int key)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

void bubbleSort(int arr[], int n)
{
    int temp;

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void fillArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        arr[i] = rand() % 10000;
    }
}

int main()
{
    int n;
    clock_t start, end;
    double time_taken;

    printf("Enter size of array (n): ");
    scanf("%d", &n);

    if (n <= 0)
    {
        printf("Invalid array size\n");
        return 0;
    }

    int *arr = (int *)malloc(n * sizeof(int));

    if (arr == NULL)
    {
        printf("Memory allocation failed\n");
        return 0;
    }

    srand(time(NULL));

    fillArray(arr, n);

    start = clock();
    int value = constantTime(arr);
    end = clock();

    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("\nO(1) Constant Time:");
    printf("\nFirst Element = %d", value);
    printf("\nTime Taken = %lf seconds\n", time_taken);

    int key = arr[n / 2];

    start = clock();
    int index = linearSearch(arr, n, key);
    end = clock();

    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("\nO(n) Linear Time (Linear Search):");
    printf("\nElement Found at Index = %d", index);
    printf("\nTime Taken = %lf seconds\n", time_taken);

    start = clock();
    bubbleSort(arr, n);
    end = clock();

    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("\nO(n^2) Quadratic Time (Bubble Sort):");
    printf("\nTime Taken = %lf seconds\n", time_taken);

    free(arr);

    return 0;
}
