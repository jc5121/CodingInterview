#include <stdio.h>
 
void swap(int* a, int i, int j){
	int temp = a[i];
	a[i] = a[j];
	a[j] = temp;
}
// �зֲ��� 
int partition(int* a, int low, int high){
	int i = low;
	// �����õ�--j��������ôд���ĳ�j--���� 
	int j = high + 1;
	// ѡ����Ϊ�з�Ԫ�� 
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
