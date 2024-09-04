'''
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

3 operações: depósito, saque e extrato.

DEPOSITO
Deve ser possível depositar valores positivos para a minha conta bancária. 
A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

SAQUE
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

EXTRATO
Essa operação deve listar todos os depósitos e saques realizados na conta. 
No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45


'''
menu = '''
    [1] DEPOSITO
    [2] SAQUE
    [3] EXTRATO
    

    - O que vc deseja realizar? '''

total_in_account = 0
limite = 500
extrato = ''
saques = 0




var = True
while(var):
    ops = int(input(menu))
    
    if ops == 1:
        valor_deposito = int(input('Qual o valor vc deseja depositar?'))
        total_in_account += valor_deposito  
            
    elif ops == 2 :
        saques += 1
        valor_saque = int(input('Quanto deseja sacar?'))
        if saques == 3:
            print('Seu limite de saques, sao 3 por dia')
            var = False
        elif valor_saque <= 500 and total_in_account >= valor_saque:
            
            total_in_account -= valor_saque
        else:
            print(f'Voce nao tem o suficiente em conta ou execedeu o limite de saque diario \n EXTRATO: R${total_in_account:.2f}')

    elif ops == 3:
        print(f'O tatal que vc tem na conta e de R${total_in_account:.2f}')
        var = False
    else: 
        print('''
        DIGITE UM VALOR VALIDO 
        ''')

    










