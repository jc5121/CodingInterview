bool isSymmetrical(TreeNode* pRoot){
	return isSymmetrical(pRoot, pRoot);
}

bool isSymmetrical(TreeNode* pRoot1, TreeNode* pRoot2){
	if(pRoot1 == nullptr && pRoot2 == nullptr)
		return true;
	
	if(pRoot1 == nullptr || pRoot2 == nullptr)
		return false;
	
	if(pRoot1->val != pRoot2->val)
		return false;
		
	return isSymmetrical(pRoot1->left, pRoot2->right)
		&& isSymmetrical(pRoot2->left, pRoot1->right);
}
