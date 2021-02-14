import io
try:
    my_file= open("REDME.TXT", 'r', encoding='utf-8')
    content = my_file.write("יקי זה Yaki\n")
    my_file.seek(0)
    print(y)
except io.UnsupportedOperation as e:
    print(e)
print(content)
my_file.close()

