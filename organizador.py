import os

""" Bibilioteca para abir pop up importando apenas a função """
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma pasta')

""" Pega todos os arquivos que estão no caminho passado """
listaArq = os.listdir(caminho)


locais = {
    "imagens": [".png",".jpg",".jpeg"],
    "planilhas": [".xls"],
    "programas": [".exe"],
    "PDFs": [".pdf"],
}

for arq in listaArq:
    """ pegar extensao do arquivo """
    nome, extensao = os.path.splitext(f"{caminho}/{arq}")
    
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arq}", f"{caminho}/{pasta}/{arq}")
""" print(listaArq) """