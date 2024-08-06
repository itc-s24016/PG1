def scope_test():
    #グローバル視点：ネステッドスコープ（scope_test視点：ローカルスコープ）
    def do_local():
        #ローカルスコープ
        s1 = "local   "
    def do_nonlocal():
        #ネステッドへスコープ
        nonlocal s2
        s2 = "nonlocal"
    def do_global():
        #グローバルへスコープ
        global s3
        s3 = "global  "
    s0 = s1 = s2 = s3 = "test    "
    do_local()
    print("After local    :", s0, s1, s2, s3)
    do_nonlocal()
    print("After nonlocal :", s0, s1, s2, s3)
    do_global()
    print("After global   :", s0, s1, s2, s3)

#グローバルスコープ
s0 = s1 = s2 = s3 = "initial "
print("In the global  :", s0, s1, s2, s3)
scope_test()
print("After func call:", s0, s1, s2, s3)
