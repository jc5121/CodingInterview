#include <stdio.h>
#include <math.h>
// 动态规划方法 
int maxProductAfterCutting_1(int length){
	// 由于至少要剪一次，所以1,2,3是特例，与后面products中的值不同 
	if(length < 2) return 0;
	if(length == 2) return 1;
	if(length == 3) return 2;
	
	// 多了个0，所以数组大小length+1 
	int* products = new int[length + 1];
	products[0] = 0;
	products[1] = 1;
	products[2] = 2;
	products[3] = 3;
	
	int max = 0;
	// 计算每一个数的f(n)，从4开始 
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

// 贪心算法，当绳子长度>5时减3，需要数学分析出2*2=4，是临界值,所以3越多越好，是为“贪心” 
maxProductAfterCutting_2(int length){
	if(length < 2) return 0;
	if(length == 2) return 1;
	if(length == 3) return 2;
	
	int numOf3 = length / 3;
	
	// 最后剩4的情况 
	if(length % 3 == 1){
		--numOf3;
		return pow(3, numOf3) * 4;
	}
	// 最后剩5 
	else if(length % 3 == 2){
		return pow(3, numOf3) * 2;
	} 
	// 正好
	else
		return pow(3, numOf3); 		
} 

int main(int argc, char** argv){
	printf("%d\n", maxProductAfterCutting_1(10));
	printf("%d\n", maxProductAfterCutting_2(10));
	return 0;
}
