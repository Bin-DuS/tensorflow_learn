#ifndef __COLIN_H__
#define __COLIN_H__
typedef struct{
	int *a;
	int len;
}x_t;
typedef struct{
	x_t *ax;
	int len;
}y_t;
int func2(int a);
int func3(y_t *p);
void free_y_t(y_t *p);
#endif