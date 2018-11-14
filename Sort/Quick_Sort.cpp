#include <stdio.h>
 
void swap(int* a, int i, int j){
	int temp = a[i];
	a[i] = a[j];
	a[j] = temp;
}
// 切分操作 
int partition(int* a, int low, int high){
	int i = low;
	// 下面用的--j，必须这么写，改成j--不行 
	int j = high + 1;
	// 选最左为切分元素 
	int v = a[low];
	
	while(true){
		while(a[++i] < v) if(i == high) break;
		while(a[--j] > v) if(j == low) break; 
		if(i >= j) break;
		swap(a, i, j);
	}
	swap(a, low, j);
	
	return j;
} 
// high = n-1;
void sort(int* a,int low, int high){
	if(low >= high) return;
	int j = partition(a, low, high);
	sort(a, low, j-1);
	sort(a, j+1, high);
} 

int main(int argc, char** argv){
	int a[10] = {0, 4, 2, 5, 12, 23, 4, 3, 6, 1};
	sort(a, 0, 9);
	for(int i = 0; i<10; i++)
		printf("%d\n", a[i]);
}
