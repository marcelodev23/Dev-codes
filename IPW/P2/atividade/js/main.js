function questao01(lado) {
    console.log('---------------------');
    console.log('Questão 01');
    var  area_quadrado = lado ** 2;
    console.log('A área do quadrado é de '+area_quadrado+' cm²');
}

function questao02(lado) {
    console.log('---------------------');
    console.log('Questão 02');
    var  p = 4 * lado ;
    console.log('O perímetro do quadrado é de '+p+' m');
}

function questao03(base,altura) {
    console.log('---------------------');
    console.log('Questão 03');
    var perímetro = 2*(base+altura);
    console.log('O perímetro do retagulo é de '+perímetro+' m');
}

function questao04(base,altura) {
    console.log('---------------------');
    console.log('Questão 04');
    var área_retagulo = base * altura;
    console.log('O área do retagulo é de '+ área_retagulo+' cm²');
}

function questao05(quantidade) {
    console.log('---------------------');
    console.log('Questão 05');
    galinha = 2 * 4;
    dedos_galinha = quantidade * galinha
    console.log('Em galinheiro com ' + quantidade + ' galinhas tem ' + dedos_galinha + ' dedos de galinha.');
}

function questao06(numero_vacas) {
    console.log('---------------------');
    console.log('Questão 06');
    vaca = 4 * 5;
    quantidade_total = numero_vacas * vaca;
    console.log('Com ' + numero_vacas +' vacas tem a quantidade total ' + quantidade_total+' mL de leite');
}

function questao07(x,y) {
    console.log('---------------------');
    console.log('Questão 07');
    console.log(x);
    console.log(y);
    
    x = x+y;
    y = x-y;
    x = x-y;

    console.log(x)
    console.log(y);
}

function questao08(numero_vacas) {
    console.log('---------------------');
    console.log('Questão 08');
    vaca = 4 * 5;
    quantidade_total = numero_vacas * vaca;

    console.log('Com ' + numero_vacas +' vacas tem a quantidade total ' + quantidade_total+' mL de leite');
    console.log('Gera um total de ' + quantidade_total /2 +' garrafas de 2L.');
}

function questao09(numero_vacas) {
    console.log('---------------------');
    console.log('Questão 09');
    vaca = 4 * 5;
    quantidade_total = numero_vacas * vaca;
    garrafas = quantidade_total / 2;
    console.log('Com ' + numero_vacas +' vacas ');
    console.log('Gera uma quantidade total ' + quantidade_total+' mL de leite');
    console.log('Gera um total de ' + garrafas +' garrafas de 2L.');
    console.log('Gera um total de R$ ' + garrafas * 3 );
}

function questao10(numero_vacas) {
    console.log('---------------------');
    console.log('Questão 10');
    vaca = 4 * 5;
    quantidade_total = numero_vacas * vaca;
    garrafas = quantidade_total / 2;
    total_venda_garrafas = garrafas * 3 
    console.log('Com ' + numero_vacas +' vacas ');
    console.log('Gera uma quantidade total ' + quantidade_total+' mL de leite');
    console.log('Gera um total de ' + garrafas +' garrafas de 2L.');

    if (garrafas >= 10) {
        desconto = (total_venda_garrafas * 10)/100
        console.log('Gera um total de R$ ' + (total_venda_garrafas - desconto )+ ' com desconto de 10% ');
        console.log('Valor do desconto foi de R$ ' + desconto);
    }else{
        console.log('Gera um total de R$ ' + garrafas * 3 );
    }    
}

function questao11(peso,altura) {
    console.log('---------------------');
    console.log('Questão 11');
    //var peso = 55.00
    //var altura = 1.60  
    var imc = peso / (altura * altura)
    console.log('O valor do IMC é de ' + imc); 
}

function questao12(anterior,atual) {
    console.log('---------------------');
    console.log('Questão 12');
    Kwh = atual-anterior;
    valor_Kwh = Kwh * 0.809980;
    adic_B_vermelha = 21.52; 
    icms = valor_Kwh* 27/100;
    pis = valor_Kwh * 0.9912/100; 
    confins= valor_Kwh * 4.5657/100;
    ilum_publica = 15.78;
    juros_mora = 0.65;
    multa = 6.52;
    total_a_pagar =   valor_Kwh + adic_B_vermelha + ilum_publica + juros_mora + multa; 
    console.log('Consumo em Kwh: ' + Kwh); 
    console.log('Valor total R$ ',valor_Kwh);
    console.log('Valor ICMS(R$): ',icms);
    console.log('PIS(R$): ',pis);
    console.log('CONFINS(R$): ',confins);
    console.log('Lançamento e Servicos');
    console.log('Comtrib serv.Ilum.Publica',ilum_publica);
    console.log('Juros de mora : ',juros_mora);
    console.log('Multa : ',multa);
    console.log('Total a Pagar ',total_a_pagar);

}

questao01(6)
questao02(6)
questao03(7,3)
questao04(10,5)
questao05(2)
questao06(2)
questao07(16,24)
questao08(2)
questao09(2)
questao10(2)
questao11(55.24,1.60)
questao12(1944462,1944825)