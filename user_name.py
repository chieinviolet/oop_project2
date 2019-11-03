"""
※雰囲気コード
データ型宣言: UserName  <<python ではクラス型と呼ばれる。
    属性:
      実際のユーザー名
    ルール:
      ・ユーザー名は4文字以上20文字以下である
    できること
      ・ユーザー名を大文字に変換する
"""


class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}は文字数違反やで！')

        self.name = name

    def screen_name(self):
        return self.name.upper()


# UserNameクラスのインスタンス化
hibiki = UserName(name='Hibiki')

# print (hibiki)
# print(type (hibiki))<<<<<type がUserNameになる！？
# print(hibiki.name)

# <<<<UserNameクラスのインスタンス化
# sho = UserName(name = 'Sho')
# print(sho.name)

# こんなんあったらうれしい！から入る。option + enter で実装。
print(hibiki.screen_name())
