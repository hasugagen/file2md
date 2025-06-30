# ファイルMarkdown変換ツール (file2md)

## 1. 概要

このツールは、指定されたフォルダ内に存在する各種ドキュメントファイル（Word, Excel, PowerPoint, PDFなど）を、一括でMarkdown形式に変換するコマンドラインツールです。

Microsoftの`markitdown`ライブラリを活用し、Windows環境で動作する単一の実行ファイル（.exe）として利用できます。

## 2. 主な機能

- **多様なファイル形式のサポート**: `markitdown`がサポートする全てのファイル形式（.pdf, .docx, .xlsx, .pptxなど）に対応します。
- **柔軟な入力指定**: 単一ファイル、フォルダ、ワイルドカード（`*`）での指定が可能です。
- **再帰的処理**: サブフォルダ内のファイルもまとめて変換するオプションがあります。
- **Excelの複数シート対応**: Excelファイルに複数のシートがある場合、各シートを個別のMarkdownファイルとして出力します。
- **出力先指定**: 変換後のファイルの出力先フォルダを指定できます。指定しない場合は入力元と同じフォルダに出力されます。
- **フォルダ構造の維持**: 出力先を指定した場合でも、元のフォルダ階層を維持して出力します。

## 3. 開発環境のセットアップ

開発やカスタマイズを行うための環境構築手順です。

### 前提条件

- [Python 3.10](https://www.python.org/downloads/) 以上がインストールされていること。
- [Git](https://git-scm.com/downloads) がインストールされていること。

### セットアップ手順

1. **リポジトリをクローンします。**
   ```bash
   git clone <repository-url>
   cd markitdown-tool
   ```

2. **Pythonの仮想環境を作成し、有効化します。**
   ```bash
   # 仮想環境を作成 (初回のみ)
   python -m venv .venv

   # 仮想環境を有効化 (作業開始時に毎回実行)
   .venv\Scripts\activate
   ```

3. **必要な依存ライブラリをインストールします。**
   ```bash
   pip install -r requirements.txt
   ```

これで、ソースコードの編集やデバッグが可能になります。

## 4. ツールの使い方

仮想環境を有効化した後、`src/main.py`を直接実行できます。

```bash
python src/main.py --input <入力パス> [オプション]
```

### コマンドライン引数

| 引数 | 短縮形 | 必須 | 説明 |
| :--- | :--- | :--- | :--- |
| `--input <path>` | `-i <path>` | **はい** | 変換対象のファイルまたはフォルダのパス。ワイルドカード使用可。 |
| `--output <path>`| `-o <path>` | いいえ | 変換後のファイルの出力先フォルダ。省略時は入力元と同じ場所。 |
| `--recursive` | `-r` | いいえ | 入力フォルダのサブフォルダも再帰的に検索します。 |

### 実行例

- **単一フォルダ内のファイルを変換し、別のフォルダに出力**
  ```bash
  python src/main.py -i "C:\Reports" -o "D:\Markdown_Files"
  ```

- **サブフォルダを含めて再帰的に変換**
  ```bash
  python src/main.py -i "C:\Reports" -o "D:\Markdown_Files" -r
  ```

- **ワイルドカードを使い、同じ場所に出力**
  ```bash
  python src/main.py -i "C:\Project\data\2024_*.pdf"
  ```

## 5. ビルド方法

依存ライブラリを含んだ単一の実行ファイル（`.exe`）を作成するには、プロジェクトルートにある`build.bat`を実行します。

```bash
.\build.bat
```

実行後、`dist`フォルダ内に`file2md.exe`が生成されます。
