#脱出ゲーム
#プレイヤーは東西南北の壁を確認することができる
#壁には仕掛けがあり、仕掛けを調べていくことで情報を集めていく
#脱出のための必要要素は4つ
#選択回数によってHPが減っていく
#MAP中央には食事が用意されているが回復値はそれぞれ決まっており、食べたら消える
#Keyを4つ集めたら脱出、HPが0になる前に脱出できなければゲームオーバー

#PLの位置
key = ""
#PLの体力
pl_hp = 15
#北の脱出用鍵
north_escape1 = 0
north_escape2 = 0

#東の脱出用鍵
east_escape1 = 0
east_escape2 = 0

import choice_game
import choice_north
import center_room
import south_room
import north_room
import west_room
import east_room

#スタート
print("貴方は薄暗い部屋の中央に立っている。")
print("部屋は薄暗く、窓や扉といった出入口は見当たらない。")
print("不気味な雰囲気を感じる、はやく脱出を試みたほうがいいだろう。")
print("現在のHP：15/15")
print("選択肢を選んでください。")

while True:
    key = input("""
ce:部屋の中央を見る
no:部屋の北側を見る
so:部屋の南側を見る
ea:部屋の東側を見る
we:部屋の西側を見る\n""").strip()
    if key in ["ce", "no", "so", "ea", "we"]:
        break
    else:
        print("正しい選択肢を入力してください")

    

while pl_hp > 0 or 0 in [north_escape1, north_escape2, east_escape1, east_escape2:
    #部屋の中央
    if key == "ce":
        key = center_room.center()
    #中央_テーブル確認
    elif key == "cc":
        key, pl_hp = center_room.center_cook(pl_hp)
 
    #南の壁
    elif key == "so":
        key, pl_hp = south_room.south(pl_hp)   
        
    #北の壁を見る
    elif key == "no":
        key = north_room.north()
        
    #北_一番上の棚を見る
    elif key == "top":
        key = north_room.top_shelf()

    #北_赤い狼のぬいぐるみに触れる
    elif key == "red":
        key, pl_hp = north_room.red_wolf(pl_hp)

    #北_黒い狼のぬいぐるみに触れる
    elif key == "black":
        key = north_room.black_wolf()

    #北_白い狼のぬいぐるみに触れる
    elif key == "white":
        key = north_room.white_wolf()

    #北_白い狼のぬいぐるみ_縫い目をほどく
    elif key == "undo":
        key, north_escape1 = north_room.white_wolf_undo()

    #北_白い狼のぬいぐるみ_元の位置に戻す
    elif key == "re":
        key = north_room.white_wolf_return()

    #北_中央の棚を見る
    elif key == "center":
        key = north_room.center_shelf()        

    #北_一番下の棚を見る
    elif key == "down":
        key = north_room.down_shelf()

    #北_大サイズの子ぶたのぬいぐるみ確認
    elif key == "large":
        key, pl_hp = north_room.large_piglet(pl_hp)

    #北_中サイズの子ぶたのぬいぐるみ確認
    elif key == "medium":
        key, pl_hp = north_room.medium_piglet(pl_hp)

    #北_小サイズの子ぶたのぬいぐるみ確認
    elif key == "small":
        key = north_room.small_piglet()

    #北_小サイズの子ぶたの座っている場所の確認
    elif key == "move":
        key, north_escape2 = north_room.small_piglet_move()

    #西の壁
    elif key == "we":
        key, pl_hp = west_room.west(pl_hp)   

    #東の壁
    elif key == "ea":
        key = east_room.east()

    #東_星空のキャンバス
    elif key == "star":
        key, pl_hp = east_room.canvas_star()
        
    #東_林檎のキャンバス
    elif key == "apple":
        key, pl_hp = east_room.canvas_apple()

    #東_林檎のキャンバスに触れる
    elif key == "touch":
        key, pl_hp,east_escape1 = east_room.canvas_apple_touch(pl_hp)
        
    #東_真っ白なキャンバス
    elif key == "void":
        key, pl_hp = east_room.canvas_void(pl_hp)
        
    #東_薔薇のキャンバス
    elif key == "rose":
        key = east_room.west()   



if pl_hp <= 0:
    print("体力が尽きてしまい、床に倒れた。\n\
薄れゆく意識のなか、貴方は何かの声を聞いた気がする。\n\
Game Over")






































    


