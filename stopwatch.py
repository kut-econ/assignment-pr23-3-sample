# 以下にクロージャstopwatchを定義してください。
# %%
import time
def stopwatch():
    stopped = True      # 停止中ならTrue
    start = None        # 計測開始時刻
    def inner():
        nonlocal stopped,start
        # ここにコードを書いてプログラムを完成させて
        # ください。
        # 
        # ヒント1：time.time()関数により、現在の時刻が
        # 秒単位で返されますので、これを利用してください。
        # ヒント2：stoppedがTrueかFalseかで動作を分けて
        # ください。Trueは停止中、Falseは計測中です。
        # ヒント3: 停止中の場合、startに現在時刻を記録
        # して、stoppedをFalse（動作中）にします。逆に
        # 動作中の場合は、どうすればよいか考えてみて
        # ください。何度でも繰り返し計測できるようにする
        # には、どうすればよいでしょうか？
    return inner

# %%

