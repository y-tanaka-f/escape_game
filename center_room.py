import choice_game
#料理の残り個数の初期値辞書
eat_list = {"おにぎり":1, "サンドイッチ":1, "ステーキ弁当":2, "青汁":3}


#部屋の中央の関数
def center():
    print("部屋の中央だ。")
    print("部屋は薄暗く、窓や扉といった出入口は見当たらない。")
    print("選択肢を選んでください。")

    if len(eat_list) == 0:
        r_key = choice_game.sentaku1()

    else:
        while True:
            r_key = input("""cc:テーブルを見る
no:部屋の北側を見る
so:部屋の南側を見る
ea:部屋の東側を見る
we:部屋の西側を見る\n""").strip()
            if r_key in ["no", "so", "ea", "we", "cc"]:
                return r_key
            else:
                print("正しい選択肢を入力してください")

#中央テーブルを見る
def center_cook(hp):
    if len(eat_list) == 0:
        print("テーブルの上には何もない。食事は全て食べてしまっている。")
        print("選択肢を選んでください。")
        r_key = str(choice_game.sentaku1())
        
    else:
        print("テーブルの上にはいくつかの料理が乗っている。")
        print("脱出の手がかりはないようだが、料理を食べることで体力は回復できそうだ。")

        #料理一覧とそれぞれのHP回復量を表示
        for i in eat_list:
            print(f"{i}：HP回復量{eat_list[i]}")

        while True:
            eat_key = input(str("食べる料理を選んでください。\n"))
            if hp >= 15:
                print("お腹がいっぱいで料理を食べられそうにない。\nまた後で食べよう。")
            
                r_key = str(choice_game.sentaku1())

                break
        
            elif eat_key in eat_list:
                hp += eat_list[eat_key]
                if hp >= 15:
                    hp = 15
                
                    print(f"体力が{eat_list[eat_key]}回復した")
                    print(f"現在の体力は{hp}/15だ")


                    del eat_list[eat_key]

                if hp >= 15:            
                    print("選択肢を選んでください。")
            
                    r_key = choice_game.sentaku1()
                    break

                else:
                    print("選択肢を選んでください。")
                    while True:
                        r_key = input("""no:部屋の北側を見る
so:部屋の南側を見る
ea:部屋の東側を見る
we:部屋の西側を見る
eat：もう一度料理を食べる\n""")
                        if r_key in ["no", "so", "ea", "we", "ce"]:
                            break
                        else:
                            print("正しい選択肢を入力してください")
                                    
            else:
                    print("その料理はありません")
        
        return(r_key,hp) 
        






































    

