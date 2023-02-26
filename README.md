# Patchouli
LINEトーク履歴解析ライブラリ・Patchouli(パチュリー)
## About
LINEで書き出したトーク履歴をパースします。  
トーク履歴は、OSによって保存方式が違います。Patchouliでは、AndroidとWindowsをサポートしています。
## Install
```sh
$ pip install git+https://github.com/nakasyou/Patchouli.git
```
## How to use it?
```python
import patchouli

with open("talk.txt") as f:
    result=patchouli.Parse(
        f.read(), #トーク履歴のテキストデータ
        patchouli.modes.ja.android # modeを指定。ここではAndroid.
    )
    print(result)
```
resultは、```Parse```クラスのインスタンスとなります。  
1番目のトークを取り出したいなら  
```python
first=result[0]
```
と記述できます。
firstの内容は、```patchouli.Seq```クラスのインスタンスになっています。  
このインスタンスから、情報を取り出すことができます。  
```python
first.user # ユーザー名
first.time # 日時(datetime.datetime)
first.seq  # 本文
```
## Detail
### patchouli.modes
#### patchouli.modes.Mode
- モード作成用クラス
- ```patchouli.modes.Mode(**options)```
#### patchouli.modes.ja
##### patchouli.modes.ja.windows
- windows用モード
##### patchouli.modes.ja.android
- android用モード
### patchouli.Parse
- パースのクラス
- ```patchouli.Parse(text,mode=patchouli.modes.windows)```
