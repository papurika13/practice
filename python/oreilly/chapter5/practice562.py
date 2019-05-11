dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
inventory = {'金貨': 42, 'ロープ': 1}

def add_to_inventory(inventory, added_items):
    for item in added_items:
        # インベントリーにアイテムがない場合
        if item not in inventory:
            inventory[item] = 1
        else:
            #あれば加算する
            inventory[item]+=1

def display_inventory(inventory):
    print("持ち物リスト")
    item_total = 0
    for k, v in inventory.items():
        print(k + ': ' + str(v))
        item_total += v
    print('アイテム総数' + str(item_total))
    
inv = add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)