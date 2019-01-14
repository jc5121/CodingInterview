#include<cstdio> 
class Singleton
{
public:
	static Singleton* getInstance();
private:
	Singleton();
	static Singleton* instance;
};

Singleton::Singleton(){
	
}

// have to initialize here
Singleton* Singleton::instance = new Singleton();
Singleton* Singleton::getInstance(){
	return instance;
}

int main(int argc, char** argv)
{
	Singleton* instance1 = Singleton::getInstance();
	Singleton* instance2 = Singleton::getInstance();
	
	if(instance1 != instance2)
		printf("%s", "????");
	else
		printf("%s\n", "yeap!");
	
	return 0;
}
