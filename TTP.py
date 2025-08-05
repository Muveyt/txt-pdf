import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF

def convert_txt_to_pdf(txt_path, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            for line in file:
                pdf.cell(200, 10, txt=line.strip(), ln=True)
        pdf.output(pdf_path)
        messagebox.showinfo("Success", f"PDF saved to:\n{pdf_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_txt():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        txt_entry.delete(0, tk.END)
        txt_entry.insert(0, file_path)

def save_pdf():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_entry.delete(0, tk.END)
        pdf_entry.insert(0, file_path)

def convert():
    txt_path = txt_entry.get()
    pdf_path = pdf_entry.get()
    if txt_path and pdf_path:
        convert_txt_to_pdf(txt_path, pdf_path)
    else:
        messagebox.showwarning("Missing Info", "Please select both TXT file and PDF save location.")

# GUI Setup
root = tk.Tk()
root.title("TXT to PDF Converter")
root.geometry("500x200")

tk.Label(root, text="Select TXT file:").pack(pady=5)
txt_entry = tk.Entry(root, width=50)
txt_entry.pack()
tk.Button(root, text="Browse", command=browse_txt).pack(pady=5)

tk.Label(root, text="Save PDF as:").pack(pady=5)
pdf_entry = tk.Entry(root, width=50)
pdf_entry.pack()
tk.Button(root, text="Choose Save Location", command=save_pdf).pack(pady=5)

tk.Button(root, text="Convert to PDF", command=convert, bg="green", fg="white").pack(pady=10)

root.mainloop()
