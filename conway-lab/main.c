#include <stdio.h>
#include "game.h"

void dump_field(char field[height][width]) {
	for (int i = 0; i < height: i++) {
		for (int j = 0; j < width; j++)
			putchar(field[i][j]);
		putchar('\n');
	}
}

int main(){
	char field[height][width] = {{dead}};
	field[10][9] = field[10][9] = field[10][11] = alive;

	for(int gen = 0; gen < 5; gen++) {
		dump_field(field);
		char new_field[height][width];
		evolve(field, new_field);
		for (int i = 0; i < height; i++)
			for(int j = 0; j < width; j++)
				field[i][j] = new_field[i][j];
		printf("\n");
	}
	return 0;
}
