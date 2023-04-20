import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64

root = tk.Tk()
root.title("Program Enkripsi & Dekripsi")


# fungsi untuk mengecek apakah kunci yang dimasukkan benar
def cek_kunci():
    string_kunci = entry_kunci.get().encode('utf-8')
    tambalan_kunci = string_kunci.ljust(32, b'\0')
    kunci = base64.urlsafe_b64encode(tambalan_kunci)
    fernet = Fernet(kunci)
    try:
        fernet.encrypt(b'Tes pesan')  # mencoba melakukan enkripsi
        return True
    except:
        return False


# fungsi untuk melakukan enkripsi
def enkripsi():
    if cek_kunci():
        pesan = entry_pesan.get()
        string_kunci = entry_kunci.get().encode('utf-8')
        tambalan_kunci = string_kunci.ljust(32, b'\0')
        kunci = base64.urlsafe_b64encode(tambalan_kunci)
        fernet = Fernet(kunci)
        enkripsi_pesan = fernet.encrypt(pesan.encode('utf-8'))
        output.config(state='normal')
        output.delete(1.0, tk.END)
        output.insert(tk.END, "Text yang dimasukkan: " + pesan + '\n')
        output.insert(tk.END, "Text yang sudah dienkripsi: " + str(enkripsi_pesan.decode('utf-8')) + '\n')
        output.config(state='disabled')
    else:
        messagebox.showerror("Kunci Salah", "Kunci yang dimasukkan salah! Silahkan coba kembali.")


# fungsi untuk melakukan dekripsi
def dekripsi():
    if cek_kunci():
        pesan = entry_pesan.get()
        string_kunci = entry_kunci.get().encode('utf-8')
        tambalan_kunci = string_kunci.ljust(32, b'\0')
        kunci = base64.urlsafe_b64encode(tambalan_kunci)
        fernet = Fernet(kunci)
        try:
            dekripsi_pesan = fernet.decrypt(pesan.encode('utf-8')).decode('utf-8')
            output.config(state='normal')
            output.delete(1.0, tk.END)
            output.insert(tk.END, "Text yang dimasukkan: " + pesan + '\n')
            output.insert(tk.END, "Text yang sudah didekripsi: " + dekripsi_pesan + '\n')
            output.config(state='disabled')
        except:
            messagebox.showerror("Text dengan Kunci Tidak Cocok",
                                 "Text atau kunci yang dimasukkan salah! Silahkan coba kembali.")
    else:
        messagebox.showerror("Kunci Salah", "Kunci yang dimasukkan salah! Silahkan coba kembali.")


# fungsi untuk keluar dari program
def keluar():
    root.destroy()


# membuat widget
label_pesan = tk.Label(root, text="Masukkan text:")
label_pesan.pack(pady=5)

entry_pesan = tk.Entry(root, width=70)
entry_pesan.pack(pady=5)

label_kunci = tk.Label(root, text="Masukkan kunci:")
label_kunci.pack(pady=5)

entry_kunci = tk.Entry(root, width=50, show="*")
entry_kunci.pack(pady=5)

button_enkripsi = tk.Button(root, text="Enkripsi", command=enkripsi)
button_enkripsi.pack(pady=5)

button_dekripsi = tk.Button(root, text="Dekripsi", command=dekripsi)
button_dekripsi.pack(pady=5)

button_keluar = tk.Button(root, text="Keluar", command=keluar)
button_keluar.pack(pady=5)

output_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
output_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

output_scrollbar = tk.Scrollbar(output_frame)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output = tk.Text(output_frame, yscrollcommand=output_scrollbar.set)
output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

output_scrollbar.config(command=output.yview)

root.mainloop()
