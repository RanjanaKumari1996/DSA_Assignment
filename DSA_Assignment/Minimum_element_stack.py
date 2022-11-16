 C
 C++
 Java
#include <stdio.h>
int main()
{
    int q;
    scanf("%d",&q);
    int stack[q],stackmin[q];
    int top=-1,topmin=-1;
    while(q--)
    {
        int x;scanf("%d",&x);
        if(x==1)
        {
            int y;scanf("%d",&y);
            stack[++top]=y;
            if(topmin==-1)
              stackmin[++topmin]=y;
            else if(y<=stackmin[topmin])
                stackmin[++topmin]=y;
        }
        else if(x==2)
        {
            if(top==-1)
                printf("-1\n");
            else
            {
                if(stack[top]==stackmin[topmin])
                    topmin--;
                //printf("%d\n",stack[top]);
                top--;}
        }
        else if(x==3)
        {
            if(top==-1)
                printf("-1\n");
            else
                printf("%d\n",stack[top]);}
            else
            {
                if(top==-1)
                    printf("-1\n");
                else
                    printf("%d\n",stackmin[topmin]);}
    }
    return 0;
