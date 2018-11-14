#include <stdio.h>
// 辅助数组 auxiliary 
void merge(int* a, int low, int mid, int high, int* aux){
	int i = low;
	int j = mid + 1;
	
	// 复制至辅助数组 
	for(int k = low; k <= high; k++)
		aux[k] = a[k];
		
	// 回归 
	for(int k = low; k <= high; k++){
		// 左或右用尽时直接复制另一边 
		if(i > mid) a[k] = aux[j++];
		else if(j > high) a[k] = aux[i++];
		// 找到比较小的，在aux中比！！！ 
		else if(aux[j] < aux[i]) a[k] = aux[j++];
		else a[k] = aux[i++];
	} 
} 
// 自顶向下，递归；如果自底向上就不用递归了 
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
