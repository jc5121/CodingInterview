#include <stdio.h>

void swap(int* a, int i, int j){
	int temp = a[i];
	a [i] = a[j];
	a[j] = temp;
} 

// 冒泡排序，蠢到我不好理解了，交换很多次 
void bubble_sort(int*a, int N){
	if(a == nullptr || N <= 0)
		return;
	// 将a[0...i]中最大的数据放在末尾
	for(int i = N - 1; i > 0; --i){
		for(int j = 0; j < i; ++j){
			if(a[j] > a[j + 1])
				swap(a, j, j+1);
		} 
	}
} 

int main(int argc, char** argv){
	int a[10] = {0, 4, 2, 5, 12, 23, 4, 3, 6, 1};
	bubble_sort(a, 10);
	for(int i = 0; i<10; i++)
		printf("%d\n", a[i]);
}
