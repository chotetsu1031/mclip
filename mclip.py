#マルチクリップボードプログラム（mclip.py）
import sys
import pyperclip
import json
import os

PHRASES_FILE = 'phrases.json'

#JSONファイルを読み込む
def load_phrases():
  if os.path.exists(PHRASES_FILE):
    with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
      return json.load(f)
    return {}

#JSONファイルに保存する
def save_phrases(data):
  with open(PHRASES_FILE, 'w', encoding='utf-8') as f:
    #Pythonのデータ構造→JSONファイルに変換して保存
    json.dump(data, f, indent=2, ensure_ascii=False)

TEXT = load_phrases()

#使い方の説明
def print_usage():
      print('■ 使い方:')
      print('  python mclip.py [キーフレーズ名]  → コピー実行')
      print('  python mclip.py --add キー 値    → 登録または上書き')
      print('  python mclip.py --delete キー    → 削除')
      print('  python mclip.py --list           → 登録済み一覧')

if len(sys.argv) < 2:
  print_usage()
  sys.exit()

command = sys.argv[1]

if command == "--add" and len(sys.argv) >= 4:
  key = sys.argv[2]
  #第三引数以降をvalueに設定
  value = " ".join(sys.argv[3:])
  TEXT[key] = value
  save_phrases(TEXT)
  print(f"■ '{key}' を登録／更新しました。")
elif command == "--delete" and len(sys.argv) == 3:
  #削除するかどうかの確認
  confirm = input(sys.argv[2] + "を本当に削除しますか？(Y/N)")
  if(confirm == "N" or confirm == "n"):
    print("■ 削除をキャンセルしました。")
  elif(confirm == "Y" or confirm == "y"):
      key = sys.argv[2]
      if key in TEXT:
        del TEXT[key]
        save_phrases(TEXT)
        print(f"■ '{key}' を削除しました。")
      else:
        print(f"■ '{key}' は登録されていません。")
  else:
    print("■ Y/N以外が入力されたため、削除をキャンセルしました。")
elif command == "--list":
  print("■ 登録済みキーフレーズ一覧：")
  for k in TEXT:
    print(f" - {k}")
elif command in TEXT:
  pyperclip.copy(TEXT[command])
  print(f"■ '{command}'のテキストをクリップボードにコピーしました。")
else:
  print(f"■ '{command}' に対応するテキストがありません。")
  print_usage()
