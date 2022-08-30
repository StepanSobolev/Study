strt = b'r\xc3\xa9sum\xc3\xa9'

dec_strt = strt.decode()
print(dec_strt)

enc_strt = dec_strt.encode('Latin1')
print(enc_strt)

dec_2_strt = enc_strt.decode('Latin')
print(dec_2_strt)