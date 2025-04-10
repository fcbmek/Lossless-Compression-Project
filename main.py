
option = input("Choose one of the lossless data compression algorithmics 1 for huffman coding or 2 for lzw\n")


if option == '1':
    print("huffman coding:")
    exec(open("huffman.py").read())
elif option == '2':
    print("lzw algorithm:")
    exec(open("lzw.py").read())
else: print("error")


