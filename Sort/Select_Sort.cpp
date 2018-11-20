#include <stdio.h>

void swap(int* a, int i, int j){
	int temp = a[i];
	a [i] = a[j];
	a[j] = temp;
} 

// ѡ���������������
void select_sort(int* a, int N){
	if(a == nullptr || N <= 0)
		return;
		
	for(int i = 0; i < N; ++i){
		// �ź���Ĳ������һ��Ϊ��С�� 
		int min = i;
		for(int j = i + 1; j < N; ++j){
			if(a[j] < a[min])
				min = j;
		}
		swap(a, min, i);
	}
} 

int main(int argc, char** argv){
	int a[10] = {0, 4, 2, 5, 12, 23, 4, 3, 6, 1};
	select_sort(a, 10);
	for(int i = 0; i<10; i++)
		printf("%d\n", a[i]);
}
