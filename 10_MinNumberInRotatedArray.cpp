#include <stdio.h>
#include <vector>
using namespace std;

int minNumberInRotateArray(vector<int> rotateArray) {
	if(rotateArray.empty())
		return -1;
	
	int start = 0;
	int end = rotateArray.size() - 1;
	int mid = start;
	
	
	
	while(rotateArray[start] >= rotateArray[end])
	{
		if(end - start == 1){
			mid = end;
			break;
		}
		mid = (start + end)/2;
		// 当3个位置相等时，只能用顺序排序了，这在每一次迭代中都有可能发生 
		if(rotateArray[start] == rotateArray[end] && rotateArray[mid] == rotateArray[start]){
			int min = rotateArray[0];
			for(int i = 0; i<rotateArray.size(); i++){
				if(min > rotateArray[i])
					min = rotateArray[i];
		}
		
		return min;
	}    
		if(rotateArray[mid] >= rotateArray[end])
			start = mid;
		else if(rotateArray[mid] <= rotateArray[end])
			end = mid;
	}
	
	return rotateArray[mid];
}
    
int main(int argv, char** argc){
	vector<int> a = {5, 6, 7, 8, 9, 1, 2, 3, 4};
	int min = minNumberInRotateArray(a);
	printf("%d\n", min);
}
