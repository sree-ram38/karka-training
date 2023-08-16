# def flat(lis):
#     flatList = []
#     for element in lis:
#         if type(element) is list:
#             for item in element:
#                 flatList.append(item)
#         else:
#             flatList.append(element)
#         return flatList
# lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
# print('List', lis)
# print('Flat List', flat(lis))

lists=[[1,2,3,[4,5]],[6,7,[8,9]],[10,[11,12,13]]]
def print_nested_list(lists):
    for i in lists:
        if type(i)==list:
            print_nested_list(i)
        else:
            print(i,end=" ")
print_nested_list(lists)