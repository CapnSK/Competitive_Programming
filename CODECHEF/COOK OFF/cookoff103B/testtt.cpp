#include<iostream>
#include<stdio.h>
#include<string.h>
int main()
{
char *p = "abcde";
printf("%lu %lu %lu",sizeof(p),strlen(p),sizeof("abcde"));
return 0;
}