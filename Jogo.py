from time import sleep

def introducao():
    direcoes = ["direita", "esquerda", "frente"]
    print("\nVocês entram na casa pelos fundos, depois de descer do telhado.")
    sleep(1)
    print("Sua família se separa em grupos, e você decide para onde quer ir.")
    sleep(1)
    print("Direita (cozinha)")
    print("Esquerda (quarto)")
    print("Frente (sala)\n")
    inputjogador = ""
    while inputjogador not in direcoes:
        inputjogador = input()
        if inputjogador == "direita":
            cozinha()
        elif inputjogador == "esquerda":
            quarto()
        elif inputjogador == "frente":
            sala()
        else:
            print("Por favor, digite uma opção válida.")
            inputjogador

def cozinha():
    direcoes = ["olhar", "voltar"]
    decisao = ["quarto", "sala"]
    print("\nVocê segue o corredor a frente e entra na cozinha, a direita.")
    sleep(1)
    print("A cozinha está limpa, tudo guardado no lugar certo.")
    sleep(1)
    print("Seus irmãos procuram por comida mas não encontram nada.")
    sleep(1)
    print("Você pode olhar em cima da geladeira.")
    sleep(1)
    print("Olhar")
    sleep(1)
    print("Voltar\n")
    inputjogador = ""
    while inputjogador not in direcoes:
        inputjogador = input()
        if inputjogador == "olhar":
            print("\nVocê segue o caminho, até o topo da geladeira.")
            sleep(1)
            print("Passa pela mesa, pelo fogão, mas não encontra nada.")
            sleep(1)
            print("\nVocê escala a geladeira, e quando finalmente alcança o topo...")
            sleep(1.9)
            print("você fica preso numa ratoeira.")
            sleep(1)
            print("O impacto foi tão forte que esmagou seus órgaos,")
            print("te oferecendo uma morte lenta e dolorosa.")
            sleep(1)
            print("Você morreu!")
            quit()
        elif inputjogador == "voltar":
            print("\nPara onde você quer ir?")
            sleep(1)
            print("Quarto")
            print("Sala\n")
            inputjogador = ""
            while inputjogador not in decisao:
                inputjogador = input()
                if inputjogador == "quarto":
                    quarto()
                elif inputjogador == "Sala":
                    sala()
        else:
            print("\nDigite uma opção válida.")
            inputjogador

def quarto():
    direcoes = ["sala", "quarto"]
    print("\nVocê entra no quarto e ele está vazio. Um rato mais velho te chama de volta.")
    sleep(1)
    print("Onde você deseja ir?")
    sleep(1)
    print("Sala")
    print("Cozinha\n")
    inputjogador = ""
    while inputjogador not in direcoes:
        inputjogador = input()
        if inputjogador == "sala":
            sala()
        elif inputjogador == "cozinha":
            cozinha()
        else:
            print("Digite uma opção válida.")
            inputjogador

def sala():
    direcoes = []
    print("""
          \nVocê corre o restante do corredor até a sala, e vê seus irmãos amarrando um senhor
          \nque estava dormindo. A mesa está cheia de comida e vocês fazem a festa!
          """)
    sleep(1)
    quit()


if __name__ == "__main__":
    while True:
        print("""
        \nVocê está correndo com sua família de ratos, no meio do telhado,
        \nprontos para invadir a casa de um humano.
        \nA outra família de ratos aguarda vocês, e vocês entram juntos na casa.
        \nQual seu nome?
        \n 
        """)
        name = input()
        sleep(1)
        print("\nBoa sorte, " + name + ".")
        sleep(1)
        introducao()
