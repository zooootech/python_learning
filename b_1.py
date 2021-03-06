# 多数決
# https://atcoder.jp/contests/past202004-open/tasks/past202004_b

# -------------------------------------------------

# count() メソッドと max() 関数を使用
S = input()

# str.count(sub[, start[, end]])
# 文字列メソッドである count() は、 [start, end] の範囲に、部分文字列 sub が重複せず出現する回数を返します。
na = S.count("a")
nb = S.count("b")
nc = S.count("c")

# max(iterable, *[, key, default])
# max(arg1, arg2, *args[, key])
# 組み込み関数である max() は、 iterable の中で最大の要素、または 2 つ以上の引数の中で最大のものを返します。
mx = max(na, nb, nc)

if mx == na:
  print("a")
elif mx == nb:
  print("b")
else:
  print("c")

# -------------------------------------------------

S = input()

na = 0
nb = 0
nc = 0

for x in S:
  if x == "a":
    na += 1
  elif x == "b":
    nb += 1
  else:
    nc += 1

if na > nb and na > nc:
  print("a")
elif nb > na and nb > nc:
  print("b")
else:
  print("c")