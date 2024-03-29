#移動選択肢（部屋の中央用）
def sentaku1():
    while True:
        r_key = input("""no:部屋の北側を見る
so:部屋の南側を見る
ea:部屋の東側を見る
we:部屋の西側を見る\n""").strip()
        if r_key in ["no", "so", "ea", "we"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")

#移動選択肢（部屋の南）
def sentaku2():
    while True:
        r_key = input("""no:部屋の北側を見る
ea:部屋の東側を見る
we:部屋の西側を見る
ce：部屋の中央に戻る\n""").strip()
        if r_key in ["no", "ea", "we", "ce"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")


#移動選択肢（部屋の南）
def sentaku3():
    while True:
        r_key = input("""no:部屋の北側を見る
so:部屋の南側を見る
ea:部屋の東側を見る
ce：部屋の中央に戻る\n""").strip()
        if r_key in ["no", "so", "ea", "ce"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")



















            
