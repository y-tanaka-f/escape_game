#移動選択肢（部屋の東側の壁）
def command_canvas():
    while True:
        r_key = input("""star：星空の描かれたキャンバスを見る
apple：瑞々しい真っ赤な林檎の描かれたキャンバスを見る
void：何も描かれてないように見える真っ白なキャンバスを見る
rose:血のように赤く美しい薔薇の描かれたキャンバスを見る
ce:部屋の中央に戻る\n""").strip()
        if r_key in ["star", "apple", "void", "rose", "ce"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")

def command_canvas_star():
    while True:
        r_key = input("""apple：瑞々しい真っ赤な林檎の描かれたキャンバスを見る
void：何も描かれてないように見える真っ白なキャンバスを見る
rose:血のように赤く美しい薔薇の描かれたキャンバスを見る
ce:部屋の中央に戻る\n""").strip()
        if r_key in ["apple", "void", "rose", "ce"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")


def command_canvas_apple():
    while True:
        r_key = input("""touch：中央の林檎の絵に触れてみる
star：星空の描かれたキャンバスを見る
void：何も描かれてないように見える真っ白なキャンバスを見る
rose:血のように赤く美しい薔薇の描かれたキャンバスを見る
ce:部屋の中央に戻る\n""").strip()
        if r_key in ["apple", "void", "rose", "ce"]:
            return r_key
        else:
            print("正しい選択肢を入力してください")




            









































































            















            
