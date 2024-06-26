import choice_game

#料理の残り個数の初期値辞書
eat_list = {"おにぎり":1, "サンドイッチ":3, "ステーキ弁当":4, "青汁":7}


#部屋の中央の関数
def center():
    print("部屋の中央だ。")
    print("部屋は薄暗く、窓や扉といった出入口は見当たらない。")


    if len(eat_list) == 0:
        print("ここで他に見るものはなさそうだ。")
        print("選択肢を選んでください。")
        r_key = choice_game.sentaku1()

    else:
        while True:
            print("選択肢を選んでください。")
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
        r_key = choice_game.sentaku1()
        
    else:
        print("テーブルの上にはいくつかの料理が乗っている。")
        print("脱出の手がかりはないようだが、料理を食べることで体力は回復できそうだ。")
        print("選択肢を選んでください。")
        while True:
            #料理一覧とそれぞれのHP回復量を表示
            print(f"現在のHP：{hp}/15")
            for i in eat_list:
                print(f"{i}：HP回復量{eat_list[i]}")
            eat_key = input("ce:食べずに部屋の中央へ戻る。\n")

            if eat_key in "ce":
                r_key = eat_key
                break

            elif hp >= 15:
                print("お腹がいっぱいで料理を食べられそうにない。\nまた後で食べよう。")
            
                r_key = str(choice_game.sentaku1())
                break
        
            elif eat_key in eat_list:
                hp += eat_list[eat_key]
                print(f"体力が{eat_list[eat_key]}回復した")
                if hp >= 15:
                    hp = 15
                    print(f"現在の体力は{hp}/15だ")
                    del eat_list[eat_key]
                    print("選択肢を選んでください。")            
                    r_key = choice_game.sentaku1()
                    break

                else:
                    print(f"現在の体力は{hp}/15だ")
                    print("選択肢を選んでください。")
                    while True:
                        r_key = input("""no:部屋の北側を見る
so:部屋の南側を見る
ea:部屋の東側を見る
we:部屋の西側を見る
cc：もう一度料理を食べる\n""")
                        if r_key in ["no", "so", "ea", "we", "cc"]:
                            break
                        else:
                            print("正しい選択肢を入力してください")
                            
                    break
                                    
            else:
                print("その料理はありません")
        
        return(r_key,hp) 
        






































    


