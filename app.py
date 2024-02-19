import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os


def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("WebP files", "*.webp")])
    if not file_paths:
        return
    save_pdf(file_paths)


def save_pdf(file_paths):
    images = [Image.open(x).convert("RGB") for x in file_paths]
    save_path = filedialog.asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]
    )
    if save_path:
        images[0].save(save_path, save_all=True, append_images=images[1:])
        tk.messagebox.showinfo("成功", "PDFファイルを保存しました。")


def main():
    root = tk.Tk()
    root.title("WebP to PDF Converter")
    root.geometry("300x150")

    select_button = tk.Button(
        root, text="WebPファイルを選択してPDFに変換", command=select_files
    )
    select_button.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
