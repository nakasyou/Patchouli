# Patchouli
[![PyPI version](https://badge.fury.io/py/pypatchouli.svg)](https://badge.fury.io/py/pypatchouli)  
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
import pypatchouli as patchouli

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
firstの内容は、```pypatchouli.Seq```クラスのインスタンスになっています。  
このインスタンスから、情報を取り出すことができます。  
```python
first.user # ユーザー名
first.time # 日時(datetime.datetime)
first.seq  # 本文
```
## Detail
### pypatchouli.modes
#### pypatchouli.modes.Mode
- モード作成用クラス
- ```pypatchouli.modes.Mode(**options)```
#### pypatchouli.modes.ja
##### pypatchouli.modes.ja.windows
- windows用モード
##### pypatchouli.modes.ja.android
- android用モード
### pypatchouli.Parse
- パースのクラス
- ```pypatchouli.Parse(text,mode=patchouli.modes.windows)```
