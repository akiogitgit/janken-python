import random
import sys

# 定数
hands = {"rock": 1, "scissors": 2, "paper": 3}

totalGameCount = 5 # ゲーム数
gameStatuses = [1,2,3] # 0: あいこ、1: 勝ち、2: 負け
# gameStatuses = {"draw": 1, "win": 2, "lose": 3}
gameModes = [1,2] # 1: 


# ゲームモードを設定
def getGameMode():
    inputNumber = input("ゲームモードを選択: 1. CPU vs CPU 2. CPU vs USER")
    
    # 入力が数字かチェック
    try:
        inputNumber = int(inputNumber)
    except Exception as e:
        print("正しい手を入力してください")
        sys.exit() # 終了
        
    # 入力が1~3かをチェック
    if inputNumber < hands["rock"] or inputNumber > hands["paper"]:
        print("正しい手を入力してください")
        sys.exit() # 終了
    
    return inputNumber

# 名前の入力を取得
def getInputName():
    name = input("名前を入力してください")
    return name

# じゃんけんの手の入力を取得
def getInputHand(gameCount: int):
    inputNumber = input("{}回戦目: 何を出しますか？数字で入力してください。1.グー 2.チョキ 3.パー".format(gameCount))
    
    # 入力が数字かチェック
    try:
        inputNumber = int(inputNumber)
    except Exception as e:
        print("正しい手を入力してください")
        sys.exit() # 終了
        
    # 入力が1~3かをチェック
    if inputNumber < hands["rock"] or inputNumber > hands["paper"]:
        print("正しい手を入力してください")
        sys.exit() # 終了
    
    return inputNumber

# 両者の勝敗をチェック
# 返り値　1: あいこ、2: p1の勝ち、3: p1の負け
def checkWinner(player1Hand: int, player2Hand: int):
    # print(player1Hand,player2Hand)
    if player1Hand == player2Hand:
        return 1

    # if player1Hand == hands[0] and player2Hand == hands[1] or player1Hand == hands[1] and player2Hand == hands[2] or player1Hand == hands[2] and player2Hand == hands[0]:
    #     return 2
        
    if (player1Hand == hands[0] and player2Hand == hands[1] or
        player1Hand == hands[1] and player2Hand == hands[2] or
        player1Hand == hands[2] and player2Hand == hands[0]
        ):
        return 2
    
    return 3

# 勝敗からメッセージを生成
def generateResultMessage(resulutStatus: int, player1Name: str):
    if resulutStatus == 1:
        return "あいこなのでもう一回"
    if resulutStatus == 2:
        return player1Name + "の勝ち"
    if resulutStatus == 3:
        return player1Name + "の負け"

# じゃんけんをして結果を表示
def playGame(gameCount: int, player1Name: str):
    # 手を取得
    # cpuHand = random.randint(hands[0], hands[2])
    cpuHand = 1
    playerHand = getInputHand(gameCount)
    
    # じゃんけん結果を取得
    resultStatus = checkWinner(playerHand, cpuHand)
    resultMessage = generateResultMessage(resultStatus, player1Name)
    
    print(resultMessage)
    
    # あいこならもう一回やる
    if resultStatus == 1:
        playGame(gameCount, player1Name)
    

# 連続でゲームを実行
for gameCount in range(1, totalGameCount + 1):
    # 名前の入力
    player1Name = getInputName()
    # ゲームをする
    playGame(gameCount, player1Name)
    
    print("")
