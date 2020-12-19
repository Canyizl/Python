#include <iostream>
#include <string.h>
using namespace std;

int next[101];

void getNext(int* next,char* p){
	int i,n,k;
	
	n=strlen(p);
	next[1]=next[0]=0;
	k=0;
	for(i=2;i<=n;i++){
		for(;k!=0&&p[k]!=p[i-1];k=next[i]);
		if(p[k]==p[i-1])k++;
		next[i]=k;		
	}
}

void kmp(char* text,char* p,int* next)
{
	int len_t,len_p,s,q;
	len_t=strlen(text);
	len_p=strlen(p);
	q=s=0;
	// q��ʾ�ϴε���ƥ���˶����ַ���s��ʾ�����ַ��ĵڼ�λ��ʼ 
	while(s<len_t){
		for(q=next[q];q<len_p&&p[q]==text[s];q++,s++);
		if(q==0)s++;
		else if (q==len_p){
			cout<<"ƥ��ɹ�����ԭ�ĵĵ�"<<s-len_p+1<<"����ʼ��"<<endl; 
	//		q=0; ������Ϊ�����ص� 
		}
	}
}

int main()
{
	char p[]="cac";
	char text[]="cacaca";

	getNext(next,p);
	kmp(text,p,next);
	
	return 0;
}
