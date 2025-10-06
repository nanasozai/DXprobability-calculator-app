import tkinter as tk
from tkinter import messagebox
import math
import ttkbootstrap as ttk # ttkbootstrapをインポート

# P(t,y,z) を計算する関数
def calculate_P(t, y, z):
    if not (1 <= y <= 10):
        raise ValueError("内部計算エラー: yが1から10の範囲外です。")
    if not (z >= 1):
        raise ValueError("zは自然数（1以上）である必要があります。")
    
    if t < 1: 
        return 0.0

    x = math.floor((t - 1) / 10) + 1
    w = (t - 1) % 10 + 1

    if w > y:
        return 0.0

    p_removed_per_roll = y / 10.0
    p_survive_per_roll = 1.0 - p_removed_per_roll

    total_probability = 0.0

    for k in range(1, z + 1):
        binomial_coefficient = math.comb(z, k)

        term1_base = (p_survive_per_roll)**(x - 1) if (x - 1) >= 0 else 1.0
        term1 = (1.0 - term1_base)**(z - k)

        term2 = (term1_base)**k
        
        prob_max_w = (w / 10.0)**k
        prob_max_w_minus_1 = (max(0, w - 1) / 10.0)**k
        term3 = prob_max_w - prob_max_w_minus_1
        
        total_probability += binomial_coefficient * term1 * term2 * term3

    return total_probability

# 累積関数 E(t_max, y, z) を計算する関数
def calculate_E(t_max, y, z):
    if t_max <= 0:
        return 0.0
    
    if not (1 <= y <= 10):
        raise ValueError("内部計算エラー: yが1から10の範囲外です。")
    if not (z >= 1):
        raise ValueError("zは自然数（1以上）である必要があります。")

    cumulative_probability = 0.0
    for t_val in range(1, t_max + 1):
        cumulative_probability += calculate_P(t_val, y, z)
    return cumulative_probability

# GUIアプリケーションのメインクラス
class QCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("判定成功率計算アプリ") 
        master.geometry("450x450") # ウィンドウサイズを少し大きく
        master.resizable(False, False) # ウィンドウサイズ変更不可に

        # スタイルの設定 (ttkbootstrapのテーマを適用)
        # "flatly", "cosmo", "litera", "united", "materia", "journal" など色々試せます
        style = ttk.Style("flatly") 

        # メインフレーム
        main_frame = ttk.Frame(master, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # タイトルラベル
        ttk.Label(main_frame, text="判定成功率計算", font=("Helvetica", 18, "bold"), bootstyle="primary").pack(pady=15)

        # 入力フィールドとラベルのフォントスタイル
        label_font = ("Helvetica", 12)
        spinbox_font = ("Helvetica", 12)

        # 目標値(t)
        t_frame = ttk.Frame(main_frame)
        t_frame.pack(fill=tk.X, pady=5)
        ttk.Label(t_frame, text="目標値(t):", font=label_font).pack(side=tk.LEFT, padx=5)
        self.t_var = tk.IntVar(value=10)
        # Spinboxの矢印を大きくするため、bootstyleとfontを調整
        self.t_spinbox = ttk.Spinbox(t_frame, from_=1, to=1000, textvariable=self.t_var, width=8, font=spinbox_font, bootstyle="primary")
        self.t_spinbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(t_frame, text="(1以上の整数)", font=("Helvetica", 10)).pack(side=tk.RIGHT, padx=5)

        # クリティカル値(c)
        c_frame = ttk.Frame(main_frame)
        c_frame.pack(fill=tk.X, pady=5)
        ttk.Label(c_frame, text="クリティカル値(c):", font=label_font).pack(side=tk.LEFT, padx=5)
        self.c_var = tk.IntVar(value=5)
        self.c_spinbox = ttk.Spinbox(c_frame, from_=2, to=11, textvariable=self.c_var, width=8, font=spinbox_font, bootstyle="primary")
        self.c_spinbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(c_frame, text="(2以上11以下の整数)", font=("Helvetica", 10)).pack(side=tk.RIGHT, padx=5)

        # ダイス数(z)
        z_frame = ttk.Frame(main_frame)
        z_frame.pack(fill=tk.X, pady=5)
        ttk.Label(z_frame, text="ダイス数(z):", font=label_font).pack(side=tk.LEFT, padx=5)
        self.z_var = tk.IntVar(value=3)
        self.z_spinbox = ttk.Spinbox(z_frame, from_=1, to=100, textvariable=self.z_var, width=8, font=spinbox_font, bootstyle="primary")
        self.z_spinbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(z_frame, text="(1以上の自然数)", font=("Helvetica", 10)).pack(side=tk.RIGHT, padx=5)

        # 計算ボタン
        # ttkbootstrapのButtonで見た目を改善
        self.calculate_button = ttk.Button(main_frame, text="計算実行", command=self.calculate_q, 
                                           bootstyle="primary", # プライマリカラーのボタン
                                           width=20, # ボタンの幅
                                           padding=10 # ボタン内のパディング
                                          )
        self.calculate_button.pack(pady=20)

        # 結果表示エリア
        self.result_label = ttk.Label(main_frame, text="判定成功率: ", font=("Helvetica", 16, "bold"), bootstyle="success", justify=tk.CENTER)
        self.result_label.pack(pady=10)

    def calculate_q(self):
        try:
            t = self.t_var.get()
            c = self.c_var.get()
            z = self.z_var.get()

            # 入力値のバリデーション
            if t < 1:
                messagebox.showerror("入力エラー", "目標値(t)は1以上の整数である必要があります。")
                return
            if not (2 <= c <= 11):
                messagebox.showerror("入力エラー", "クリティカル値(c)は2以上11以下の整数である必要があります。(y=c-1が1〜10になるため)")
                return
            if z < 1:
                messagebox.showerror("入力エラー", "ダイス数(z)は1以上の自然数である必要があります。")
                return

            y_calculated = c - 1

            # 計算実行
            cumulative_E_t_minus_1 = calculate_E(t - 1, y_calculated, z)
            Q_value = (1.0 - cumulative_E_t_minus_1) * 100.0

            # 結果を「判定成功率: Q値%」の形式で表示
            result_text = f"判定成功率: {Q_value:.12f}%"
            self.result_label.config(text=result_text)

        except ValueError as e:
            messagebox.showerror("計算エラー", f"無効な入力です: {e}")
        except Exception as e:
            messagebox.showerror("エラー", f"予期せぬエラーが発生しました: {e}")

# アプリケーションの実行
if __name__ == "__main__":
    # tk.Tk() の代わりに ttk.Window() を使用
    root = ttk.Window(themename="flatly") # テーマをWindow作成時に指定
    app = QCalculatorApp(root)
    root.mainloop()