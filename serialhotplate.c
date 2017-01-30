#include <stdio.h>

#define ROWS 	8192
#define COLUMNS 8192


void initHotplate(float array[ROWS][COLUMNS]){
	// top row, leftmost column, rightmost column: 0 degrees
	// row 400, columns 0 thru 330: 100 degrees
	// array[200][500] = 100 degrees
	// bottom row: 100 degrees

	// ALL OTHER CELLS: 50 degrees

	for(int row = 0; row < ROWS; row++){
		for(int col = 0; col < COLUMNS; col++){
			// leftmost or rightmost column
			if(row == 0 || col == 0 || col == (COLUMNS-1))
				array[row][col] == 0;

			else if(row == (ROWS-1)								// bottom row
					|| (row == 400 && col >= 0 && col <= 330)	// array[400][0->330]
					|| (row == 200 && col == 500))				// array[200][500]
				array[row][col] = 100;

			else
				array[row][col] = 50;
		}
	}
}


void computeSteadyState(float t[ROWS][COLUMNS]){
	unsigned counter = 0;
	float t_minus_1[ROWS][COLUMNS] = t;
	print(t_minus_1);
	for(int row = 0; row < ROWS; row++){
		for(int col = 0; col < COLUMNS; col++){
			t[row][col] = (t)/8;
		}
		counter++;	
	}
}


void print(float array[ROWS][COLUMNS]){
 	for(int row = 0; row < ROWS; row++){
 		printf("hotplate[%d]:,", row);
	 	for(int col = 0; col < COLUMNS; col++){
	 		printf("%0.1f,", array[row][col]);	
	 	} 
	 	printf("\n");
 	}
}


int main(){

    // Create hotplate 2d array; hotplate[row][column]
    static float hotplate[ROWS][COLUMNS];
    initHotplate(hotplate);
    computeSteadyState(hotplate);
    // print(hotplate);
 }
