import tkinter as tk
import random

val_lista = ["Sten", "Sax", "Påse"]

def spel_runda(spelare_val):
    slump_val = random.choice(val_lista)

    vinnare = {
        "Sten": "Sax",
        "Sax": "Påse",
        "Påse": "Sten"
    }

    dator_val_label.config(text=f"Datorn valde: {slump_val}")

    if spelare_val == slump_val:
        resultat_label.config(text="Resultat: Oavgjort!")
    elif vinnare[spelare_val] == slump_val:
        resultat_label.config(text="Resultat: Du vinner!")
    else:
        resultat_label.config(text="Resultat: Datorn vinner!")


root = tk.Tk()
root.title("Sten Sax Påse")

instr_label = tk.Label(root, text="Välj ditt drag:")
instr_label.pack(pady=10)

knapp_frame = tk.Frame(root)
knapp_frame.pack(pady=10)

btn_sten = tk.Button(knapp_frame, text="Sten", width=10,
                     command=lambda: spel_runda("Sten"))
btn_sten.grid(row=0, column=0, padx=5)

btn_sax = tk.Button(knapp_frame, text="Sax", width=10,
                    command=lambda: spel_runda("Sax"))
btn_sax.grid(row=0, column=1, padx=5)

btn_pase = tk.Button(knapp_frame, text="Påse", width=10,
                     command=lambda: spel_runda("Påse"))
btn_pase.grid(row=0, column=2, padx=5)

dator_val_label = tk.Label(root, text="Datorn valde: -")
dator_val_label.pack(pady=5)

resultat_label = tk.Label(root, text="Resultat: -", font=("Arial", 12, "bold"))
resultat_label.pack(pady=10)

root.mainloop()
