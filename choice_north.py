#移動選択肢（部屋の北側の棚）
def command_shelf():
    while True:
        r_key = input("""top：一番上の棚を見る
center：中央の棚を見る
down：一番下の棚を見る
ce:部屋の中央に戻る\n""").strip()
        if r_key in ["top", "center", "down", "ce"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")

#シナリオ選択肢（北側＿狼のぬいぐるみ）
def command_top_shelf():
    while True:
        r_key = input("""red:赤いぬいぐるみに触れる
black：黒いぬいぐるみに触れる
white:白いぬいぐるみに触れる
no:部屋の北側に戻る\n""").strip()
        if r_key in ["red", "black", "white", "no"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")

#シナリオ選択肢（北側＿赤色狼のぬいぐるみ）
def command_red_wolf():
    while True:
        r_key = input("""black：黒いぬいぐるみに触れる
white:：白いぬいぐるみに触れる
no:部屋の北側に戻る\n""").strip()
        if r_key in ["black", "white", "no"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")


#シナリオ選択肢（北側＿黒色狼のぬいぐるみ）
def command_black_wolf():
    while True:
        r_key = input("""red：赤いぬいぐるみに触れる
white:：白いぬいぐるみに触れる
no:部屋の北側に戻る\n""").strip()
        if r_key in ["red", "white", "no"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")


#シナリオ選択肢（北側＿白色狼のぬいぐるみ）
def command_white_wolf():
    while True:
        r_key = input("""undo：縫い目をほどく
re：ぬいぐるみを元の位置に戻す\n""").strip()
        if r_key in ["undo", "re"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")

#シナリオ選択肢（北側＿脱出キー入手（狼「け」）
def command_key_white_wolf():
    while True:
        r_key = input("""re：ぬいぐるみを元の位置に戻す\n""").strip()
        if r_key in ["re"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")

#シナリオ選択肢（北側＿白色狼のぬいぐるみ_元の位置に戻す）
def command_return_white_wolf():
    while True:
        r_key = input("""red:赤いぬいぐるみに触れる
black：黒いぬいぐるみに触れる
no:部屋の北側に戻る\n""").strip()
        if r_key in ["red", "black", "no"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")

#シナリオ選択肢（北側＿中央の棚）
def command_center_shelf():
    while True:
        r_key = input("""top：一番上の棚を見る
down：一番下の棚を見る
ce:部屋の中央に戻る\n""").strip()
        if r_key in ["top", "down", "ce"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")


#シナリオ選択肢（北側＿一番下の棚＿子豚）
def command_down_shelf():
    while True:
        r_key = input("""large:左端の子ぶたのぬいぐるみに触れる
medium：中央の子ぶたのぬいぐるみに触れる
small：右端の子ぶたのぬいぐるみに触れる
no:部屋の北側に戻る\n""").strip()
        if r_key in ["large", "medium", "small", "no"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")


#シナリオ選択肢（北側＿大きいサイズの子ぶた）
def command_large_piglet():
    while True:
        r_key = input("""medium：中央の子ぶたのぬいぐるみに触れる
small：右端の子ぶたのぬいぐるみに触れる
no:部屋の北側に戻る\n""").strip()
        if r_key in ["medium", "small", "no"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")

#シナリオ選択肢（北側＿中サイズの子ぶた）
def command_medium_piglet():
    while True:
        r_key = input("""large:左端の子ぶたのぬいぐるみに触れる
small：右端の子ぶたのぬいぐるみに触れる
no:部屋の北側に戻る\n""").strip()
        if r_key in ["large", "small", "no"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")

#シナリオ選択肢（北側＿小サイズの子ぶた）
def command_small_piglet():
    while True:
        r_key = input("""move:子ぶたのぬいぐるみを動かす
large:左端の子ぶたのぬいぐるみに触れる
medium：中央の子ぶたのぬいぐるみに触れる
no:部屋の北側に戻る\n""").strip()
        if r_key in ["move", "large", "medium", "no"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")

#シナリオ選択肢（北側＿脱出キー入手（子ぶた「た」）
def command_key_small_piglet():        
    while True:
        r_key = input("""large:左端の子ぶたのぬいぐるみに触れる
medium：中央の子ぶたのぬいぐるみに触れる
no:部屋の北側に戻る\n""").strip()
        if r_key in ["large", "medium", "no"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")






















































            























            















            
