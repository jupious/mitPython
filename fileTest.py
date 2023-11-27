f = open("test_log.txt",'w', encoding='utf8')
for i in range(1,11):
    data = "%d번째 줄.\n"%i
    f.write(data)
f.close