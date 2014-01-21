#include <stdio.h>
#include <string.h>
/**
* Command line code to verify if a string or number is a palindrome
* @antiadriano 2014 
**/

#include <ctype.h>

#define swap(a, b) a ^= b, b ^= a, a ^= b

char * strCheck(char * s){
   char * b = s;
   char * e = s + strlen(s) - 1;

   if(*e == '\n')
      --e;

   for(; e > b; --e, ++b){
      if(*e ^ *b)
         return "Not a palindrome\n";
   }
   
   return "Is a palindrome\n";
}

char * setLower(char * s){
   for(;*s;++s)
      *s = tolower(*s);
   return s;
}

int main(int argc, char *argv[]){
   char buf[512];
   scanf("%s", buf);

   setLower(buf);

   printf("%s", strCheck(buf));
   return 0;
}
