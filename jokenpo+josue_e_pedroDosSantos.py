while True:

        #pontuacao
    ponto_pc = 0
    ponto_j = 0

    print ("=====================")
    print ("Olá, seja benvindo ao jokenpo!")
    print ("Para ganhar você precisará vencer 5 rodadas, o nosso esquema de pontos funciona da seguinte maneira:")
    print ("Vitória: 1 ponto \nEmpate: 0 pontos \nPara vencer a partida: 5 pontos")
    print ("=====================")
    print (f"Digite 0 para sair \nDigite 1 para começar")

    escolha = input("Digite aqui: ").strip()
    
    if escolha == "0":
        print ("Você saiu")
        break
    elif escolha == "1":  
        
        while ponto_j < 5 and ponto_pc <5:
            
            
            #escolha jogador
            print ("=====================")
            print ("Para começar escolha entre:")
            print ("Pedra = 1 \nPapel = 2 \nTesoura = 3")
            jogo = input("Digite aqui: ").strip()
            print ("=====================")
                


                #escolha pc
            import random 
            pc = random.randint(1,3)
                
                #jogo


                #empate
            if jogo == "1" and pc == 1:
                print ("Empate!")
                print ()
                print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
                continue
                
            if jogo == "2" and pc == 2:
                print ("Empate!")
                print ()
                print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
                continue
                
                
            if jogo == "3" and pc == 3:
                print ("Empate!")
                print ()
                print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
                continue

                #jogador ganha 
                
                
            elif jogo == "1" and pc == 3:
                print ("O jogador venceu a rodada!")    
                ponto_j += 1
                print ()
                print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
                continue 
                
            elif jogo == "2" and pc == 1:
                print ("O jogador venceu a rodada!")    
                ponto_j += 1
                print ()
                print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
                continue 
                
            elif jogo == "3" and pc == 2:
                print ("O jogador venceu a rodada!")    
                ponto_j += 1
                print ()
                print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
                continue 

                
                #pc ganha 

            elif pc == 1 and jogo == "3":
                print ("O computador venceu a rodada!")    
                ponto_pc += 1
                print ()
                print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
                continue 
                
            elif pc == 2 and jogo == "1":
                print ("O computador venceu a rodada!")    
                ponto_pc += 1
                print ()
                print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
                continue 
                
            elif pc == 3 and jogo == "2":
                print ("O computador venceu a rodada!")    
                ponto_pc += 1
                print ()
                print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
                continue 

                #escolha errada
                
            else:
                print ("Escolha umas das opções dadas, tente novamente")
                continue
            
        


        print ("==============")
        if ponto_j == 5:
            print ("Você ganhou!!")
        else:
            print ("O computador ganhou")
            
            
        print ("Você quer continuar jogando?")
        print ("Escolha 0 para sair \nEscolha 1 para continuar")
        fim = input("Sua escolha: ")
        
        if fim == "0":
            print ("Você saiu")
            break
        elif fim == "1":
            ("Vamos começar uma nova partida")
            continue
        else:
            print ("Escolha umas das opções dadas, tente novamente")
            continue


    else:
        print ("=====================")
        print ("Escolha umas das opções dadas, tente novamente")
        continue

