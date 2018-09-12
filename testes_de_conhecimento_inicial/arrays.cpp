#include <iostream>
using namespace std;
#include <stdbool.h>

int main() {
	int quantA, quantB, kA, kB;
	int listaA[1000];
	int listaB[1000];
	bool ok = true;
	int aux1=0, aux2=0;
	cin>>quantA;
	cin>>quantB;
	cin>>kA;
	cin>>kB;
	
	for (int i=0;i<quantA;i++){
		cin>>listaA[i];
	}
	for (int i=0;i<quantB;i++){
		cin>>listaB[i];
	}
	
	while((aux1 < kA && aux2 < kB) || aux1 == 0){
		if(listaA[aux1] >= listaB[aux2]){
			ok = false;
		}
		if(aux1 == kA && aux2 < kB){
			aux2+=1;
			aux1=0;
		}
		aux1+=1;
	}
	if(ok){
		cout<<"YES";
	}
	else{
		cout<<"NO";
	}
}
