#include <iostream>
#include <cmath>
using namespace std;

const int MAXN = 1e5+1;
char S[MAXN],T[MAXN];
int P[MAXN];

void manacher(char S[], int len)
{
	int k = 0;
	T[k++]='$',T[k++]='#';
	for(int i=0;i < len; i++)
	{
		T[k++]=S[i];
		T[k++]='#';
	}
	T[k]='0';
	
	int r=0,c=0;	//r����ǰ�ԳƵ���Զ���룬c����öԳƵ����� 
	for(int i = 0;i < k; i++)
	{
		int &p=P[i];
		p = r > i ? min(P[2*c-i],r-i) : 0; 		//P[2*c-i] --> �ԳƵ�x + i = 2*c �ԳƵ�����ΪP[2*c-i] 
		while(T[i+p+1]==T[i-p-1]) p++;
		if(i + p > r) {r = i + p; c = i;}		//���i+p>r �и������չ��Χ�����i��Ϊ�����ģ�rΪ�°뾶�� 
	}
	
/*	for(int i=0;i<k;i++)
	{
		cout<<P[i]<<' ';
	}   �������*/
	
	// ����ԭ�ַ����Ŀ�ͷ�±� = (i - P[i])  / 2  ֻҪ���� ��ͷ �� ��ͷ+P[i]-1 ֮����ַ��� 
 } 
 
int main()
{
	int n;
	cin>>n; 
	for(int i=0;i<n;i++)
	{
		cin>>S[i];
	}
	manacher(S,n);

	return 0;
} 
