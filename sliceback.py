#        01234567890123456789012345
letters="abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]
print(backwards)

#qpo
backwards= letters[16:13:-1]
print(backwards)
#edcba
backwards= letters[4::-1]
print(backwards)
#last 8 characters
backwards=letters[:17:-1]
print(backwards)

#idioms
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
