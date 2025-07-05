#マルチクリップボードプログラム
TEXT = {'checked': 'ご指摘いただいた点を修正いたしましたので、ご確認お願い致します。',
        'mail_start': 'お疲れ様です。須田です',
        'mail_end': '以上、お手数ですが宜しくお願い致します。'}

import sys
import pyperclip

if len(sys.argv) < 2:
  print('使い方：python mclip.py [キーフレーズ名]')
  print('キーフレーズに対応するテキストをクリップボードにコピーします。')
  sys.exit()

keyphrase = sys.argv[1] # 最初のコマンドライン引数がキーフレーズ
if keyphrase in TEXT:
  pyperclip.copy(TEXT[keyphrase])
  print(keyphrase + 'のテキストをクリップボードにコピーしました。')
else:
  print(keyphrase + 'に対応するテキストがありません。')
