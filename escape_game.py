#PLの部屋位置
key = ""
#PLの体力
pl_hp = 15
#北の脱出用鍵
north_escape1 = 0
north_escape2 = 0

#東の脱出用鍵
east_escape1 = 0
east_escape2 = 0

#部屋の脱出用鍵
escape = ""

import sys

#各部分のシナリオ、および選択肢のインポート
import choice_game
import choice_north
import choice_east
import center_room
import south_room
import north_room
import west_room
import east_room


#プレイヤー死亡時のゲーム終了
def game_over():
    print("体力が尽きてしまい、床に倒れた。")
    print("薄れゆく意識のなか、貴何かの声を聞いた気がする。")
    print("ゲームオーバー")
    sys.exit()


#スタート
print("薄暗い部屋の中央に立っている。")
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

    
#各部屋のシナリオ分岐
while pl_hp > 0 and 0 in [north_escape1, north_escape2, east_escape1, east_escape2]:
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

    #北_白い狼のぬいぐるみ_縫い目をほどく（脱出キー入手）
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

    #北_小サイズの子ぶたの座っている場所の確認（脱出キー入手）
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
        key = east_room.canvas_star()
        
    #東_林檎のキャンバス
    elif key == "apple":
        key = east_room.canvas_apple()

    #東_林檎のキャンバスに触れる（脱出キー入手）
    elif key == "touch":
        key, pl_hp,east_escape1 = east_room.canvas_apple_touch(pl_hp)
        
    #東_真っ白なキャンバス
    elif key == "void":
        key, pl_hp = east_room.canvas_void(pl_hp)

    #東_薔薇のキャンバス
    elif key == "rose":
        key = east_room.canvas_rose()   
        
    #東_薔薇のキャンバスに吸い込まれる（脱出キー入手）
    elif key == "***":
        key, pl_hp, east_escape2 = east_room.canvas_rose_sucked(pl_hp)   

#PL死亡
if pl_hp <= 0:
    game_over()

#脱出キーをすべて集めて進むシナリオ
else:
    print("もうこの部屋の中に探せるものは無いようだ。")
    print("どうしたのとかと考えていたら、部屋の中央のテーブルに奇妙な黒い箱が現れた。")
    print("先ほどまであったはずのキャンバスやぬいぐるみは、気付いたら消えている……。")
    print("この部屋から出る手がかりは、もうこの黒い箱だけのようだ。")


    while True:
        key = input("""yes:黒い箱を見る
no:現実逃避をして部屋の中を歩き回る\n""")
        if key in ["yes", "no"]:
            #PL死亡
            if key == "no":
                game_over()
            #次のシナリオへ進む
            elif key == "yes":
                break                
        else:
            print("正しい選択肢を入力してください")


#最終チャレンジへ進行
print("黒い箱を見た。")
print("箱の上部には白い四角が4つ並んでいる。")
print("四角に触れたら文字が浮かび上がり、1マス1文字選択できるようになっている。")


#ヒントを思い出す選択肢
while pl_hp > 0 and escape != "help":
    while True:
        key = input("""wolf:狼のぬいぐるみを思い出す
piglet:三匹の子ぶたのぬいぐるみを思い出す
apple:林檎の絵を思い出す
rose:赤い薔薇の絵を思い出す
hope:箱に文字を入力する\n""")
        if key in ["wolf", "piglet", "apple", "rose", "hope"]:
            if key == "wolf":
                print("狼のぬいぐるみについて思い出した。")
                print("白色の狼の腹に入っていた紙に、「け（12）」と文字が書かれていた気がする。")
            if key == "piglet":
                print("子ぶたのぬいぐるみについて思い出した。")
                print("一番小さな子ぶたが座っていた白いレンガ部分に、「た（8）」と文字が書かれていた気がする。")
            if key == "apple":
                print("林檎の絵について思い出した。")
                print("変色した林檎の絵の上に、「て（16）」と文字が書かれていた気がする。")
            if key == "rose":
                print("真っ赤な薔薇の絵のことを思い出した。")
                print("……詳細を思い出そうとすると、激しく頭が痛み始める。")
                print("ただ、「す（5）」という文字を見たことだけは、思い出せた。")
            if key == "hope":
                print("今まで見つけたものを頼りに、箱に文字を入力してみよう。")
                escape = input("4文字の暗号を入力してください：")
                if escape != "help":
                    print("……何も起きない。")
                    print("どうやら入力する文字を間違ったようだ。")
                    print("なぜだか一気に体力を消耗した気がする……。")
                    pl_hp -= 5
                    print(f"現在のHP：{hp}/15")
                else:
                    break

        else:
            print("正しい選択肢を入力してください")


#PL死亡
if pl_hp <= 0:
    game_over()

#脱出成功
else:
    print("…………目を開けたら、そこには見慣れた天井が広がっていた")
    print("どうやら奇妙な夢を見ていたらしい。")
    print("おかげで寝ていたはずなのに、とても疲れている")
    print("どこかで「モウスコシダッタノニ……」と、誰かのこえが、きこえたきがした。")
    print("ゲームクリアです、脱出おめでとう！")


































    


