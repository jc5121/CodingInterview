#include <stdio.h>
#include <vector>
#include <stack>

using namespace std;

bool IsPopOrder(vector<int> pushV,vector<int> popV){
	
	bool bPossible = false;
	int nLength = pushV.size();
	
	if(!pushV.empty() && !popV.empty() && pushV.size() == popV.size()){
		stack<int> stackData;
		int i = 0;
		int j = 0;
		// 当弹出序列遍历完时，循环结束， 
		while(j < nLength){
			// 栈为空或栈顶元素不等于弹出元素时，从压入序列向栈压入 
			while(stackData.empty() || stackData.top() != popV[j]){
				if(i > nLength - 1)
					break;
				else{
					stackData.push(pushV[i]);
					++i;
				}
			
			}
			//  此时压入序列为空，或者@与@相等，如果压完了仍没有相等的，说明不匹配 
			if(stackData.top() != popV[j]) 
				break;
			else{
				// （相等时，弹出 
				stackData.pop();
				++j;
			}
			
		}
		
		// 主循环结束，恰好栈为空，说明弹出序列匹配 
		if(stackData.empty() && j == nLength)
			bPossible = true;
		
	}
	
	return bPossible;
}

int main(int argc, char** argv){
	vector<int> pushV = {1, 2, 3, 4, 5};
	vector<int> popV1 = {4, 5, 3, 2, 1}; // yes
	vector<int> popV2 = {4, 3, 5, 1, 2}; // no 
	
	printf("%d\n", IsPopOrder(pushV, popV1));
	printf("%d\n", IsPopOrder(pushV, popV2));
	return 0;
}
