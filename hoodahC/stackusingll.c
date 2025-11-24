#include<stdio.h>
#include<stdlib.h>
#define maxsize 5
int count=0;
struct node
{
	int data;
	struct node *link;
};
struct node *top=NULL;

void push()
{	
	int item;
	if(count>maxsize-1)
	{
		printf("Stack overflow");
	}
	else
	{
		printf("Enter the item to be stored in the newnode");
	        scanf("%d",&item);
		struct node *newnode;
		newnode = (struct node *)malloc(sizeof(struct node));
		newnode->data = item;
		newnode->link = NULL;
		//make the created node as the first node
		if(top==NULL)
		{
			top=newnode;
			count+=1;
		}
		else
		{
			newnode->link=top;
			top=newnode;
			count+=1;	
		}
	} 
}

void traverseList()
{
	struct node *ptr;
	ptr=top;
	if(ptr==NULL)
	{
		printf("stack is empty");
	}
	else
	{
		while(ptr!=NULL)
		{
			printf("%d ",ptr->data);
			ptr=ptr->link;
		}
	}	  
	printf("\n");
}
void pop()
{
	struct node *ptr;
	ptr=top;
	if(top==NULL)
	{
		printf("List is empty therefore deletion is not possible");
	}
	else
	{
		printf("The item deleted is %d\n",ptr->data);
		top=top->link;
		free(ptr);
		count-=1;
	}
}
int main()
{
	int choice;
	do
	{
		printf("-------------------MENU----------------\n");
		printf("1.PUSH\n2.Display\n3.POP\n4.Exit\n");
		printf("enter your choice");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
				push();
				break;
			case 2:
				traverseList();
				break;
			case 3:
				pop();
				break;
			case 4:
				printf("exit\n");
				break;
			default:
				printf("invalid choice.try again\n");
		}
	}while(choice!=4);
	return 0;
}
