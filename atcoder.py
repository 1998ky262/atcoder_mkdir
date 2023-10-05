import os
contest_name,level_max=map(str,input().split())
new_dir_path = "ここにいれたいパスを入力しろあほ。じゃないとばぐる。（必然）"+ contest_name
if not os.path.exists(new_dir_path):
   os.mkdir(new_dir_path)
count=["A","B","C","D","E","F","G","HEX"]
count=count[:count.index(level_max)+1]
print(count)
for i in count:
    the_dir = new_dir_path+"/"+contest_name+i+".py"
    if not os.path.exists(the_dir):
       f = open(the_dir,"w")
       f.write("")  # 何も書き込まなくてファイルは作成されました
       f.close()
#atcoder用のpythonファイルを生成するためのスクリプト
#コンテスト名　半角空白　レベル最大
#暇すぎて作った
