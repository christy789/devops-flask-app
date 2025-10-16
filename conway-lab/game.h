#ifndef GAME_H
#define GAME_H

#define width 20
#define height 20 
#define alive 'O'
#define dead '.'

int count_alive(char field[height][width], int x, int y);
void evolve (char field [height][width], char new_field [height][width]);

#endif

