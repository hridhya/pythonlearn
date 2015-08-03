text = "X-DSPAM-Confidence:    0.8475"
value = text.find(':')
print float(text[value+1:])