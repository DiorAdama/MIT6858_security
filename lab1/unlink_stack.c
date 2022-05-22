#include <unistd.h>


void func(char* s){
    s[0]+=1;
    s[2]+=1;
}

int main(){
    char* s = "/mnt/d/k2gilo/security_6858/lab/grades.txt";
    func(s);
    int a = 2*3;
    return 0;
}
