import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
import numpy as np

# بناء نموذج التعلم الآلي (في هذه الحالة استخدام نموذج الانحدار الخطي)
model = LinearRegression()

# البيانات - يمكن استبدال هذه البيانات بمجموعة بيانات خاصة بك
X = np.array([[1000, 2], [1500, 3], [2000, 4], [2500, 5]])  # مساحة الأرض وعدد الغرف
y = np.array([50000, 75000, 100000, 125000])  # سعر الأرض

# تدريب نموذج التعلم الآلي
model.fit(X, y)

# دالة للتنبؤ بسعر الأرض استنادًا إلى المساحة وعدد الغرف
def predict_price(area, rooms):
    return model.predict([[area, rooms]])

# دالة للتعامل مع الزر "توقع السعر"
def predict():
    try:
        area = float(entry_area.get())
        rooms = float(entry_rooms.get())
        price = predict_price(area, rooms)
        messagebox.showinfo("توقع سعر الأرض", f"سعر الأرض المتوقع هو: ${price[0]:,.2f}")
    except ValueError:
        messagebox.showerror("خطأ", "الرجاء إدخال قيم صحيحة للمساحة وعدد الغرف")

# إنشاء واجهة المستخدم
root = tk.Tk()
root.title("توقع سعر الأرض")

label_area = tk.Label(root, text="المساحة (قدم مربعة):")
label_area.grid(row=0, column=0, padx=10, pady=5)
entry_area = tk.Entry(root)
entry_area.grid(row=0, column=1, padx=10, pady=5)

label_rooms = tk.Label(root, text="عدد الغرف:")
label_rooms.grid(row=1, column=0, padx=10, pady=5)
entry_rooms = tk.Entry(root)
entry_rooms.grid(row=1, column=1, padx=10, pady=5)

button_predict = tk.Button(root, text="توقع السعر", command=predict)
button_predict.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()