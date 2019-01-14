int TreeDepth(TreeNode* pRoot)
{
    if(pRoot == nullptr)
        return 0;
    
    int nLeft = TreeDepth(pRoot -> left);
    int nRight = TreeDepth(pRoot -> right);
    
    return (nLeft > nRight)?(nLeft + 1) : (nRight + 1);
}

