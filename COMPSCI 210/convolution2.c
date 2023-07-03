#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    FILE *file1, *file2, *file3;
    int i = 0;
    int filter[5][5];
    int** data;
    int** rlt;
    int j, k, l, m;
    int val;
    int iter;

    if (argc < 5) {
        printf("Usage: ./convolution2 data1.txt filter1.txt temp111 1\n");
        return 1;
    }
    file1 = fopen(argv[1], "r");
    file2 = fopen(argv[2], "r");
    if ((file1 == NULL) || (file2 == NULL)) {
        printf("Error: Files cannot open\n");
        return 1;
    }
    iter = atoi(argv[4]);
    if (iter == 0) {
        printf("Error: Invalid iteration\n");
        return 1;
    } 
    file3 = fopen(argv[3], "w");
    data = (int**) malloc(sizeof(int*) * 1024);
    rlt = (int**) malloc(sizeof(int*) * 1024);
    for (i = 0; i < 1024; i++) {
        data[i] = (int*) malloc(sizeof(int) * 1024);
        rlt[i] = (int*) malloc(sizeof(int) * 1024);
    }

    i = 0;
    do {
        j = 0;
        do {
            if (j == 1023) {
                fscanf(file1, "%d\n", &val);
                data[i][j] = val;
            }
            else {
                fscanf(file1, "%d,", &val);
                data[i][j] = val;
            }
            j = j + 1;
        } while (j < 1024);
        i = i + 1;
    } while (i < 1024);

    i = 0;
    do {
        int j = 0;
        do {
            if (j == 4) {
                fscanf(file2, "%d\n", &val);
                filter[i][j] = val;
            }
            else {
                fscanf(file2, "%d,", &val);
                filter[i][j] = val;
            }
            j = j + 1;
        } while (j < 5);
        i = i + 1;
    } while (i < 5);


    // Perform the convolution operation
    for (int itr = 0; itr < iter; itr++) {
        for (i = 0; i < 1024; i++) {
            for (j = 0; j < 1024; j++) {
                int sum = 0;

                // Apply the filter to the current element
                for (k = -2; k <= 2; k++) {
                    for (l = -2; l <= 2; l++) {
                        int x_index = i + k;
                        int y_index = j + l;

                        // Check boundaries to avoid accessing out-of-bounds indices
                        if (x_index >= 0 && x_index < 1024 && y_index >= 0 && y_index < 1024) {
                            int x_val = data[x_index][y_index];
                            int h_val = filter[2 - k][2 - l];
                            sum += x_val * h_val;
                        }
                    }
                }

                // Scale down the value by dividing by a scaling factor (adjust as needed)
                sum /= 16;

                // Saturate the value to keep it within the range of -16 to 16
                if (sum < -16)
                    sum = -16;
                else if (sum > 16)
                    sum = 16;

                // Store the result in the rlt matrix for the next iteration
                rlt[i][j] = sum;
            }
        }

        // Update the data array with the new values for the next iteration
        for (i = 0; i < 1024; i++) {
            for (j = 0; j < 1024; j++) {
                data[i][j] = rlt[i][j];
            }
        }
    }

    // Write the result to the output file
    for (i = 0; i < 1024; i++) {
        for (j = 0; j < 1024; j++) {
            fprintf(file3, "%d ", rlt[i][j]);
        }
        fprintf(file3, "\n");
    }

    // Free the allocated memory
    for (i = 0; i < 1024; i++) {
        free(data[i]);
        free(rlt[i]);
    }
    free(data);
    free(rlt);

    // Close the files
    fclose(file1);
    fclose(file2);
    fclose(file3);

    return 0;
}
