####################################################################################################################################################################################
#                                                                                                                                                                                  #
#                                                                                                                                                                                  #
#                                                                      Urna eletronica escrita em python                                                                           #
#                                                                   Trabalho de Laboratório de Programação                                                                         #
#                                                                       TUTOR: LAZARO NOGUEIRA PENA NETO                                                                           #
#                                                                           Aluno: Túlio S Marinho                                                                                 #
#                                                                      Universidade: Universidade de Uberaba                                                                       #
#                                                                                                                                                                                  #
#                                                                                                                                                                                  #
####################################################################################################################################################################################

#Aninhamento de dicionários de códigos e nomes dos candidatos
#Cadda código é uma chave que identifica seus respectivos dicionários
candidatos = {
    1 : {"nome": "Jamil Messala", "votos": 0},
    2 : {"nome": "Lúcio Polvo Silvério", "votos": 0}, 
    3 : {"nome": "Rômulo Zemo", "votos": 0}, 
    4 : {"nome": "Cícero Moges", "votos": 0}, 
    5 : {"nome": "Nulo", "votos": 0}, 
    6 : {"nome": "Branco", "votos": 0}
    }

#Função para apresentação dos nomes e códigos dos candidatos
def apresentarCandidatos():
    print("\nLista de canditados e seus respectivos códigos:")
    print("-"*50)
    for codigo in candidatos:
        nome = candidatos[codigo]["nome"]
        print(f"Código do candidato {codigo} | nome: {nome}")
    print("="*50)

#Função para atribuição do voto ao candidato e verificação da escolha
def urna():
    while True:
        entrada = input("Digite o número do candidato que deseja votar ou L para listar os canditados e seus respectivos códigos: ").strip().upper()
        
        if entrada == "L":
            apresentarCandidatos()
            continue

        try:
            voto = int(entrada)
        #Tratamento de excessão: caso o usuário digite um valor ou caractere inválido
        except ValueError:
             print("Entrada inválida. Digite um número ou.")
             continue
        
        #Confirmação da escolha do eleitor
        if voto in candidatos:
                print(f"Seu voto é para: {candidatos[voto]['nome']}")
                confirma = str(input("Digite S para sim e confirmar, ou N para cancelar e escolher o candidato novamente: ")).strip().upper()

                if confirma == "S":
                    candidatos[voto]["votos"] +=1
                    print("--- VOTO CONFIRMADO ---")
                    return voto

                elif confirma == "N":
                    print("Voto cancelado. Tente novamente.")
                    continue

                else:
                    print("Opção inválida. Por favor escola S para confirmar ou N para cancelar")
                    continue
        else:
                print("Código inválido. Tente novamente.")

numeroEleitores = 10
eleitores = 0
print("\n"+"="*33)
print("--- URNA ELETRONICA EM PYTHON ---")
print("Desenvolvido por: Túlio S Marinho")
print("="*33)

print(f"\nlIniciando votação para {numeroEleitores} eleitores")

while eleitores < numeroEleitores:
     print(f"--- {eleitores + 1} de {numeroEleitores} ---")
     votoRealizado = urna()
     eleitores +=1

print("\n" + "="*30)
print("Resultado da Eleição:")
print("="*30)

#Loop de apresentação e apuração dos votos
for codigo in candidatos:
    nome = candidatos[codigo] ["nome"]
    votos = candidatos[codigo] ["votos"]
    print(f"{nome}: {votos} votos")
    print("-"*30)

#verificação de candidato vencedor
candidatoVencedor = None
maiorVotos = -1

for codigo, dados in candidatos.items():
    votos = dados["votos"]
    nome = dados["nome"]
    
    if votos > maiorVotos:
        maiorVotos = votos
        candidatoVencedor = nome

# Exibe o resultado
print("-" * 30)
print("RESULTADO FINAL")
print("-" * 30)

if candidatoVencedor:
    if maiorVotos == 0:
        print("Nenhum voto foi registrado.")
    else:
        print(f"Candidato Vencedor: {candidatoVencedor}")
        print(f"Total de votos: {maiorVotos}")
        
        #Verificação de empates
        empatados = []
        for codigo, dados in candidatos.items():
            if dados["votos"] == maiorVotos and dados["nome"] != candidatoVencedor:
                empatados.append(dados["nome"])
        
        if empatados:
            print(f"Atenção: Empate com: {', '.join(empatados)}. Esses candidatos deverão seguir para o segundo turno")
else:
    print("Nenhum candidato foi identificado.")

#Condicional para cálculo da porcentagem de votos brancos e nulos. Evitando divisão por zero
if candidatos[5]["votos"] > 0 or candidatos[6]["votos"] > 0:
    porcentagemNulos = candidatos[5]["votos"] / numeroEleitores * 100
    porcentagemBrancos = candidatos[6]["votos"] / numeroEleitores * 100
    print(f"A porcentagem de votos nulos foi de: {porcentagemNulos}%")
    print(f"A porcentagem de votos em branco foi de: {porcentagemBrancos}%")

else:
    print("A porcentagem de votos brancos e nulos foi de: 0%")



