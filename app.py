import random


def main():
    f = open("members.txt", mode="r")
    text = f.read()

    f.close()

    # テキストを改行で区切ってリスト化
    lines = text.split("\n")
    print(lines)

    print("=================================================================================================")

    # 改行(\n)で区切る(split) <- OK

    # random.sample(x, k) <- 重複無しのランダム
    print(f"Table1: {random.sample(lines, 6)}")
    print(f"Table2: {random.sample(lines, 5)}")
    print(f"Table3: {random.sample(lines, 4)}")

    # print(f"Table2: {random.choice(lines)}, {random.choice(lines)}, {random.choice(lines)}")
    # print(f"Table3: {random.choice(lines)}, {random.choice(lines)}, {random.choice(lines)}")

    print("=================================================================================================")


if __name__ == "__main__":
    main()
