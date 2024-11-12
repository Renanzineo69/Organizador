import os
import shutil

def organizar_arquivos(diretorio_nome):
    # Obtém o diretório do usuário
    diretorio_origem1 = os.path.expanduser("~")
    diretorio_origem = os.path.join(diretorio_origem1, diretorio_nome)
    
    # Verifica se o diretório de origem existe
    if not os.path.exists(diretorio_origem):
        print("O diretório de origem não existe.")
        return

    # Loop por todos os arquivos no diretório
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)

        # Verifica se é um arquivo (e não uma pasta)
        if os.path.isfile(caminho_arquivo):
            # Obtém a extensão do arquivo
            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao.lstrip('.')  # Remove o ponto

            # Cria um diretório para a extensão, se não existir
            diretorio_destino = os.path.join(diretorio_origem, extensao)
            os.makedirs(diretorio_destino, exist_ok=True)

            # Define o caminho completo para o arquivo no diretório de destino
            destino_arquivo = os.path.join(diretorio_destino, arquivo)

            # Se o arquivo já existir, incrementa o nome com um sufixo
            contador = 1
            while os.path.exists(destino_arquivo):
                # Gera um novo nome com o contador
                novo_nome = f"{nome} ({contador}){os.path.splitext(arquivo)[1]}"
                destino_arquivo = os.path.join(diretorio_destino, novo_nome)
                contador += 1

            # Move o arquivo para o diretório correspondente com o novo nome
            shutil.move(caminho_arquivo, destino_arquivo)

    print("Arquivos organizados com sucesso!")

# Apenas especifique o nome do diretório do qual deseja organizar
organizar_arquivos('Downloads')
