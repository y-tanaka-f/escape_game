import choice_game
#部屋の西
def west(hp):
    print("西の壁を見た。")
    print("壁には何もなく白で塗りつぶされている。")
    print("なにかの視線を感じる気がするが、気のせいだろうか。")
    print("ずっと壁を見ていたら何かに吸い込まれてしまいそうな気分になる")
    print("脱出の手がかりは……残念ながら見つからない。")
    print("壁を見たことで気分がわるくなり、体力が3減ったようだ。")

    hp -= 3
    
    print(f"現在のHP：{hp}/15")
    print("選択肢を選んでください。")

    r_key = choice_game.sentaku3()


    return(r_key,hp)
