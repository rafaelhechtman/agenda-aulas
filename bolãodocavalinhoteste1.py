import tkinter as tk
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.title("Exemplo de Carregamento de Imagem")

    # Caminho das imagens (ajuste conforme o nome das suas imagens)
    img_path_fluminense = "Fluminense.png"
    img_path_flamengo = "Flamengo.png"

    try:
        # Abrir imagens
        img_fluminense = Image.open(img_path_fluminense)
        img_flamengo = Image.open(img_path_flamengo)

        # Exibir imagens
        img_tk_fluminense = ImageTk.PhotoImage(img_fluminense)
        img_tk_flamengo = ImageTk.PhotoImage(img_flamengo)

        # Label para exibir imagens do Fluminense
        label_fluminense = tk.Label(root, text="Fluminense", image=img_tk_fluminense)
        label_fluminense.pack(padx=10, pady=10)

        # Label para exibir imagens do Flamengo
        label_flamengo = tk.Label(root, text="Flamengo", image=img_tk_flamengo)
        label_flamengo.pack(padx=10, pady=10)

        root.mainloop()
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
