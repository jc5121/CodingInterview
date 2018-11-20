#include <stdio.h>
#include <algorithm> // for abs(), fags()

double PowerWithUnsignedExponent(double base, int exponent){
	double result = 1.0;
	for(int i = 1; i <= exponent; ++i){
		result *= base;
	}
	return result;
}

bool g_InvalidInput = false;
 
double Power(double base, int exponent){
	g_InvalidInput = false;
	
	// 0的非正数次方无意义 
	if((fabs(base-0.0) < 0.000001) && (exponent <= 0)){
		g_InvalidInput = true;
		return 0.0;
	}
	
	//处理负数次方 
	int absExponent = abs(exponent);

	double result = PowerWithUnsignedExponent(base, absExponent);
	if(exponent < 0)
		result = 1.0 / result;
		
	return result;
}


int main(int argc, char** argv){
	printf("%f\n", Power(5.2, 5));
	printf("%f\n", Power(5.2, -5));
	printf("%f\n", Power(0, 1));
	printf("%f\n", Power(0, -2));
	return 0;
} 
