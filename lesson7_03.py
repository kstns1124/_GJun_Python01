import random as rnd

def play():
    print("==========猜數字遊戲==========\n\n")
    max = 100
    min = 1
    tar = rnd.randrange(min, max);
    ct = 0
    print(tar)
    while(True):
        try:
            guess = int(input(f"第{(ct+1)}次，請輸入數字({min}~{max}):"))
        except:
            print("輸入非數字")
        else:
            ct += 1
            if(guess == tar):
                print(f"猜中了，您已經猜測{(ct)}次，答案是{tar}!")
                break;
            elif(guess > tar):
                max = guess - 1
                print(f"猜錯了，答案比猜測數值小，您已經猜測{ct}次")
            else:
                min = guess + 1
                print(f"猜錯了，答案比猜測數值大，您已經猜測{ct}次")



con = "Y"
while (con.upper() == "Y"):
    play()
    while True:
        con = input("是否再玩一次?(Y/N):")
        if(con.upper() == "Y") or (con.upper() == "N"):
            break
print("遊戲結束");
