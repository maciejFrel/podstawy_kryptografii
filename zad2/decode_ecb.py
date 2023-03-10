from utils import *

encodedMessageFile = open('encoded_message.txt', 'rb')
keyStr = input('key: ')
encodedMessage = encodedMessageFile.read()
[print(x) for x in sliceIntoBlocks(encodedMessage)]

key = strToBytes(keyStr)

message = aesDecodeEcb(encodedMessage, key)
messageStr = bytesToStr(unfill(message))
print(messageStr)

encodedMessageFile.close()