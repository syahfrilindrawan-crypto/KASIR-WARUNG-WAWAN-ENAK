import tkinter as tk
from tkinter import messagebox
import json
import os

file_akun = "akun.json"

if not os.path.exists(file_akun):
    with open(file_akun, "w") as file:
        json.dump({"admin":"123"}, file)

def load_akun():
    with open(file_akun, "r") as file:
        return json.load(file)

def save_json(data):
    with open(file_akun, "w") as file:
        json.dump(data, file)
#-------------------- DATA MENU -------------

menu = {
    "Lele Goreng + Nasi": 12000,
    "Ayam Goreng + Nasi": 18000,
    "Ayam Goreng + Nasi": 18000,
    "Bebek Goreng + Nasi": 20000,
    "Tempe Tahu + Nasi": 8000,
    "Es Teh": 3000,
    "Teh Hangat": 3000,
    "Jeruk Hangat": 3000,
    "Es Jeruk": 3000,
    "Bebek": 18000,
    "Ayam": 16000,
    "Lele": 10000,
    "Sate Usus": 4000
}

pesanankamu = []
totalharga = 0


#-------------- LOGIN -------------
def cek_login():
    akun = load_akun()
    user = entry_user.get()
    pw = entry_pw.get()

    if user in akun and akun[user] == pw:
        messagebox.showinfo("Login Success", "Berhasil Login!!!")
        login_window.destroy()
        buka_kasir(user)
    else:
        messagebox.showerror("Login Failed", "Gagal Login!!!")

def register():
    akun = load_akun()
    user = entry_user.get()
    pw = entry_pw.get()

    if user in akun:
        messagebox.showerror("Error", "User sudah ada")
    else:
        akun[user] = pw
        save_json(akun)
        messagebox.showinfo("Sukses", "Akun dibuat")

#--------- kasir ----------------

def inputpesanan(pilihan):
    global totalharga
    try:
        harga = menu[pilihan]
        jumlah = int(entryjumlah.get())
        subtotal = harga * jumlah

        pesanankamu.append([pilihan, harga,jumlah,subtotal])
        totalharga += subtotal
        boxpesan.insert(tk.END, f"{pilihan} x{jumlah} = Rp{subtotal}")
        labeltotal.config(text=f"Total: Rp{totalharga}")

    except:
        messagebox.showerror("Error", "Input salah")

def hapus():
    global totalharga
    try:
        i = boxpesan.curselection()[0]
        totalharga -= pesanankamu[i][3]
        pesanankamu.pop(i)
        boxpesan.delete(i)
        labeltotal.config(text=f"Total: Rp{totalharga}")
    except:
        messagebox.showerror("Error", "Pilih Dulu")

def cetak(user):
    if not pesanankamu:
        return

    with open("nota.txt", "w") as f:
        f.write("WARUNG WAWAN ENAK\n")
        f.write("Kasir: " + user + "\n")
        f.write("="*30 + "\n")

        for i, item in enumerate(pesanankamu):
            f.write(f"{i+1}. {item[0]} x{item[2]} = {item[3]}\n")

        f.write("="*30 + "\n")
        f.write(f"Total: Rp{totalharga}\n")

    messagebox.showinfo("Sukses", "Nota dibuat")

def buka_kasir(user):
    global entryjumlah, boxpesan, totalharga, labeltotal

    root = tk.Tk()
    root.title("KASIR WARUNG WAWAN ENAK (WWE)")
    root.geometry("700x750")



    tk.Label(root, text=f"KASIR\n ===== WARUNG WAWAN ENAK (WWE) ====\n").pack()

    tk.Label(root, text=f"Login sebagai: {user}", fg="green").pack()

    frame = tk.Frame(root)
    frame.pack()

    for i, (nama, harga) in enumerate(menu.items()):
        tk.Button(frame, text=f"{nama}\nRp{harga}",
                  command=lambda n=nama: inputpesanan(n), width=15).grid(row=i // 3, column=i % 3,pady=5, padx=5)

    tk.Label(root, text="JUMLAH", font=("Calibri",12,"bold")).pack(pady=10)
    entryjumlah = tk.Entry(root)
    entryjumlah.insert(0, "1")
    entryjumlah.pack(pady=10)

    tk.Label(root, text="PESANAN KAMU", font=("Calibri", 12, "bold")).pack(pady=10)

    boxpesan = tk.Listbox(root,width=40, height=10)
    boxpesan.pack()

    labeltotal = tk.Label(root, text="Total: Rp0")
    labeltotal.pack()

    tk.Button(root, text="Hapus", command=hapus,bg="red",font=12).pack(pady=10)
    tk.Button(root, text="Cetak Nota", command=lambda: cetak(user), bg = "green",font=12).pack()

    root.mainloop()


# ================= UI LOGIN =================
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window, text="LOGIN",font=("Times new roman",12,"bold")).pack()

frame_login = tk.Frame(login_window)
frame_login.pack()

tk.Label(frame_login,text="USERNAME").grid(row=0,column=0, padx=5,pady=5)
entry_user = tk.Entry(frame_login)
entry_user.grid(row=0, column=1,padx=10, pady=10)



tk.Label(frame_login,text="PASSWORD").grid(row=1,column=0, padx=5,pady=5)
entry_pw = tk.Entry(frame_login, show="*")
entry_pw.grid(row=1, column=1,padx=10, pady=10)

tk.Button(login_window, text="Login", command=cek_login).pack(pady=5)
tk.Button(login_window, text="Register", command=register).pack()

login_window.mainloop()
