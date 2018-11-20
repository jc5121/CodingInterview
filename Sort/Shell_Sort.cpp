#include <stdio.h>

void swap(int* a, int i, int j){
	int temp = a[i];
	a [i] = a[j];
	a[j] = temp;
} 
// ϣ�����򣬸Ľ���Ĳ���������Ҫ��ȷ��h 
// ˼�룬���±�����������飬��ÿ����в�����������h��С��1ʱ���� 
void shell_sort(int* a ,int N)
	{
		if(a == nullptr || N <= 0)
		return;
		
		//�����������������ͳ��ѧ���ɵ��� 
		int h = 1;
		while(h < N/3) 
			h = 3*h + 1;//������ô���õģ� +1��Ϊ�˱�֤ h����ֵΪ 1 
			
		while(h >= 1)
		{
			for(int i = h;i<N;i++)
			{
				for(int j = i; (j>= h) && (a[j] < a[j-h]); j-=h)
				{
					// �߱Ƚϱ߽�����������h 
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
