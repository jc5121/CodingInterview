#include <iostream>

struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(nullptr) {
	}
};

ListNode* ReverseList(ListNode* pHead) {
    // 需要定义三个指针
    ListNode* pReversedHead = nullptr;
    ListNode* pNode = pHead;
    ListNode* pPrev = nullptr;
    while(pNode != nullptr){
        ListNode* pNext = pNode->next;
        
        if(pNext == nullptr)
            pReversedHead = pNode;
        
        pNode->next = pPrev;
        // 前置节点向右移动
        pPrev = pNode;
        pNode = pNext;
    }
    return pReversedHead;
}

int main(int argc, char** argv){
	return 0;
} 
