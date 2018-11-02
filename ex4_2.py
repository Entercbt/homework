c,n,b,o =0,0,0,0
strs = input("请随意输入一行字符，包含字母，数字，空格或其他字符：")
for s in strs:
    if ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z'):
        c += 1
    elif ord('0') <= ord(s) <= ord('9'):
        n += 1
    elif ord(' ') == ord(s):
        b += 1
    else:
        o += 1
print("包含字母{0}个，数字{1}个，空格{2}个，其他字符{3}个".format(c,n,b,o))
