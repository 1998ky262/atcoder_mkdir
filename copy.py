import pyperclip

file_path = r"C:\\Users\\user\\proj\\atcoder\simple.py"

try:
    with open(file_path, 'r') as file:
        content = file.read()
except FileNotFoundError:
    content = None

if content:
    pyperclip.copy(content)
    print('simple.pyの内容がクリップボードにコピーされました。')
else:
    print('simple.pyファイルが見つかりません。')
#これはAtCoderなどで早くコピーできるようにせいせいしたものです。リンクパスをいじくって自分用にしてもいいよん
