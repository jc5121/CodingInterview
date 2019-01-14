#include <stdio.h>
#include <math.h>
// ��̬�滮���� 
int maxProductAfterCutting_1(int length){
	// ��������Ҫ��һ�Σ�����1,2,3�������������products�е�ֵ��ͬ 
	if(length < 2) return 0;
	if(length == 2) return 1;
	if(length == 3) return 2;
	
	// ���˸�0�����������Сlength+1 
	int* products = new int[length + 1];
	products[0] = 0;
	products[1] = 1;
	products[2] = 2;
	products[3] = 3;
	
	int max = 0;
	// ����ÿһ������f(n)����4��ʼ 
	for(int i = 4; i <= length; ++i){
		max = 0;
		for(int j = 1; j <= i/2; ++j){
			int product = products[j] * products[i - j];
			if(max < product)
				max = product;
				
			products[i] = max;
		}
	}
	
	max = products[length];
	delete[] products;
	
	return max;
} 

// ̰���㷨�������ӳ���>5ʱ��3����Ҫ��ѧ������2*2=4�����ٽ�ֵ,����3Խ��Խ�ã���Ϊ��̰�ġ� 
maxProductAfterCutting_2(int length){
	if(length < 2) return 0;
	if(length == 2) return 1;
	if(length == 3) return 2;
	
	int numOf3 = length / 3;
	
	// ���ʣ4����� 
	if(length % 3 == 1){
		--numOf3;
		return pow(3, numOf3) * 4;
	}
	// ���ʣ5 
	else if(length % 3 == 2){
		return pow(3, numOf3) * 2;
	} 
	// ����
	else
		return pow(3, numOf3); 		
} 

int main(int argc, char** argv){
	printf("%d\n", maxProductAfterCutting_1(10));
	printf("%d\n", maxProductAfterCutting_2(10));
	return 0;
}
