#include <stdio.h>

void swap(int* a, int i, int j){
	int temp = a[i];
	a [i] = a[j];
	a[j] = temp;
} 

// 插入排序, 第二好理解的 
void insert_sort(int*a, int N){
	if(a == nullptr || N <= 0)
		return;
	
	for(int i = 1; i < N; ++i){
		for(int j = i; (j > 0) && (a[j] < a[j-1]); --j) //边比较边交换 
			swap(a, j, j-1);
	}
} 

int main(int argc, char** argv){
	int a[10] = {0, 4, 2, 5, 12, 23, 4, 3, 6, 1};
	insert_sort(a, 10);
	for(int i = 0; i<10; i++)
		printf("%d\n", a[i]);
}
