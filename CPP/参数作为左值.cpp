#include <stdio.h>

void test1(int* p)
{
	int a = 1;
	p = &a;
}

void test2(int** p)
{
	int a = 1;
	*p = &a; 
}

void test3(int a)
{
	a = 2;
}

void test4(int& a)
{
	a = 2;
}

int main(int argc, char** argv)
{
	int* p1 = nullptr;
	test1(p1);
	if(p1 == nullptr)
		printf("%s\n", "p1 is still nullptr.");
	else
		printf("%d", *p1);
	
	
	int* p3 = nullptr;
	// int** p2 = &p3; 不需要这个p2,在传参数时取地址就可以了&p3 
	test2(&p3);
	if( p3== nullptr)
		printf("%s\n", "*p2 is still nullptr.");
	else
		printf("%d\n", *p3);
		
	int a = 0;
	test3(a);
	printf("%d\n", a);
	
	test4(a);
	printf("%d\n", a);
	
	// output:nullptr, 1, 0, 2
	return 0;
 } 
