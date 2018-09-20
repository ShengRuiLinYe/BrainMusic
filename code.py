import hashlib
import base64
import qrcode
import sys
condition = True
while condition:
    print("NOTICE: input 'sha256' to encrypt string in sha256 way;\n"
          "        input 'qr code' to produce a QR code in this category\n"
          "        input 'base64' to base64 mode;\n"
          "        input 'q' to exit"
          "REMINDER: you only need to input the comment within '', but not contain ''")

    order = input().lower()

    if order == 'q':
        sys.exit()
    elif order == 'sha256':
        print("please input the string you wanna encrypt:")
        try:
            string = input().encode('utf-8')
            print("the string has been encrypted:",str(hashlib.sha256(string).digest()))
        except TypeError:
            print("this strange string can't be encryted now, sorry.")
    elif order == 'base64':
        print("Welcome to base64, you can choose encrypt with 'e'  or decrypt with 'd'")
        choice = input()
        if choice == 'e':
            print("please input the string you wanna encrypt:")
            try:
                string = input().encode('utf-8')
                encoded = base64.b64encode(string)
                print("the string has been encrypted:", str(encoded))
            except TypeError:
                print("this strange string can't be encryted now, sorry.")

        elif choice == 'd':
            print("please input the string you wanna encrypt:")
            try:
                string = input().encode('utf-8')
                decoded = base64.b64decode(string)
                print("the string has been encrypted:", str(decoded))
            except TypeError :
                print("this strange string can't be decryted now, sorry.")
        else:
            print("sorry, you entered wrong instruction.")

    elif order == 'qr code':
        print("please input the string you wanna produce QR code:")
        data = input()
        img = qrcode.make(data)
        img.save("qr code.png")
        print("you can find it in this work category")

    else:
        print("check your input, it is wrong! Try again.")
