fraza = input()
vowels = "а, я, у, ю, о, е, ё, э, и, ы"
list_fraz = fraza.split()
_set = set()

for i in list_fraz:
    countVowels = 0
    for s in i:
        if vowels.find(s) >= 0:
            countVowels+= 1
    _set.add(countVowels)
if len(_set) = 1:
    print("Парам пам-пам")
else:
    print("Пам парам")