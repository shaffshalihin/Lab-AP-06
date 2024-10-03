kata = input("kata = ")
def kata_akronim(kata):
    hasil=kata.split(" ")
    for i in hasil :
        print(i[0],end="")
kata_akronim(kata)