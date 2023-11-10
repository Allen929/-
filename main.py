import random
import xml.etree.ElementTree as ET

def load_settings():
    tree = ET.parse('C:/settings.xml')
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    n = int(root.find('n').text)
    return x1, x2, n

def save_settings(x1, x2, n):
    root = ET.Element("settings")
    ET.SubElement(root, "x1").text = str(x1)
    ET.SubElement(root, "x2").text = str(x2)
    ET.SubElement(root, "n").text = str(n)
    tree = ET.ElementTree(root)
    tree.write("settings.xml")

def play_game():
    x1, x2, n = load_settings()
    target_number = random.randint(x1, x2)
    attempts = 0

    print("歡迎來到猜數字遊戲！目標數字在", x1, "和", x2, "之間。")
    print("你有", n, "次機會猜測.")

    while attempts < n:
        guess = int(input("請猜一個數字："))

        if guess < target_number:
            print("太低了！")
        elif guess > target_number:
            print("太高了！")
        else:
            print("恭喜你猜對了！")
            break
        
        attempts += 1

    if attempts == n:
        print("抱歉，你已用完所有猜測次數。目標數字是", target_number)

if __name__ == "__main__":
    play_game()