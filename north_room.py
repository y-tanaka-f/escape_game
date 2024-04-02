import choice_north
import center_room

#部屋の北側
def north():
    print("部屋の北側だ。")
    print("沢山のぬいぐるみが並んだ棚飾りがある")
    print("一番下には三匹の子ぶた、中央には七ひきの子ヤギ、一番上には3匹の狼のぬいぐるみが置かれているようだ")
    print("選択肢を選んでください。")

    r_key = choice_north.command_shelf()

    return r_key



#棚の一番上（三匹の狼のぬいぐるみ置き場）
def top_shelf():
    print("一番上の棚を見た。")
    print("赤色・黒色・白色の狼のぬいぐるみが置いてある。")
    print("赤色と白色のぬいぐるみだけ腹が大きい気がする。")
    
    r_key = choice_north.command_top_shelf()

    return r_key


#赤色おおかみのぬいぐるみの確認
def red_wolf(hp):
    print("赤い狼のぬいぐるみに触れようと手を伸ばした。")
    print("突然狼のぬいぐるみが動き出し、腕に嚙みついてきた！")
    print("慌てて振り払うとぬいぐるみは奇妙な笑い声をあげながら、何事もなかったかのように元の棚の位置に戻っていった……。")
    hp -= 3   

    print(f"現在のHP：{hp}/15")
    r_key = choice_north.command_red_wolf()

    return(r_key,hp)


#黒色おおかみのぬいぐるみの確認
def black_wolf():
    print("黒い狼のぬいぐるみに触れた。")
    print("シルクのような手触りでとても気持ちが良い。")
    print("しかしとくに気になる点は見つからない。")

    r_key = choice_north.command_black_wolf()

    return(r_key)


#白色おおかみのぬいぐるみの確認
def white_wolf():
    print("白い狼のぬいぐるみに触れた。")
    print("他の狼と違ってとても重く、腹の部分がゴツゴツしている。")
    print("どうやら腹の部分に荒い縫い目があるようだ。")
    print("……縫い目をほどいてみようか？")


    r_key = choice_north.command_white_wolf()

    return(r_key)


#白色おおかみのぬいぐるみ_縫い目をほどく
def white_wolf_undo():
    print("赤い糸をほどいてぬいぐるみの腹を開いた。")
    print("中にはいくつかの小石と白い紙が入っていた。")
    print("紙には「け（12）」と文字が書かれている。")
    print("文字を確認すると紙は消え、ぬいぐるみの腹もいつのまにか元に戻っていた。")

    north_key = 1

    r_key = choice_north.command_key_white_wolf()

    return(r_key, north_key)



#白色おおかみのぬいぐるみ_元の位置に戻す
def white_wolf_return():
    print("重いぬいぐるみを元の位置に戻した。")

    r_key = choice_north.command_return_white_wolf()

    return(r_key)


#棚の中央（七匹の子ヤギのぬいぐるみ置き場）
def center_shelf():
    print("棚の中央を見た。")
    print("白い子ヤギが七匹並んで座っている。")
    print("全員小石を両手で抱えているようだ。")
    print("それ以外にはとくに変わった様子は見られない。")
    
    r_key = choice_north.command_center_shelf()

    return(r_key)


#棚の一番下（三匹の子豚のぬいぐるみ置き場）
def down_shelf():
    print("棚の一番下を見た。")
    print("サイズの異なる三匹の子ぶたのぬいぐるみが置かれている。")
    print("左端の子ぶたが一番大きく、右端の子ぶたが一番小さいようだ。")
    print("それぞれ左から赤いベスト、赤いベスト、白いベストと着こんでいる")

    
    r_key = choice_north.command_down_shelf()

    return(r_key)


#大サイズの子ぶたのぬいぐるみの確認
def large_piglet(hp):
    print("一番大きい子ぶたのぬいぐるみに触れた。")
    print("すると、突然子ぶたのぬいぐるみから薄い刃が何本も飛ばされ、手を切ってしまった！")
    print("手を離すとぬいぐるみは先ほどと同じ状態に戻った……。")
          
    hp -= 1   

    print(f"現在のHP：{hp}/15")
    r_key = choice_north.command_large_piglet()
    
    return(r_key,hp)

#中サイズの子ぶたのぬいぐるみの確認
def medium_piglet(hp):
    print("中ぐらいの子ぶたのぬいぐるみに触れた。")
    print("直後、子ぶたのぬいぐるみは高熱となり手を火傷してしまった！")
    print("手を離すとぬいぐるみは先ほどと同じ状態に戻った……。")

    hp -= 2   

    print(f"現在のHP：{hp}/15")
    r_key = choice_north.command_medium_piglet()

    return(r_key,hp)

#小サイズの子ぶたのぬいぐるみの確認
def small_piglet():
    print("一番小さい子ぶたのぬいぐるみに触れた。")
    print("よく見ると小さい子ぶたが座っている部分だけ白いレンガになっている。")

    r_key = choice_north.command_small_piglet()

    return(r_key)    


def small_piglet_move():
    print("子ぶたのぬいぐるみを動かすと、白いレンガに文字が書かれているのが見えた。")
    print("レンガには「た（8）」と書かれている。")
    print("文字を確認し終えたとおもったら、いつのまにか子ぶたのぬいぐるみが元の位置に戻っている……。")

    north_key = 1

    r_key = choice_north.command_key_small_piglet()

    return(r_key,north_key)





















