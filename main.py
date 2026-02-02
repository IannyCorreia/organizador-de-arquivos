import os
from tkinter.filedialog import askdirectory
caminho = askdirectory(title= "Selecione uma pasta")
listaArquivos = os.listdir(caminho)
print(listaArquivos)
locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx"],
    "PDFs": [".pdf"],
    "videos": [".mp4"],
    "docs": [".docx"],
    "slides": [".odp", ".pptx"],
    "outros": []
}
for arquivo in listaArquivos:
        origem = os.path.join(caminho, arquivo) 
        if not os.path.isfile(origem):
            continue

        nome, extensao = os.path.splitext(f"{arquivo}")
        extensao = extensao.lower()

        movido = False

        for pasta,extensoes in locais.items():
              if pasta != "outros" and extensao in extensoes:
                    destinoPasta = os.path.join(caminho, pasta)

                    if not os.path.exists(destinoPasta):
                        os.mkdir(destinoPasta)
                    
                    destino = os.path.join(destinoPasta, arquivo)

                    if os.path.exists(destino):
                        os.remove(destino)

                    os.rename(origem, destino)
                    movido = True
                    break
        if not movido:
              destinoPasta = os.path.join(caminho, "outros")
              
              if not os.path.exists(destinoPasta):
                    os.mkdir(destinoPasta)
              
              destino = os.path.join(destinoPasta, arquivo)
              if os.path.exists(destino):
                    os.remove(destino)
              os.rename(origem, destino)

              
        
            