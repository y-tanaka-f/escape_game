import choice_game
#部屋の南
def south(hp):
    print("南側の壁を見た。")
    print("壁は赤い手形で埋め尽くされている。所々に爪痕があるようだ。")
    print("脱出の手がかりは……残念ながら見つからない。")
    print("壁を見たことで気分がわるくなり、体力が1減ったようだ。")

    hp -= 2
    
    print(f"現在のHP：{hp}/15")
    print("選択肢を選んでください。")

    r_key = choice_game.sentaku2()


    return(r_key,hp)
