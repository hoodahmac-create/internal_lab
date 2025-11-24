#include<stdio.h>
char uni[26]=
{'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char s1[26],s2[26];
int bit1[26],bit2[26],result[26];
void initialize()
{
	for(int i=0;i<26;i++)
	{
		bit1[i]=0;
		bit2[i]=0;
		result[i]=0;
	}
}
void bitvector(char arr[],int n,int b1[])
{
	for(int i=0;i<26;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(uni[i]==arr[j])
			{
				b1[i]=1;
				break;
			}
	        }
	}
}
void union_set(int bit1[26],int bit2[26])
{
	for(int i=0;i<26;i++)
	{
		result[i]=bit1[i]|bit2[i];
	}
}
void setIntersection(int bit1[26], int bit2[26], int result[26])
{
	for(int i=0;i<26;i++)
	{
		result[i]=bit1[i]&bit2[i];
	}
}
void setComplement(int bit[26], int result[26])
{
	for(int i=0;i<26;i++)
	{
		if(bit[i]==1)
			result[i]=0;
		else
			result[i]=1;
	}
}
void difference(int bit1[26],int bit2[26])
{	
	int diff[26];
	int res[26];
	setComplement(bit2,diff);
	setIntersection(bit1,diff,res);
	for(int i=0;i<26;i++)
	{
		printf(" %d",res[i]);
	}
	printf("\n");
}
void printresult(int res[26])
{
	for(int i=0;i<26;i++)
	{
		printf(" %d",res[i]);
	}
	printf("\n");
}
int main()
{
	int n,n1;
	//inputing first array
	printf("how many elements");
	scanf("%d",&n);
	printf("enter the elemnets for set1");
	for(int i=0;i<n;i++)
	{
		scanf(" %c",&s1[i]);
	}
	//inputing scnd array
	printf("how many elements");
	scanf("%d",&n1);
	printf("enter the elemnets for set2");
	for(int i=0;i<n1;i++)
	{
		scanf(" %c",&s2[i]);
	}
	//initializing and calling func to make the but vectors
	initialize();
	bitvector(s1,n,bit1);
	bitvector(s2,n1,bit2);
	//printing the butvectors of the sets
	printf("The bit vectors are:\n");
	for(int i=0;i<26;i++)
	{
		printf(" %d",bit1[i]);
	}
	printf("\n");
	for(int i=0;i<26;i++)
	{
		printf(" %d",bit2[i]);
	}
	printf("\n");
	printf("UNION\n");
	union_set(bit1,bit2);
	printresult(result);
	printf("INTERSECTION\n");
	setIntersection(bit1,bit2,result);
	printresult(result);
	printf("SET COMPLEMENT\n");
	setComplement(bit1,result);
	printresult(result);
	setComplement(bit2,result);
	printresult(result);
	printf("SET DIFFERENCE\n");
	difference(bit1,bit2);
	

}
