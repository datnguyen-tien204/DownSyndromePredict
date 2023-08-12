import tkinter as tk
from tkinter import ttk
import joblib
import pandas as pd
from tkinter import messagebox

prediction_enabled = False


# Danh sách các tên model (ví dụ)
model_names = ["Logistic_Regression", "KNN", "Naive_Bayes","Decision_Tree"]

# Lưu danh sách tên model vào tệp .sav
loaded_model = None
# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Danh sách các model")

label1 = tk.Label(root, text="Tuổi mẹ( năm )")
label1.grid(row=2, column=1, padx=10, pady=10)
label2 = tk.Label(root, text="Tuổi thai (ngày)")
label2.grid(row=2, column=2, padx=10, pady=10)
label3 = tk.Label(root, text="Tiển sử sinh con hội chứng down(0:bị-1:không)")
label3.grid(row=2, column=3, padx=10, pady=10)
label4 = tk.Label(root, text="Chiều dài đầu mông(mm)")
label4.grid(row=4, column=1, padx=10, pady=10)
label5 = tk.Label(root, text="Đường kính lưỡng dịch(mm)")
label5.grid(row=4, column=2, padx=10, pady=10)
label6 = tk.Label(root, text="Chu vi đầu(mm)")
label6.grid(row=4, column=3, padx=10, pady=10)
label7 = tk.Label(root, text="Mắt/môi/mũi(0:bình thương-1:có vấn đề)")
label7.grid(row=4, column=4, padx=10, pady=10)
label8 = tk.Label(root, text="Ngực(mm):")
label8.grid(row=7, column=1, padx=10, pady=10)
label9 = tk.Label(root, text="Tỉ lệ bệnh Down trong gia đình(0<x<1)")
label9.grid(row=7, column=2, padx=10, pady=10)
label10 = tk.Label(root, text="Nồng độ Hoocmon beta hCG-máu mẹ(IU/l)")
label10.grid(row=7, column=3, padx=10, pady=10)
label11 = tk.Label(root, text="Khoảng sáng sau gáy(mm)")
label11.grid(row=7, column=4, padx=10, pady=10)
label12 = tk.Label(root, text="Chọn model")
label12.grid(row=1, column=2, padx=10, pady=10)
# Kích thước ban đầu của cửa sổ
window_width = 700
window_height = 700

# Đặt kích thước và vị trí cửa sổ
root.geometry("1000x500")


# Biến để lưu giá trị từ combo box và Entry widget
selected_model_var = tk.StringVar()
entry_var1 = tk.StringVar()
entry_var2 = tk.StringVar()
entry_var3 = tk.StringVar()
entry_var4 = tk.StringVar()
entry_var5 = tk.StringVar()
entry_var6 = tk.StringVar()
entry_var7 = tk.StringVar()
entry_var8 = tk.StringVar()
entry_var9 = tk.StringVar()
entry_var10 = tk.StringVar()
entry_var11 = tk.StringVar()

# Tạo combo box
combo_box = ttk.Combobox(root, textvariable=selected_model_var, state='readonly')
combo_box.grid(row=1, column=3, padx=10, pady=10)
combo_box['values'] = model_names

# Tạo Entry widget cho việc nhập liệu (Ô nhập liệu 1)
entry_box1 = tk.Entry(root, textvariable=entry_var1)
entry_box1.grid(row=3, column=1, padx=10, pady=10)

# Tạo Entry widget cho việc nhập liệu (Ô nhập liệu 2)
entry_box2 = tk.Entry(root, textvariable=entry_var2)
entry_box2.grid(row=3, column=2, padx=10, pady=10)

# Tạo Entry widget cho việc nhập liệu (Ô nhập liệu 2)
entry_box3 = tk.Entry(root, textvariable=entry_var3)
entry_box3.grid(row=3, column=3, padx=10, pady=10)

# Tạo Entry widget cho việc nhập liệu (Ô nhập liệu 2)
entry_box4 = tk.Entry(root, textvariable=entry_var4)
entry_box4.grid(row=6, column=1, padx=10, pady=10)

entry_box5 = tk.Entry(root, textvariable=entry_var5)
entry_box5.grid(row=6, column=2, padx=10, pady=10)

entry_box6 = tk.Entry(root, textvariable=entry_var6)
entry_box6.grid(row=6, column=3, padx=10, pady=10)

entry_box7 = tk.Entry(root, textvariable=entry_var7)
entry_box7.grid(row=6, column=4, padx=10, pady=10)

entry_box8 = tk.Entry(root, textvariable=entry_var8)
entry_box8.grid(row=9, column=1, padx=10, pady=10)


entry_box9 = tk.Entry(root, textvariable=entry_var9)
entry_box9.grid(row=9, column=2, padx=10, pady=10)

entry_box10 = tk.Entry(root, textvariable=entry_var10)
entry_box10.grid(row=9, column=3, padx=10, pady=10)

entry_box11 = tk.Entry(root, textvariable=entry_var11)
entry_box11.grid(row=9, column=4, padx=10, pady=10)
# Hàm được gọi khi chọn một model trong combo box
def on_model_select(event):
    global prediction_enabled
    global loaded_model  # Khai báo "loaded_model" ở đây để truy cập từ các hàm khác
    global selected_model

    selected_model = selected_model_var.get()
    print(f"Bạn đã chọn model: {selected_model}")

    try:
        # Load mô hình tương ứng với model đã chọn
        model_file_path = f"{selected_model}.sav"
        loaded_model = joblib.load(model_file_path)

    except FileNotFoundError:
        messagebox.showerror("Lỗi", f"Tệp mô hình {selected_model} không được tìm thấy!")
        return

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi tải mô hình {selected_model}:\n{str(e)}")
        return

    prediction_enabled = False

# Khi chọn một model trong combo box, gọi hàm on_model_select
combo_box.bind('<<ComboboxSelected>>', on_model_select)

def on_confirm_button_click():
    prediction_enabled = True
    if prediction_enabled:
        additional_info1 = entry_var1.get()

        additional_info2 = entry_var2.get()
        additional_info3 = entry_var3.get()
        additional_info4 = entry_var4.get()
        additional_info5 = entry_var5.get()
        additional_info6 = entry_var6.get()
        additional_info7 = entry_var7.get()
        additional_info8 = entry_var8.get()
        additional_info9 = entry_var9.get()
        additional_info10 = entry_var10.get()
        additional_info11 = entry_var11.get()

        # Tạo một danh sách chứa các giá trị nhập liệu
        data_test = [
            float(additional_info1),
            float(additional_info2),
            float(additional_info3),
            float(additional_info4),
            float(additional_info5),
            float(additional_info6),
            float(additional_info7),
            float(additional_info8),
            float(additional_info9),
            float(additional_info10),
            float(additional_info11)
        ]

        columns = ["tuoi_me_new","tuoi_thai_new","tiensusinhconhoichungdown","chieudaidaumong","dau_duongkinhluongdinh","dau_chuvidau","mat_moimui","nguc_nhiptimthai","d_mom_pappa","d_mom_hcgb","d_khoangsangsaugay"]
        # Chuyển danh sách thành DataFrame
        df2 = pd.DataFrame([data_test], columns=columns)

        # Thực hiện dự đoán
        prediction = loaded_model.predict(df2)
        if (prediction[0]==0):
            a="Bình thường"
        else:
            a="Có vấn đề"
        messagebox.showinfo("Kết quả dự đoán", f"Kết quả dự đoán của model {selected_model}: {a}")

    prediction_enabled = True

def reset():
    entry_var1.set("")
    entry_var2.set("")
    entry_var3.set("")
    entry_var4.set("")
    entry_var5.set("")
    entry_var6.set("")
    entry_var7.set("")
    entry_var8.set("")
    entry_var9.set("")
    entry_var10.set("")
    entry_var11.set("")

# Tạo nút xác nhận
confirm_button = tk.Button(root, text="Tính", command=on_confirm_button_click)
confirm_button.grid(row=12, column=2, columnspan=2, padx=20, pady=20)

confirm_button2 = tk.Button(root, text="Reset", command=reset)
confirm_button2.grid(row=12, column=3, columnspan=2, padx=20, pady=20)

root.mainloop()
