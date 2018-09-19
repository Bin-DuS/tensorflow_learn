#include <stdlib.h>
#include "colin.h"
int func2(int a){
	return a * a;
}
int func3(y_t *p){
	int result;
	int sum;
	int i,j;
	result = 1;
	for(i = 0;i < p->len;i++){
		sum = 0;
		for(j = 0; j < p->ax[i].len;j++){
			sum += p->ax[i].a[j];
		}
		result *= sum;
	}
	return result;
}
void free_y_t(y_t *p){
	int i;
	for(i = 0;i < p->len;i++){
		free(p->ax[i].a);
	}
	free(p->ax);
}