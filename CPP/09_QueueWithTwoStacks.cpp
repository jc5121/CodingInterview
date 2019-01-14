class Solution
{
public:
    void push(int node) {
        stack1.push(node);
    }
    int pop() {
        int top;
        if (stack1.empty() && stack2.empty())
            return 0;
        // stack2不为空时，直接返回 
        else if(!stack2.empty()){
            top = stack2.top();
            stack2.pop();
            return top;    
        }
        // stack2为空时，从stack1导入 
		else {
            while(!stack1.empty()){
				int temp = stack1.top();
				stack1.pop();
				stack2.push(temp);
				}
            top = stack2.top();  
            stack2.pop();
            return top;
        }
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};
