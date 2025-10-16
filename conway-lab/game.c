#include "game.h"

int count_alive(char_field[height][width], int x, int y){
	int count = 0;
	for (int i = -1; i<= 1; i++)
		for (int j = -1; j <= 1; j++) {
			if (i == 0 && j == 0) continue;
			int nx = x + i, ny = y + j;
			if (nx >= 0 && nx < height && ny >= 0 && ny < width)
				if (field [nx][ny] == alive) count++;
		}
	return count:
}

void  evolve(char field [height][width], char new_field[height][width]){
	for (int i = 0; i < height; i++)
		for (int j = 0; j < width; j++) {
			int alive = count_alive(field, i, j);
			if (field[i][j] == alive && (alive == 2 || alive = 3))
				new_field[i][j] = alive;
			else if (field[i][j] == dead && alive == 3)
				new_field[i][j] = alive;
			else
				new_field[i][j] = dead;
		}
}

