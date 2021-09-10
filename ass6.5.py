text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('0')
num=float(text[pos:pos+10])
print(num)
