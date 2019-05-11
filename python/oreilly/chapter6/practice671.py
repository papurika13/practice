# 表示データの宣言
table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'Devid'],
              ['dogs', 'cats', 'moose', 'goose']]
              
# 各列の最大文字数を保持する
length = [0] * len(table_data)

# 各列の最大文字数をlengthに保存する
for i in range(len(table_data[0])):
    for j in range(len(table_data)):
        length[j] = max(length[j], len(table_data[j][i]))
        
# 各列の表示位置を揃えて、行列を反転させて表示する
for i in range(len(table_data[0])):
    for j in range(len(table_data)):
        print(table_data[j][i].rjust(length[j]), end=' ')
    print()