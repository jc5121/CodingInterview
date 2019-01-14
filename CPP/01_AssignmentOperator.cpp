#include<cstring>
#include<cstdio>
class CMyString
{
public:
	CMyString(char* pData = nullptr);
	CMyString(const CMyString& str);
	~CMyString(void);
	
	// 返回引用类型才可以连续赋值 
	CMyString& operator = (const CMyString& str);
	
	void Print();
private:
	char* m_pData;
};

CMyString::CMyString(char* pData)
{
	if(pData == nullptr)
	{
		m_pData = new char[1];
		m_pData = '\0';
	}
	else
	{
		int length = strlen(pData);
		m_pData = new char[length + 1];
		strcpy(m_pData, pData);
	}
}

CMyString::CMyString(const CMyString& str)
{
	int length = strlen(str.m_pData);
	m_pData = new char[length + 1];
	strcpy(m_pData, str.m_pData);
}

CMyString::~CMyString()
{
	delete []m_pData;
} 
void CMyString::Print()
{
	printf("%s", m_pData);
}

CMyString& CMyString::operator =(const CMyString& str) 
{
	if(this == &str)
		return *this;
	
	delete []m_pData;
	m_pData = nullptr;
	
	m_pData = new char[strlen(str.m_pData) + 1];
	strcpy(m_pData, str.m_pData);
	
	return *this;
}

int main(int argc, char** argv)
{
	char* text = "Hello offer!";
	CMyString str1(text);
	CMyString str2;
	str2 = str1;
	str2.Print();
	return 0;
}
