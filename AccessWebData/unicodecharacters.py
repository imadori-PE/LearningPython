# 
# TODO Representing simple strings
# * each character is represented by a number between 0 and 256
# * we refer 8 bits in memory as a byte of memory
# * the ord() function tell us the numeric value of a simple ASCII

print(ord('G'),ord('H')) # * ordinal
# *  ASCII only 128 characters

print(chr(108),chr(105), chr(110), chr(101), chr(42))

# ? Unicode has a lot of characters
# ? UTF-8 is the best practice for encoding data moving between system 
# ? python 3, all strings internally are UNICODE
# ? when we talk to an external resource like a networkd socket we sends bytes
