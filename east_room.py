import choice_east

#部屋の東側
def east():
    print("部屋の東側を見た。")
    print("壁には四枚のキャンバスが飾ってある。")
    print("それぞれのキャンバスの間に関連性は見受けられない。")
    print("選択肢を選んでください。")

    r_key = choice_east.command_canvas()

    return r_key

#東_星空のキャンバス
def canvas_star():
    print("星空の描かれたキャンバスを見た。")
    print("美しい夜空の絵画に心が癒される気がする。")
    print("しかし、とくに気になる点は見当たらない。")
    print("選択肢を選んでください。")

    r_key = choice_east.command_canvas_star()

    return r_key

#東_林檎のキャンバス
def canvas_apple():
    print("瑞々しく美しい真っ赤な林檎の描かれたキャンバスを見た。")
    print("絵画の中で林檎はいくつも並んでいるが、中央のひと際大きい林檎が一番美しく見える")
    print("しかし、少し美しすぎる気がしないでもない。")

    r_key = choice_east.command_canvas_star()

    return r_key


#東_林檎のキャンバス_東キー1（て（16））
def canvas_apple_touch(hp):
    print("林檎の絵に触れた瞬間、インクがどろりと溶けて毒々しい緑色に変色した。")
    print("絵に触れた指からしびれる様な痛みが走り、数秒動けなくなる")
    print("変色した林檎の上には「て（16）」と書かれている。")
    print("文字を確認し終えたら、いつのまにか林檎は元の美しい赤色に戻っている……。") 
    
    hp -= 2
    east_key = 1


    r_key = choice_east.command_canvas_key_apple()

    return r_key, hp,east_key


#東_真っ白なキャンバス
def canvas_void(hp):
    print("何も描かれていない真っ白なキャンバスを見た。")
    print("とくに気になる点はない……と思っていたら、キャンバスの中央に一本の黒い線が現れた")
    print("しばらく黒い線を眺めていたら、突然視界が歪み倒れそうになる。")
    print("……とても体がだるい。視界が歪む前に「何か」を見た気がするが、何を見たのかは覚えていない。")
    print("選択肢を選んでください。")
    
    hp -= 2
    r_key = choice_east.command_canvas_void()

   return r_key, hp

#東_薔薇のキャンバス
def canvas_rose(hp):
    print("血のように赤く美しい薔薇の描かれたキャンバスを見た。")
    print("完璧すぎる薔薇の絵に、つよくひきつけられる。")
    print("吸いよせられるように、しぜんと手が絵へとのびていく。")

    r_key = choice_east.command_canvas_rose()

    return r_key


#東_薔薇のキャンバス_東キー（す（5)）
def canvas_rose(hp):
    print("。")
    print("")
    print("。")

    r_key = choice_east.command_canvas_key_rose()

    return r_key


































    
