#include <stdio.h>

void swap(int* a, int i, int j){
	int temp = a[i];
	a [i] = a[j];
	a[j] = temp;
} 
// 希尔排序，改进后的插入排序，主要是确定h 
// 思想，按下标进行增量分组，对每组进行插入排序，增量h缩小至1时结束 
void shell_sort(int* a ,int N)
	{
		if(a == nullptr || N <= 0)
		return;
		
		//设置增量，这个基于统计学，可调整 
		int h = 1;
		while(h < N/3) 
			h = 3*h + 1;//这是怎么设置的？ +1是为了保证 h最后的值为 1 
			
		while(h >= 1)
		{
			for(int i = h;i<N;i++)
			{
				for(int j = i; (j>= h) && (a[j] < a[j-h]); j-=h)
				{
					// 边比较边交换，这里是h 
					swap(a, j, j-h);
				}
			}
			h = h/3;
		}
		
	}
	
int main(int argc, char** argv){
	int a[10] = {0, 4, 2, 5, 12, 23, 4, 3, 6, 1};
	shell_sort(a, 10);
	for(int i = 0; i<10; i++)
		printf("%d\n", a[i]);
}
