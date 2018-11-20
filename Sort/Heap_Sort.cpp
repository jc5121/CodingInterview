#include <stdio.h>

/*/***************************************************************************
    * Helper functions for comparisons and swaps.
    * Indices are "off-by-one" to support 1-based indexing.
    * 为了更简便实现下沉操作，改进了比较函数和交换函数，支持从1开始的索引
    * 即堆的根节点是1而不是0 
	* 这样可以简便的从父节点算出两个子节点：k, 2k, 2k+1 
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

// 下沉操作，堆排序的基础，将k节点下沉至 
void sink(int* a, int k, int N)
{
	while(2*k <= N)
	{
		// k不可以为0，所以-1，改进swap 
		int j = 2*k;
		if(j < N && less(a, j, j+1)) j++;	// 两个子节点中那个更大 
		if(!less(a, k, j)) break;	// 满足条件，无需继续下沉了 
		swap(a, k, j);	//交换元素 
		k = j;
	}
} 

void sort(int* a ,int N)
{
	int n = N;
	// 构造阶段，构造出了堆，上大下小 
	for(int k = n/2; k >= 1; k--)
	{
		sink(a, k, n);
	}
	
	// 下沉排序 ，上小下大 
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
