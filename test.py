msg = "   Hello, my NAME is vLAd! Today is a GREAT day!!!   "
msg1 = msg.strip()
print(msg1)
msg2 = msg1.lower().capitalize()
print(msg2)
msg3 = msg2.rstrip("!") + "!"
print(msg3)
msg4 = msg3.index("Hello")
print(msg4)

before, sep, after = msg3.partition("is")
print(before)
print(sep)
print(after)