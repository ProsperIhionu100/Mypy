# from bs4 import BeautifulSoup

# with open("assign.html",'r') as html_file:
#     content =html_file.read()
    
#     soup = BeautifulSoup(content, 'lxml')
#     # Courses_html_tag =soup.find_all('h1')
#     # for course in Courses_html_tag:
#     #     print(course)
#     course_cards = soup.find_all("div")
#     for course in course_cards:
#         course_name = course.h5
#         course_price =course.li.split()[-1]
        
#     print(f'{course_name} costs {course_price}')
    
# print("Hello World")

info = [{
    "name":"prosper",
    "age":17,
    "Career":"Software Engineer"
},
{
    "name":"david",
    "age":17,
    "Career":"Software Engineer"
}]



for i in info:
    print(i["name"], i["age"])
    # print(info[1]["name"])