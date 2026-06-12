#include <stdio.h>
#include <stdlib.h>


void constantSpace(int n)
{
    int x = n;
    int y = x * 2;
    int z = x + y;

    int space = sizeof(x) + sizeof(y) + sizeof(z);

    printf("Constant Space Result: %d\n", z);
    printf("Constant Space Occupied: %d bytes\n", space);
}


void linearSpace(int n)
{
    int *arr;

    arr = (int *)malloc(n * sizeof(int));

    for(int i = 0; i < n; i++)
    {
        arr[i] = i;
    }

    int space = n * sizeof(int);

    printf("Linear Space Last Element: %d\n", arr[n-1]);
    printf("Linear Space Occupied: %d bytes\n", space);

    free(arr);
}


void quadraticSpace(int n)
{
    int **matrix;

    matrix = (int **)malloc(n * sizeof(int *));

    for(int i = 0; i < n; i++)
    {
        matrix[i] = (int *)malloc(n * sizeof(int));
    }

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            matrix[i][j] = i + j;
        }
    }

    int space = n * n * sizeof(int);

    printf("Quadratic Space Last Element: %d\n", matrix[n-1][n-1]);
    printf("Quadratic Space Occupied: %d bytes\n", space);

    for(int i = 0; i < n; i++)
    {
        free(matrix[i]);
    }

    free(matrix);
}


int main()
{
    int n;

    printf("Enter input size: ");
    scanf("%d", &n);

    printf("\n--- Constant Space O(1) ---\n");
    constantSpace(n);

    printf("\n--- Linear Space O(n) ---\n");
    linearSpace(n);

    printf("\n--- Quadratic Space O(n^2) ---\n");
    quadraticSpace(n);

    return 0;
}
