#include <iostream>

void ispis_liste(int lista[]){
    int k = sizeof(lista);
    for (int i = 0; i < k; i++){
        std::cout << lista[i] << " ";
    }
    std::cout<<std::endl;
}

void zamjena(int lista[],int a,int b){
    int x = lista[a];
    lista[a] = lista[b];
    lista[b] = x;
}

void okretanje_redoslijeda(int lista[]){
    int k = sizeof(lista);
    int pomocna_lista[k] = {};
    for (int i = 0; i < k; i++){
        pomocna_lista[i] = lista[k-i];
    }
    for (int i = 0; i < k; i++){
        lista[i] = pomocna_lista[i];
    }
}

int main(){
    int polje[15] = {11,-7,0,2,5,1,-3,-6,12,8,7,-2,4,6,-1};
    zamjena(polje,4,5);
    ispis_liste(polje);
    okretanje_redoslijeda(polje);
    ispis_liste(polje);
    return 0;
}