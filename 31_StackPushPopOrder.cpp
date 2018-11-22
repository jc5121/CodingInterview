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
		// ���������б�����ʱ��ѭ�������� 
		while(j < nLength){
			// ջΪ�ջ�ջ��Ԫ�ز����ڵ���Ԫ��ʱ����ѹ��������ջѹ�� 
			while(stackData.empty() || stackData.top() != popV[j]){
				if(i > nLength - 1)
					break;
				else{
					stackData.push(pushV[i]);
					++i;
				}
			
			}
			//  ��ʱѹ������Ϊ�գ�����@��@��ȣ����ѹ������û����ȵģ�˵����ƥ�� 
			if(stackData.top() != popV[j]) 
				break;
			else{
				// �����ʱ������ 
				stackData.pop();
				++j;
			}
			
		}
		
		// ��ѭ��������ǡ��ջΪ�գ�˵����������ƥ�� 
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
