 ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
    if(pListHead == nullptr || k == 0)
        return nullptr;
    
    ListNode* pFront = pListHead;
    ListNode* pBehind = pListHead;
    
    for(int i = 0; i<k-1; i++){
        if(pFront->next != nullptr){
             pFront = pFront -> next;
        }
        else
            return nullptr;
    }
    
    while(pFront->next != nullptr){
        pFront = pFront -> next;
        pBehind = pBehind -> next;
    }
    
    return pBehind;
}
