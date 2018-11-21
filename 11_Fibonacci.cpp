#include <stdio.h>

int Fibonacci_Recursive(int n){
	if(n<=0)
		return 0;
	if(n == 1)
		return 1;
	
	return Fibonacci_Recursive(n-1) + Fibonacci_Recursive(n-2);
} 

int Fibonacci_Iterative(int n){
	if(n<=0)
		return 0;
	if(n == 1)
		return 1;
		
	int fibN = 0;
	int fibMinusOne = 1;
	int fibMinusTwo = 0;
	
	for(int i = 2; i<=n; i++){
		fibN = fibMinusOne + fibMinusTwo;
		fibMinusTwo = fibMinusOne;
		fibMinusOne = fibN;
	}
	
	return fibN;
}

int main(int argv, char** argc){
	printf("%d\n", Fibonacci_Recursive(4));
	printf("%d\n", Fibonacci_Iterative(4));
	
	return 0;
}
