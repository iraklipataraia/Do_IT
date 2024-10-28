'''
შექმენით ბიბლიოთეკის მართვის ფუნქცია(ები)


თქვენ უნდა შექმნათ ფუნქცია ან ფუნცქიები რომლის საშუალებითაც მომხმარებელი შეძლებს წიგნების დამატებას წაშლას პითონის პროგრამის შექმნა წიგნების პატარა ბიბლიოთეკის სამართავად.
 პროგრამამ უნდა მისცეს მომხმარებლებს შემდეგი მოქმედებების შესრულება:
1. წიგნის დამატება,

2. წიგნის მოძებნა ავტორის მიხედვით

3. წიგნის მოძებნა სათაურის მიხედვით ამისთვის აუცილებელია გამოიყენოთ ლექსიკონები

'''

#
# library = {}
#
# def add_book(title, author):
#     library[title] = author
#     print(f'book {title} is added in library')
#
# def search_by_author(author):
#     for key, value in library.items():
#         if value == author:
#             print(f'{author} is in library')
#         else:
#             print(f'{author} is not in library')
#
# def search_by_title(title):
#     if title in library:
#         print(f'{title} is in library')
#     else:
#         print(f'{title} is not in library')
#

with open("test.txt", "w") as x:
    for i in range(1000):
        line_count = len
        x.write('test\n')


with open("test.txt","r") as y:

    print(y.read())