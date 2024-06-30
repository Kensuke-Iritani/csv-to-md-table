import pandas as pd
import glob
import os

def csv_to_markdown(file_path):
    # CSVファイルをUTF-8エンコードで読み込む
    df = pd.read_csv(file_path, encoding='utf-8')
    
    # データフレームをMarkdownの表形式に変換
    markdown_table = df.to_markdown(index=False)
    
    # 出力ファイル名を決定
    output_file = os.path.splitext(file_path)[0] + '.md'
    
    # Markdownの表形式をUTF-8エンコードで出力
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_table)
    
    print(f"Markdown table has been written to {output_file}")

def process_all_csv_files():
    # 現在のディレクトリ内のすべてのCSVファイルを検索
    csv_files = glob.glob('*.csv')
    
    # 各CSVファイルに対して処理を実行
    for csv_file in csv_files:
        csv_to_markdown(csv_file)

# 関数を呼び出して処理を実行
process_all_csv_files()
