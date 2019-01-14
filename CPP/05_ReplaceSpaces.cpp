#include <cstdio>
void replaceSpace(char *str,int length) {
	
	if(str == nullptr || length <= 0)
		return;
		
	int numberOfBlank = 0;
	int originalLength = 0;
	int i = 0;
	while(str[i] != '\0'){
		originalLength++;
		
		if(str[i] == ' ')
			numberOfBlank++;
			
		i++;
	}
	
	int newLength = originalLength + numberOfBlank * 2;
	if(newLength > length)
		return;
		
	int indexOfOriginal = originalLength;
	int indexOfNew = newLength;
	
	while(indexOfOriginal >= 0 && indexOfNew > indexOfOriginal){
		if(str[indexOfOriginal] == ' '){
			str[indexOfNew--] = '0';
			str[indexOfNew--] = '2';
			str[indexOfNew--] = '%';
		}
		else{
			str[indexOfNew--] = str[indexOfOriginal];
		}
		
		indexOfOriginal--;
	}
}

int main(int argc, char** argv){
	// 50Îª×ÜÈÝÁ¿ 
	char str[50] = "We are one big family.";
	printf("%s\n", str);
	replaceSpace(str, 50);
	printf("%s", str);
	return 0;
}
