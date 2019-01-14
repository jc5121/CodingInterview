
void Mirror(TreeNode *pRoot){
	if(pRoot == nullptr)
		return;
	if(pRoot->left == nullptr && pRoot->right == nullptr)
		return;
		
	TreeNode* pTemp = pRoot->left;
	pRoot->left = pRoot->right;
	pRoot->right = pTemp;
	
	if(pRoot->left)
		Mirror(pRoot->left);
	
	if(pRoot->right)
		Mirror(pRoot->right); 
}
