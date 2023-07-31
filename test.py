# こちらのテストスクリプトは、作成したfiboとstopwatch
# の動作をテストするのに使ってください。このファイルの
# 内容は採点には無関係です。
# %%
import fibo
import stopwatch
# 注) モジュールを書き換えたときは、Pythonを再起動しないと
# 変更が反映されないので気を付けてください。
# %%
# fiboのテスト
# fiboの引数をいろいろ変更して試してみてください。
fb = fibo.fibo(1,3)
for i in range(10):
    print(next(fb),end=',')
else:
    print(next(fb))
# %%
# stopwatchのテスト
sw = stopwatch.stopwatch()
# %%
# 計測開始、停止
# 通常のストップウォッチと同じく、同じ操作で何度でも
# 計測開始と停止ができます。
sw()
