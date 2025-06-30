
import argparse
import glob
import os
from pathlib import Path
from markitdown import MarkItDown

def get_output_path(input_file, output_dir, original_input_path):
    if output_dir:
        # 元の入力パスの階層を維持
        try:
            # For cases like C:\data\* where commonpath is not ideal
            base_path = Path(original_input_path).parent if not os.path.isdir(original_input_path) else original_input_path
            relative_path = Path(input_file).parent.relative_to(base_path)
            return Path(output_dir) / relative_path
        except ValueError:
            # Fallback for different drives or complex paths
            return Path(output_dir)
    else:
        # 入力ファイルと同じフォルダ
        return Path(os.path.dirname(input_file))

def main():
    parser = argparse.ArgumentParser(description='Converts various document files to Markdown format.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input file or folder. Wildcards are supported.')
    parser.add_argument('-o', '--output', help='Path to the output folder. Defaults to the same folder as the input file.')
    parser.add_argument('-r', '--recursive', action='store_true', help='Recursively search for files in subfolders.')

    args = parser.parse_args()

    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print(f"Recursive: {args.recursive}")

    # --- ここから処理を実装 ---
    input_path = args.input
    output_path = args.output
    is_recursive = args.recursive

    # ワイルドカードを含むパスの場合、globで解決
    files_to_process = glob.glob(input_path, recursive=is_recursive)

    # ディレクトリが指定された場合
    if os.path.isdir(input_path):
        if is_recursive:
            files_to_process = glob.glob(os.path.join(input_path, '**', '*'), recursive=True)
        else:
            files_to_process = glob.glob(os.path.join(input_path, '*'), recursive=False)

    # フォルダを除外し、ファイルのみを対象とする
    files_to_process = [f for f in files_to_process if os.path.isfile(f)]

    if not files_to_process:
        print(f"No files found matching the pattern: {input_path}")
        return

    print(f"Found {len(files_to_process)} files to process.")

    md = MarkItDown()

    for file_path in files_to_process:
        print(f"Processing: {file_path}")
        try:
            result = md.convert(file_path)

            output_dir = get_output_path(file_path, output_path, input_path)
            output_dir.mkdir(parents=True, exist_ok=True)

            # Excelの特殊処理
            # .sheets属性が存在し、かつ複数のシートを持つか確認
            excel_sheets = getattr(result, 'sheets', None)
            if file_path.lower().endswith(('.xlsx', '.xls')) and isinstance(excel_sheets, dict) and len(excel_sheets) > 1:
                for sheet_name, sheet_content in excel_sheets.items():
                    output_filename = f"{Path(file_path).stem}_{sheet_name}.md"
                    output_filepath = output_dir / output_filename
                    with open(output_filepath, 'w', encoding='utf-8') as f:
                        f.write(sheet_content)
                    print(f"  -> Saved sheet to: {output_filepath}")
            else:
                output_filename = f"{Path(file_path).stem}.md"
                output_filepath = output_dir / output_filename
                with open(output_filepath, 'w', encoding='utf-8') as f:
                    f.write(result.text_content)
                print(f"  -> Saved to: {output_filepath}")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == '__main__':
    main()
