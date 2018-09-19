#include <stdio.h>
#include <stdlib.h>
int main(int argc,char **argv){
	FILE *f;
	char s[1024];
	int ret;
	f = popen("python test.py 99","r");
	while((ret=fread(s,1,1024,f)) > 0){
		fwrite(s,1,ret,stdout);
	}
	pclose(f);
	f = NULL;
	return 0;
}