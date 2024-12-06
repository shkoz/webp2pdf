import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


# メッセージの定義
MESSAGES = {
    "success": "PDFファイルを保存しました。",
    "error": "PDF作成中にエラーが発生しました: {error}",
    "select_button": "WebPファイルを選択してPDFに変換",
    "window_title": "WebP to PDF Converter",
}


# 画像ファイルを開いてPillowオブジェクトに変換
def open_images(file_paths):
    images = []
    for path in file_paths:
        img = Image.open(path).convert("RGB")
        images.append(img)
    return images


# 画像をPDFとして保存
def save_images_as_pdf(images):
    save_path = filedialog.asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]
    )
    if save_path:
        images[0].save(save_path, save_all=True, append_images=images[1:])
        messagebox.showinfo("成功", MESSAGES["success"])


# メインの処理
def save_pdf(file_paths):
    images = []
    try:
        images = open_images(file_paths)
        save_images_as_pdf(images)
    except Exception as e:
        messagebox.showerror("エラー", MESSAGES["error"].format(error=str(e)))
    finally:
        for img in images:
            img.close()


# ファイル選択ダイアログを表示
def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("WebP files", "*.webp")])
    if file_paths:
        save_pdf(file_paths)


# メインウィンドウの作成
def main():
    root = tk.Tk()
    root.title(MESSAGES["window_title"])
    root.geometry("400x200")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    select_button = tk.Button(
        frame, text=MESSAGES["select_button"], command=select_files, width=30, height=2
    )
    select_button.grid(row=0, column=0, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
