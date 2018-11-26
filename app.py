def main():
    f = open("members.txt", mode="r")
    text = f.read()
    print(text)

    f.close()


if __name__ == "__main__":
    main()
