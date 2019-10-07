#include <stdio.h>

void swap(int *a, int *b);
void sortByStep(int s[], int *begin, int step);

int len = 8;
void main() {
	int s[] = {93, 32, 14, 54, 22, 33, 84, 21};
	int step = len/2;
	while (step!=0) {
		for(int i=0; i<step; i++)
		{
			sortByStep(s, &(s[i]), step);
		}
		step /= 2;
	}

	printf("%d ", s[0]);
	printf("%d ", s[1]);
	printf("%d ", s[2]);
	printf("%d ", s[3]);
	printf("%d ", s[4]);
	printf("%d ", s[5]);
	printf("%d ", s[6]);
	printf("%d \n", s[7]);
}

void sortByStep(int s[], int *begin, int step)
{
	int *cur = begin;
	while (cur < s+len ) {
		int i = 1;
		while( cur+(i*step) < s+len ) {
			if( *cur > *(cur+(i*step)) ) {
				swap(cur, cur+(i*step));
			}

			i++;
		}

		cur+=step;
	}
}

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}
