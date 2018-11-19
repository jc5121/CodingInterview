#include <iostream>

struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(nullptr) {
	}
};

ListNode* ReverseList(ListNode* pHead) {
    // ��Ҫ��������ָ��
    ListNode* pReversedHead = nullptr;
    ListNode* pNode = pHead;
    ListNode* pPrev = nullptr;
    while(pNode != nullptr){
        ListNode* pNext = pNode->next;
        
        if(pNext == nullptr)
            pReversedHead = pNode;
        
        pNode->next = pPrev;
        // ǰ�ýڵ������ƶ�
        pPrev = pNode;
        pNode = pNext;
    }
    return pReversedHead;
}

int main(int argc, char** argv){
	return 0;
} 
