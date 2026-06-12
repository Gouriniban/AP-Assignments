#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *data;
    size_t length;
    size_t capacity;
} StringBuffer;

/* Function to initialize the StringBuffer */
StringBuffer* sb_init(size_t initial_capacity) {
    StringBuffer *sb = (StringBuffer *)malloc(sizeof(StringBuffer));

    if (sb == NULL) {
        printf("Memory allocation failed for StringBuffer.\n");
        return NULL;
    }

    sb->data = (char *)malloc(initial_capacity * sizeof(char));

    if (sb->data == NULL) {
        printf("Memory allocation failed for data buffer.\n");
        free(sb);
        return NULL;
    }

    sb->length = 0;
    sb->capacity = initial_capacity;

    sb->data[0] = '\0';   // Initialize as empty string

    return sb;
}

/* Function to append a string */
void sb_append(StringBuffer *sb, const char *str) {
    size_t str_len = strlen(str);

    /* Check if capacity is enough */
    while (sb->length + str_len + 1 > sb->capacity) {

        size_t new_capacity = sb->capacity * 2;

        /* Safe realloc */
        char *temp = (char *)realloc(sb->data, new_capacity);

        if (temp == NULL) {
            printf("Reallocation failed.\n");
            return;
        }

        sb->data = temp;
        sb->capacity = new_capacity;

        printf("Buffer grown to capacity: %zu\n", sb->capacity);
    }

    /* Append new string */
    strcpy(sb->data + sb->length, str);

    sb->length += str_len;
}

/* Destructor function */
void sb_free(StringBuffer *sb) {
    if (sb != NULL) {
        free(sb->data);
        free(sb);
    }
}

int main() {
    /* Initialize buffer with small capacity */
    StringBuffer *sb = sb_init(8);

    if (sb == NULL) {
        return 1;
    }

    printf("Initial Capacity: %zu\n", sb->capacity);

    /* Append strings */
    sb_append(sb, "Hello");
    printf("String: %s\n", sb->data);

    sb_append(sb, ", ");
    printf("String: %s\n", sb->data);

    sb_append(sb, "World!");
    printf("String: %s\n", sb->data);

    sb_append(sb, " This is a dynamic string buffer example.");
    printf("String: %s\n", sb->data);

    printf("\nFinal String: %s\n", sb->data);
    printf("Final Length: %zu\n", sb->length);
    printf("Final Capacity: %zu\n", sb->capacity);

    /* Free memory */
    sb_free(sb);

    printf("\nMemory freed successfully.\n");

    return 0;
}