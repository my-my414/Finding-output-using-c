#include<stdio.h>
int main()
{
    int m=10;
    int n=6;
    n=m++ + ++m;
    printf("%d %d",m,n);
}
