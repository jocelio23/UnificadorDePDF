##importa bibliotecas para funções do pdf e de entrada de arquvivos

import PyPDF2
import os
#chamada de função de unir
merger = PyPDF2.PdfMerger()

#listando arquivos para unir
lista_de_arquivos = os.listdir("arquivos")

#colocando arquivos em ordem de nome
lista_de_arquivos.sort()

for arquivo in lista_de_arquivos:
    if(".pdf" in arquivo):
        merger.append(f"arquivos/{arquivo}")
        print({arquivo})

merger.write("PDF_mesclado.pdf")
