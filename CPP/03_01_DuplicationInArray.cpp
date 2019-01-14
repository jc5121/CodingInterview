#include <cstdio>
#include <vector>
using namespace std;

int findDuplicate(vector<int>& nums) {
    vector<int> hash;
    
    hash.resize(nums.size());
    hash.assign(nums.size(),0);
	int duplication = -1;
	for(int i = 0; i<nums.size(); i++){
		hash[nums[i]]++;
	}
	
	for(int i = 0; i<hash.size(); i++){
		if(hash[i] > 1){
			duplication = i;
			break;
	}
	}
	
	return duplication;
}

int main(int argc, char** argv)
{
	vector<int> a = {2, 3, 1, 0, 2, 5, 3};
	int duplication = findDuplicate(a);
	
	printf("%d", duplication);
}
    
