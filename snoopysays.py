import sys

try:
    arg1 = sys.argv[1]
except IndexError:
    print("No arguments provided")
    exit(1)

print(rf"""
  <{arg1}>
    \
     \
      \
      　  ●
      　　/⌒ヽ
      　 ｜ 　|/⌒ヽ(ヽ
      　 (｀　∥ー⌒) |
      　|￣||￣￣￣￣￣|
      　|―||―――――|
      　|　Ｕ　　　　　|
      　|￣￣￣￣￣￣￣|
      　|＿＿＿＿＿＿＿|
      　　|―――――|
      　　|―――――|""")
