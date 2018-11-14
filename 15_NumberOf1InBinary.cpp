#include <stdio.h>

int NumberOf1(int n){
    int count = 0;
    unsigned int flag = 1;
    while(flag){
    	if(n & flag)
    		count++;
    	flag = flag << 1;
	}
	return count;
} 

int NumberOf1_2(int n){
	int count = 0;
	while(n){
		n = (n - 1) & n;
		count++;
	}
	
	return count;
}
int main(int argc, char** argv){
	printf("%d \n", NumberOf1(1994));
	
	printf("%d \n", NumberOf1_2(1994));
	
	return 0;
}
