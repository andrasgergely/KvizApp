import customtkinter
from AA_kviz_modul import AA_betolt_kerdesek, AA_Kviz

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Focis kvíz")
app.geometry("900x650")
app.resizable(False, False)

BG = "#0b0f1a"
CARD = "#141b2d"
BTN_KERDES = "#06b2ff"
BTN_KERDES_SZIN = "black"
BTN_UJ = "#3cc85e"

app.configure(fg_color=BG)

frame = customtkinter.CTkFrame(app, fg_color=CARD, corner_radius=25)
frame.pack(padx=40, pady=40, fill="both", expand=True)

kviz = AA_Kviz(AA_betolt_kerdesek(), kerdes_db=10)

title = customtkinter.CTkLabel(frame, text="Focis kvíz", font=("Segoe UI", 32, "bold"))
title.pack(pady=20)

lab_kerdesszam = customtkinter.CTkLabel(frame, text="", font=("Segoe UI", 16))
lab_kerdesszam.pack(pady=5)

lab_kerdes = customtkinter.CTkLabel(frame, text="", font=("Segoe UI", 20))
lab_kerdes.pack(pady=20)

gombok = []
for i in range(3):
    b = customtkinter.CTkButton(
        frame,
        text="",
        width=350,
        height=45,
        fg_color=BTN_KERDES,
        hover_color="#1598d4",
        text_color=BTN_KERDES_SZIN,
        font=("Segoe UI", 16, "bold"),
        command=lambda idx=i: None
    )
    b.pack(pady=8)
    gombok.append(b)

progress = customtkinter.CTkProgressBar(frame, width=450, progress_color="#3cc85e")
progress.set(0)
progress.pack(pady=20)

btn_uj = customtkinter.CTkButton(
    frame,
    text="Új játék",
    width=200,
    height=45,
    fg_color=BTN_UJ,
    hover_color="#2faa4e",
    text_color="white",
    font=("Segoe UI", 17, "bold"),
    command=lambda: uj_jatek()
)
btn_uj.pack(pady=20)
btn_uj.pack_forget()

def kerdes_megjelenit():
    btn_uj.pack_forget()
    adatok = kviz.aktualis()
    if adatok is None:
        mutat_eredmeny()
        return

    kerdes_szoveg, valaszok = adatok
    lab_kerdesszam.configure(text=f"Kérdés: {kviz.index + 1} / {kviz.db}")
    lab_kerdes.configure(text=kerdes_szoveg)

    for i, g in enumerate(gombok):
        g.configure(text=valaszok[i], command=lambda idx=i: valasztas(idx))
        g.pack(pady=8)

    progress.set(kviz.index / kviz.db)

def valasztas(idx):
    kviz.valasz(idx)
    kerdes_megjelenit()

def mutat_eredmeny():
    for g in gombok:
        g.pack_forget()

    helyes, ossz, szaz, szoveg = kviz.eredmeny()

    lab_kerdesszam.configure(text="Kvíz vége")
    lab_kerdes.configure(text=f"Eredményed: {helyes}/{ossz}\n{szaz}%\n\n{szoveg}")

    progress.set(szaz / 100)
    progress.pack_forget()
    progress.pack(pady=30)

    btn_uj.pack_forget()
    btn_uj.pack(pady=35)

def uj_jatek():
    kviz.uj()
    kerdes_megjelenit()

kerdes_megjelenit()
app.mainloop()
