#include <stdio.h>
 
struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x), next(nullptr){  // 用构造函数而不用new运算符 
	}
}; 

void printListFromTailToHead(ListNode* head) {
	if(head != nullptr){
		if(head -> next != nullptr){
			printListFromTailToHead(head->next);
		}	
		printf("%d\n", head->val);
	}        
}
int main(int argc, char** argv)
{
	ListNode* head = nullptr;
	ListNode* pNode = nullptr;
	ListNode* pNew = nullptr;
	for(int i = 0; i<10; i++){
		pNew = new ListNode(i); // 还是要new.. 
		if(head == nullptr){
			pNode = pNew;
			head = pNode;
		}	
		else{
			pNode->next = pNew;
			pNode = pNode->next;
		}
	}
	pNode = head;
	while(pNode->next != nullptr){
		printf("%d\n", pNode->val);
		pNode = pNode->next;
		if(pNode->next == nullptr)
			printf("%d\n", pNode->val);
	}
	printf("%s\n", "Reversed Order:");
	printListFromTailToHead(head);
	return 0;
}
