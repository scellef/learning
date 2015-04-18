#include <ncurses.h>
#include <unistd.h>
#include <stdlib.h>

typedef struct {
	WINDOW * win;
	int height;
	int width;
	int posy;
	int posx;
} windowbox;

int main() {

	intscr();
	start_color();
	cbreak();
	noecho();
	curs_set(0);

	init_pair(1,COLOR_BLACK,COLOR_WHITE);
	init_pair(2,COLOR_WHITE,COLOR_BLACK);

	wbkdg(stdscr,COLOR_PAIR(1));

	mvprintw(1,8,"HI I'm %s.","el_seano");

	refresh();

	windowbox main;
	main.height = LINES - 6;
	main.width = COLS - 12;
	main.posy = (LINES - main.height) / 2;
	main.posx = (COLS - main.width) / 2 ;
	main.win = newwin(main.height, main.width, main.posy, main.posx);
	wbkgd(main.win,COLOR_PAIR(2));

	
	mvprintw(3,8,"HI I'm %s.","el_seano");

	getch();

	endwin();
	return 0;
}
