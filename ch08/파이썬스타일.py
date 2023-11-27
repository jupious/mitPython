a, b, c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)
print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])

test = 'aaa bbb ccc'
test.split()
print(test)

print("=====================================================")

dog_song = "my dog has brown eyes, my dog is cute"
print({i:j for j,i in enumerate(dog_song.split())}) #print에 {}로 묶어서 딕셔너리

f = lambda x : x/2
print (list(map(f,[1,2,3,4,5])))

print("=====================================================")
def asterisk_test(a, args):
    print(a, *args)
    print(type(args))
asterisk_test(1, {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
