#include <stdio.h>
// �������� auxiliary 
void merge(int* a, int low, int mid, int high, int* aux){
	int i = low;
	int j = mid + 1;
	
	// �������������� 
	for(int k = low; k <= high; k++)
		aux[k] = a[k];
		
	// �ع� 
	for(int k = low; k <= high; k++){
		// ������þ�ʱֱ�Ӹ�����һ�� 
		if(i > mid) a[k] = aux[j++];
		else if(j > high) a[k] = aux[i++];
		// �ҵ��Ƚ�С�ģ���aux�бȣ����� 
		else if(aux[j] < aux[i]) a[k] = aux[j++];
		else a[k] = aux[i++];
	} 
} 
// �Զ����£��ݹ飻����Ե����ϾͲ��õݹ��� 
void sort(int* a, int low, int high, int* aux){
	if(high <= low) return;

	int mid = low + (high - low) / 2;
	sort(a, low, mid, aux);
	sort(a, mid+1, high, aux);
	merge(a, low, mid, high, aux);
}

int main(int argc, char** argv){
	int a[13] = {0, 4, 2, 5, 12, 23, 4, 3, 6, 1, 10, 11, 15};
	int aux[13];
	// high = n - 1 
	sort(a, 0, 12, aux);
	for(int i = 0; i<13; i++)
		printf("%d\n", a[i]);
}
