a = str(input())
SearchFirst = a.find('f')
SearchLast = a.rfind('f')
if SearchFirst == -1:
    print()
elif SearchFirst != -1:
    if SearchFirst == SearchLast:
        print(SearchLast)
    else:
        print(SearchFirst, SearchLast)
