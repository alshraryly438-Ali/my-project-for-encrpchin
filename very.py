import tkinter as tk
from tkinter import messagebox
import base64

# ووووووو الدوال الأساسية للتشفير وفك التشفير
def swap(si, sj):
    return sj, si

def pr1(s, t):
    j = 0
    for i in range(256):
        j = (j + s[i] + t[i]) % 256
        s[i], s[j] = swap(s[i], s[j])
    return s

def pr2(s, le):
    k = []
    x = 0
    j = 0
    for i in range(le):
        x = (x + 1) % 256
        j = (j + s[x]) % 256
        s[x], s[j] = swap(s[x], s[j])
        t = (s[x] + s[j]) % 256
        k.append(s[t])
    return k

def keycr(k, le):
    s = list(range(256))
    t = [ord(k[i % len(k)]) for i in range(256)]
    s = pr1(s, t)
    key = pr2(s, le)
    return key

def en(text, key):
    key = keycr(key, len(text))
    ctext = []
    for i in range(len(text)):
        c = key[i] ^ ord(text[i])
        ctext.append(c)
    return ''.join(chr(c) for c in ctext)

def dec(ctext, key):
    key = keycr(key, len(ctext))
    text = []
    for i in range(len(ctext)):
        c = key[i] ^ ord(ctext[i])
        text.append(c)
    return ''.join(chr(c) for c in text)

def en_base64(text, key):
    ctext = en(text, key)
    return base64.b64encode(ctext.encode('latin-1')).decode('utf-8')

def dec_base64(ctext, key):
    ctext = base64.b64decode(ctext).decode('latin-1')
    return dec(ctext, key)

# دوال الواجهة
def encrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
   
    if not text or not key:
        messagebox.showerror("Error", "Both text and key are required!")
        return
   
    cipher = en_base64(text, key)
    cipher_output.delete("1.0", tk.END)
    cipher_output.insert("1.0", cipher)

def decrypt_text():
    cipher = text_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
   
    if not cipher or not key:
        messagebox.showerror("Error", "Both cipher and key are required!")
        return
   
    try:
        plain = dec_base64(cipher, key)
        cipher_output.delete("1.0", tk.END)
        cipher_output.insert("1.0", plain)
    except Exception:
        messagebox.showerror("Error", "Invalid cipher text or key!")

# إعداد واجهة المستخدم
root = tk.Tk()
root.title("Encrypt and Decrypt Tool")
root.geometry("600x400")
root.configure(bg="#f5f5f5")

# إعداد الخطوط
font_label = ("Arial", 12, "bold")
font_entry = ("Arial", 12)
font_button = ("Arial", 10, "bold")

# عنوان التطبيق
title_label = tk.Label(root, text="Encryption & Decryption Tool", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# إدخال النص
text_label = tk.Label(root, text="Enter Text or Cipher:", font=font_label, bg="#f5f5f5", fg="#333")
text_label.pack(anchor="w", padx=20)
text_entry = tk.Text(root, height=5, width=60, font=font_entry)
text_entry.pack(padx=20, pady=5)

# إدخال المفتاح
key_label = tk.Label(root, text="Enter Key:", font=font_label, bg="#f5f5f5", fg="#333")
key_label.pack(anchor="w", padx=20)
key_entry = tk.Entry(root, width=50, font=font_entry)
key_entry.pack(padx=20, pady=5)

# أزرار التشفير وفك التشفير
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt", font=font_button, bg="#4CAF50", fg="white", width=15, command=encrypt_text)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = tk.Button(button_frame, text="Decrypt", font=font_button, bg="#2196F3", fg="white", width=15, command=decrypt_text)
decrypt_button.grid(row=0, column=1, padx=10)

# حقل الإخراج
output_label = tk.Label(root, text="Output:", font=font_label, bg="#f5f5f5", fg="#333")
output_label.pack(anchor="w", padx=20)
cipher_output = tk.Text(root, height=5, width=60, font=font_entry, bg="#e8f5e9")
cipher_output.pack(padx=20, pady=5)

# تشغيل التطبيق
root.mainloop()
