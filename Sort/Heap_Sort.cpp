#include <stdio.h>

/*/***************************************************************************
    * Helper functions for comparisons and swaps.
    * Indices are "off-by-one" to support 1-based indexing.
    * Ϊ�˸����ʵ���³��������Ľ��˱ȽϺ����ͽ���������֧�ִ�1��ʼ������
    * ���ѵĸ��ڵ���1������0 
	* �������Լ��ĴӸ��ڵ���������ӽڵ㣺k, 2k, 2k+1 
    ***************************************************************************/ 
    
bool less(int*a, int x, int y)
{
	return a[x-1] <= a[y-1];
}

void swap(int* a, int i, int j)
{
	int temp = a[i-1];
	a [i-1] = a[j-1];
	a[j-1] = temp;
}

// �³�������������Ļ�������k�ڵ��³��� 
void sink(int* a, int k, int N)
{
	while(2*k <= N)
	{
		// k������Ϊ0������-1���Ľ�swap 
		int j = 2*k;
		if(j < N && less(a, j, j+1)) j++;	// �����ӽڵ����Ǹ����� 
		if(!less(a, k, j)) break;	// ������������������³��� 
		swap(a, k, j);	//����Ԫ�� 
		k = j;
	}
} 

void sort(int* a ,int N)
{
	int n = N;
	// ����׶Σ�������˶ѣ��ϴ���С 
	for(int k = n/2; k >= 1; k--)
	{
		sink(a, k, n);
	}
	
	// �³����� ����С�´� 
	while(n > 1)
	{
		swap(a, 1, n--);
		sink(a, 1, n);
	}
}

int main(int argc, char** argv){
	int a[10] = {0, 4, 2, 5, 12, 23, 4, 3, 6, 1};
	sort(a, 10);
	for(int i = 0; i<10; i++)
		printf("%d\n", a[i]);
} 
