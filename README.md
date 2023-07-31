# 課題3

以下で、二つのPythonスクリプトfibo.py、stopwatch.pyを作成していただきます。作成できたら、スクリプトtest.pyから二つのスクリプトをモジュールとして読み込み、動作をテストしてください。正しく動作することが確認できたら提出してください。

## 3-1

ジェネレータに関する課題です。漸化式

```python
a[i+2] = a[i] + a[i+1]
```

に従う数列を順番に返すジェネレータ`fibo`を定義したスクリプト`fibo.py`を作成してください。

注) 上の式で、`a[i]`はPythonのリストではなく、単なる数列`a`の`i`番目を表す記号です。

なお、初項は`a[0]`であり、`fibo`は、`a[0]`と`a[1]`の値を引数にとります。例えば、次のようにジェネレータオブジェクトを作成して変数`fb`に代入したとします。

```python
import fibo
fb = fibo.fibo(1,3)
```

この場合、1回目の`next(fb)`の戻り値は1、2回目は3、3回目は4、4回目は7となり、以下次のように続いていきます。

```bash
1,3,4,7,11,18,29,47,76,...
```

3番目以降の数は、いずれも前二つの数の和になっていることに注意してください。`next(fb)`の呼び出しは任意の回数可能であるとします。

## 3-2

クロージャに関する課題です。次のようなストップウォッチ機能をもったクロージャを定義したスクリプト`stopwatch.py`を作成してください。このクロージャは一度呼び出すと"Running..."と画面に出力して時間の計測を開始し、2回目に呼び出すと、"Stopped."と出力して、1回目の呼び出しから2回目の呼び出しまでに経過した秒数を**戻り値として**返します。また、同じように何度でも時間を計測することができます。

より具体的には、以下のようにインターラクティブモードもしくはREPLで使用します。

```python
# 準備
>>> import stopwatch
>>> sw = stopwatch.stopwatch()
```

```python
# 計測開始(1回目のswの呼び出し)
>>> sw()
Running...
```

```python
# 計測終了(2回目のswの呼び出し)
>>> sw()      
Stopped.
2.08023738861084
```

ヒント：`time`モジュールの`time`関数によって、現在時刻を秒で取得することができますので、これを活用してください。