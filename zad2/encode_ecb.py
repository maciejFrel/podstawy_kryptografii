from utils import *

messageFile = open('message.txt', 'r')
encodedMessageFile = open('encoded_message.txt', 'wb')
keyStr = input('key: ')
messageStr = messageFile.read()
message, key = strToBytes(messageStr), strToBytes(keyStr)

# print(len(message), len(messageStr), len(fillToBlockSize(message)))

encodedMessage = aesEncodeEcb(message, key)
# [print(x) for x in sliceIntoByteGroups(encodedMessage)]
encodedMessageFile.write(encodedMessage)

messageFile.close()
encodedMessageFile.close()