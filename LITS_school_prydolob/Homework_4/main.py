from dec import dec_b, dec_u, dec_i, not_error

@dec_b
@dec_i
@dec_u
@not_error
def return_str(f_text):
    return f_text


text = 'str'

print(return_str(text))
print(return_str(text))