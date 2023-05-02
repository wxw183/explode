#include<stdio.h>
#include<math.h>
#include<malloc.h>
#define tp 10000000
double t,ch1[tp],p;
int main(){
    FILE *fpi,*fpo;
    fpi=fopen("data.csv","r");
    long i,j;
    for(i=0;i<tp;i++){
        fscanf(fpi,"%g,%g,%g\n",&p,&ch1[i],&p);
    }
    long sample=1000;
    for(i=0;i<tp-sample;i++){
        p=0;
        for(j=0;j<sample;j++){
            p+=ch1[i+j];
        }
        p/=sample;
        p/=0.1539;
        ch1[i]=p;
    }
    fclose(fpi);
    fpi=fopen("data.csv","r");
    fpo=fopen("filted.csv","w");
    for(i=0;i<tp;i++){
        fscanf(fpi,"%g,%g,%g\n",&t,&p,&p);
        fprintf(fpo,"%g,%g,%g\n",t,ch1[i],ch1[i]);
        
    }
    fclose(fpi);
    fclose(fpo);
}