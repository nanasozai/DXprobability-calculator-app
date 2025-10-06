# DXprobability-calculator-app
ダブルクロス3rdの判定ダイス・クリティカルに応じて判定目標値以上のダイスロールの成功確率を計算します

# 判定成功率計算アプリ (DXprobability Calculator App)

## 概要

このアプリケーションは、特定のゲームシステム（ダブルクロス The 3rd Edition を想定）において、ダイスロールの「判定成功率」を計算するためのシンプルなGUIツールです。
目標値(t)、クリティカル値(c)、ダイス数(z)を入力することで、達成値が目標値以上になる確率を算出します。

Pythonと`tkinter`（UIフレームワーク）および`ttkbootstrap`（UIスタイル）を使用して開発されました。

## 機能

-   目標値(t)の設定（1以上の整数）
-   クリティカル値(c)の設定（2以上11以下の整数）
-   ダイス数(z)の設定（1以上の自然数）
-   これらの入力値に基づいた判定成功率の計算と表示

## スクリーンショット

![アプリのスクリーンショット](https://github.com/user-attachments/assets/455c01cb-1b58-43f7-92cd-0de3a51c0d3e)
**注**: 上記スクリーンショットはイメージです。実際のアプリの見た目は、ご利用のOSや`ttkbootstrap`のテーマによって多少異なる場合があります。

## ダウンロードと実行

Python環境がない方でも簡単に利用できるよう、Windows用の実行ファイル（`.exe`）を配布しています。

1.  `q_calculator.exe` をダウンロードします。
2.  ダウンロードしたファイルをダブルクリックして実行します。

### 安全性の確認 (任意)

ダウンロードした実行ファイルのハッシュ値を確認することで、ファイルが破損していないこと、またはダウンロード中に改ざんされていないことを検証できます。

**ファイル名**: `q_calculator.exe`
**サイズ**: 約 24.5 MB
**SHA256ハッシュ**:
```1894E53BEDA90C98B0031480D3AD4678FE4E4A9A292016E8FB7C48C4F78271DF```


## ソースコードからの実行（開発者向け）

Python環境がある方は、ソースコードをクローンして実行することも可能です。

### 必要なもの

-   Python 3.10.6
-   以下のPythonライブラリ

### インストール方法

1.  このリポジトリをクローンします:
    ```bash
    git clone https://github.com/nanasozai/DXprobability-calculator-app.git
    cd DXprobability-calculator-app
    ```
2.  仮想環境を作成し、アクティベートします (推奨):
    ```bash
    python -m venv venv
    # Windowsの場合
    .\venv\Scripts\activate
    # macOS/Linuxの場合
    source venv/bin/activate
    ```
3.  必要なライブラリをインストールします:
    ```bash
    pip install -r requirements.txt
    ```

### 実行方法

1.  仮想環境をアクティベートした状態で、以下のコマンドを実行します:
    ```bash
    python q_calculator.py
    ```

## 実行ファイル（.exe）のビルド方法（開発者向け）

配布されている `.exe` ファイルは、以下の環境とコマンドでビルドされています。
自身でビルドして、配布されているファイルとの同一性を確認したい場合に参考にしてください。

### ビルド環境

-   **OS**: Windows 10/11 (64-bit)
-   **Python バージョン**: Python 3.10.6 
-   **PyInstaller バージョン**: PyInstaller 6.11.1
-   **ttkbootstrap バージョン**: ttkbootstrap 1.14.2


### ビルド手順

1.  上記の「インストール方法」に従って、環境をセットアップします。
2.  プロジェクトのルートディレクトリで以下のコマンドを実行します:
    ```bash
    pyinstaller --onefile --noconsole q_calculator.spec
    ```
    （`--name DXprobability-calculator-app` オプションは、実行ファイル名を `DXprobability-calculator-app.exe` にするためのものです。必要に応じて調整してください。）

3.  ビルドが成功すると、`dist` フォルダ内に `DXprobability-calculator-app.exe` ファイルが生成されます。
4.  このファイルと配布されている `DXprobability-calculator-app.exe` のハッシュ値を比較することで、同一性を確認できます。

## ライセンス

このプロジェクトは [MIT License](LICENSE) の下で公開されています。
詳細については、`LICENSE` ファイルを参照してください。

## 連絡先

ご質問やご意見がありましたら、GitHubのIssue機能をご利用いただくか、以下の連絡先までお問い合わせください。

-   **GitHub**: [@nanasozai](https://github.com/nanasozai)

---
