#include <iostream>
#include <stdio.h>
#include <queue>
#include <vector>
#include <string.h>
using namespace std;

const int INF=0x3f3f3f3f;
const int MAXN=100001;

struct qnode{
	int v,c;					//v������㣬c����ǰ·���� 
	qnode(int _v=0,int _c=0):v(_v),c(_c){}
	bool operator < (const qnode &r) const	//�������������ȶ��� 
	{
		return c>r.c;
	}
};

struct Edge{           	//�ڽӾ��� 
	int v,cost;			//v����ָ��ĵ㣬cost����·�� 
	Edge(int _v=0,int _cost=0):v(_v),cost(_cost){}
};
vector<Edge> E[MAXN];		//E[i][j]�����iָ��j��E[i][j].costΪ���߼�·���� E[i][j].v����ָ��ĵ�j�� 

bool vis[MAXN];			//�Ƿ���ʱ�־ 
int dist[MAXN];			//��ž���,��㵽ÿ�������̾��� 

void Dijkstra(int n,int start) 			//nΪ��������startΪѡȡ����� 
{
	memset(vis,false,sizeof(vis));
	for(int i=1;i<=n;i++)
		dist[i]=INF;
	priority_queue<qnode> que;
	while(!que.empty()) que.pop();
	dist[start]=0;
	que.push(qnode(start,0));
	qnode tmp;
	while(!que.empty())
	{
		tmp=que.top();
		que.pop();
		int u=tmp.v;				//uΪ��ǰ������Ϊ��� 
		if(vis[u]) continue;
		vis[u]=true;
		for(int i=0;i<E[u].size();i++)		//E[u].size()�ȼ��ڽڵ��� 
		{
			int v=E[u][i].v;				//vΪָ�����һ���ڵ� 
			int cost=E[u][i].cost;			//costΪ��ǰ���u��Ŀ���v����֪���� 
			if(!vis[v]&&dist[v]>cost+dist[u])		//�Ƚ����ֱ�ӵ�v�㣬���ȵ�u���ٵ�v���·�� 
			{
				dist[v]=dist[u]+cost;
				que.push(qnode(v,dist[v]));			///��Ŀ���������У�������һ���ɳ� 
			}
		}
	}
}

void addedge(int u,int v,int w)  			//���ڳ�ʼ���ڽӾ��� 
{
	E[u].push_back(Edge(v,w));
}

int main()
{
	/*  2 
	P1--->P3 
 1	��     ��4
	P2--->P4 
	   4
	*/ 
	
	int n=4;
	int v,w;
	freopen("in.txt","r",stdin); //��������ֱ���in.txt��out.txt�У� 
	freopen("out.txt","w",stdout);
	for(int i=1;i<=n;i++)
	{
		addedge(i,0,-1);		//ʹ�ÿ�ʼ��Ϊ1��������0�� 
		for(int j=1;j<=n;j++)
		{
			cin>>w;
			if(w==-1)			//������-1���� 
				addedge(i,j,INF); 
			else
				addedge(i,j,w);
		} 
	}
	
/*	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=n;j++)
		{
			cout<<E[i][j].cost<<' ';
		} 
		cout<<endl;
	}*/
	
	Dijkstra(4,1);
	for(int i=1;i<=4;i++)
		cout<<dist[i]<<' '; 
	return 0;
} 

/*
	in.txt:	0 1 2 -1
			1 0 -1 4
			2 -1 0 4
			-1 4 4 0   
			
	out.txt��׼�𰸣� 0 1 2 5 
*/
