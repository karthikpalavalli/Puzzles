#include<iostream>

using namespace std;

class Solution 
{
	public:
    		int hammingDistance(int x, int y) 
    		{
        		int x_xor_y = x xor y;
			int count = 0;

			while(x_xor_y)
			{
				x_xor_y = x_xor_y & (x_xor_y-1);
				count++;
			}
			return count;
    		}
};


int main()
{
	int num_a, num_b;
	cin>>num_a>>num_b;
	Solution hamming_solution;
	cout<<hamming_solution.hammingDistance(num_a, num_b);
	return 0;
}


