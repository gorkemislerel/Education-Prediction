import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = pd.read_csv("world-education-data.csv")
df.columns = ["ülke", "ülke_kodu", "yıl", "eğitim_harcamaları_gsyih", "yetişkin_okuryazarlık_oranı", "ilköğretim_tamamlama_oranı", 
              "ilköğretim_öğrenci_öğretmen_oranı", "ortaöğretim_öğrenci_öğretmen_oranı", "ilköğretim_kayıt_oranı", 
              "ortaöğretim_kayıt_oranı", "yükseköğretim_kayıt_oranı"]

columns_to_fill = ["eğitim_harcamaları_gsyih", "ilköğretim_tamamlama_oranı", 
                   "ilköğretim_öğrenci_öğretmen_oranı", "ortaöğretim_öğrenci_öğretmen_oranı", 
                   "ilköğretim_kayıt_oranı", "ortaöğretim_kayıt_oranı", "yükseköğretim_kayıt_oranı"]
for col in columns_to_fill:
    df[col] = df[col].fillna(df[col].mean())

df = df[df['yetişkin_okuryazarlık_oranı'].notna()]

y = df["yetişkin_okuryazarlık_oranı"]
X = df.drop(["ülke", "ülke_kodu", "yıl", "yetişkin_okuryazarlık_oranı"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_model = KNeighborsRegressor()
knn_grid = {
    "n_neighbors": [3, 5, 7, 9],
    "weights": ["uniform", "distance"],
    "algorithm": ["auto", "ball_tree", "kd_tree", "brute"]
}
knn_cv = GridSearchCV(knn_model, param_grid=knn_grid, cv=3, verbose=2)
knn_cv.fit(X_train_scaled, y_train)

knn_tuned = KNeighborsRegressor(**knn_cv.best_params_)
knn_tuned.fit(X_train_scaled, y_train)

def update_graph():
    if not prediction_history:
        return

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(range(len(prediction_history)), prediction_history, color='skyblue')
    ax.set_title("Tahmin Sonuçları Geçmişi")
    ax.set_xlabel("Tahmin #")
    ax.set_ylabel("Okuryazarlık Oranı")

    for widget in frame_graph.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=frame_graph)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

prediction_history = []
def predict():
    try:
        input_values = [float(entry.get()) for entry in entry_vars]
        input_data = pd.DataFrame([input_values], columns=X.columns)
        input_data_scaled = scaler.transform(input_data)
        prediction = knn_tuned.predict(input_data_scaled)[0]

        prediction_history.append(prediction)
        update_graph()
        messagebox.showinfo("Tahmin Sonucu", f"Yetişkin Okuryazarlık Oranı Tahmini: {prediction:.2f}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen tüm alanları doğru şekilde doldurduğunuzdan emin olun.")

root = tk.Tk()
root.title("Eğitim Verisi Tahmin Uygulaması")
root.geometry("600x600")
root.configure(bg="lightblue")

frame_input = tk.Frame(root, bg="lightblue")
frame_input.pack(pady=10, anchor="w")
entry_vars = []
inputs = [
    "Eğitim Harcamaları (GSYİH):", "İlköğretim Tamamlama Oranı:", "İlköğretim Öğrenci-Öğretmen Oranı:",
    "Ortaokul Öğrenci-Öğretmen Oranı:", "İlköğretim Kayıt Oranı:", "Ortaöğretim Kayıt Oranı:", "Yükseköğretim Kayıt Oranı:"
]
default_values = [5.0, 95.0, 20.0, 15.0, 98.0, 85.0, 50.0]

for label_text, default in zip(inputs, default_values):
    tk.Label(frame_input, text=label_text, bg="lightblue").pack()
    entry = tk.Entry(frame_input)
    entry.insert(0, str(default))
    entry.pack()
    entry_vars.append(entry)

button_predict = ttk.Button(root, text="Tahmin Et", command=predict)
button_predict.pack(pady=10)

frame_graph = tk.Frame(root, bg="white", relief=tk.RAISED, borderwidth=2)
frame_graph.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()