vote_num = 0
def vote():"票の追加"
    print("投票します")
    global vote_num
    vote_num += 1
    
def reset_box():"全ての票を取り消す"
    global vote_num
    print("箱を空にします")
    vote_num = 0
    
def check_box():"現在の箱の状態を見る"
    global vote_num
    print("票の数は{}です".format(vote_num))




"paiza.ioでのみ正しく動く"
vote()
check_box()

vote()
check_box()

for i in range(3):
    vote()
    
check_box()
reset_box()
check_box()
