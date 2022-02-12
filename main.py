import requests
from time import sleep
import os
import zipfile
from keyword import iskeyword

# cookies = {"stms":"046A99F6B63EF0F482C3C37DCDBDAD3E985F6ECA09EF6940909B3897BB8DD532",
#            "stps":"eyJVc2VyTmFtZSI6IlNUZHcyMFBLSC9HU0hMNW45NXY5WG8zVm1vY1FXSnVvNXUwR0xuRG5nNzA9IiwiVXNlcklkIjoieVZ1ZGl"
#                    "VbkhyOTAzR24zLzVQV0NSZVdlWWt3UW5LcFYiLCJTdG9yZWRJZGVudGl0aWVzIjp7IjkwNTcxNGQ3LWQxMmEtNGUyOC04ODBmL"
#                    "TlmZTlhMGNhYjMyZiI6Im15MHREZ1A0aVpqT1UvTjZBaE5vc2c9PSIsIjk0Yzc0MjUxLWI2YTItNDQ0NC04OWMxLTgzNjEyMTd"
#                    "jYTY5MyI6Im15MHREZ1A0aVpqeWYyOVROVGFMWUE9PSJ9LCJBdHRyaWJ1dGVzIjp7IklzQWRtaW4iOiJpMFJsbGIrTkU0QT0iL"
#                    "CJJc1N1cHBvcnQiOiJpMFJsbGIrTkU0QT0ifX0%3D",
#            "stul":"281475010023963:00000000-0000-0000-0000-000000000000=21.02.2022 12:09:36"}
#
# header = {"X-ProductKey":"67B9EB2E-CC49-44D6-98F6-44942B99AB55"}
# #
# spisok = []
# #
#
# authorization_json = {"UserName":"EKF_exportdata@mtproject.ru","Password":"E7g177ITNo64tXQT"}
# path_to_authorization = "https://portal.systtech.ru/EKF-UAT/api/auth/credentials?Content-type=application/json"
#
# global autorization
# autorization = requests.post(path_to_authorization, json=authorization_json)
# for cookie in autorization.cookies.items():
#     if cookie not in spisok:
#         spisok.append(cookie)
# cookies = dict(spisok)
# print(autorization)
# print(cookies)
# assert autorization.status_code == 200
#
#
#
# params = {"SpecificationId":5, "Args":"{args_default:true }"}
# path_execute_query = "https://portal.systtech.ru/EKF-UAT/api/parameterizedquery/executequery"
# execute_query = requests.post(path_execute_query,
#                           cookies=cookies,
#                           headers=header,
#                           json=params)
# global notification_id
# notification_id = execute_query.json()
# print(notification_id)
# assert execute_query.status_code == 200
#
# timeout = '60'
# def implicit_wait_elements(timeout):
#     answer = 'Not ready yet'
#     current_waiting_time = 0
#     while current_waiting_time <= int(timeout):
#         try:
#             get_result = requests.post("https://portal.systtech.ru/EKF-UAT/api/parameterizedquery/getresult",
#                                        cookies=cookies,
#                                        headers=header,
#                                        json=notification_id)
#             assert get_result.status_code == 200
#             d1 = dict(get_result.json())
#             global link_to_download
#             link_to_download = d1['result']
#             assert answer != link_to_download
#             break
#         except:
#             sleep(1)
#             current_waiting_time += 1
#     else:
#         raise TimeoutError(f'Сообщение еще в очереди, попробуйте повторить запрос позднее')
#
#     print(link_to_download)
#     print(answer)
#
# implicit_wait_elements(timeout)
#
#
# global get_file
# get_file = requests.get(link_to_download,
#                           cookies=cookies,
#                           headers=header)
#
#
# print(get_file)
# print(link_to_download)
#
#
# with open("C:\\test\\test1.zip", "wb") as f:
#     f.write(get_file.content)
#     f.close()
#
#
# archive_wirh_csv = zipfile.ZipFile('C:\\test\\test1.zip', 'r')
# archive_wirh_csv.printdir()
# content_archive_wirh_csv = archive_wirh_csv.namelist()
# for name in content_archive_wirh_csv:
#     if '.csv' in name:
#         True
#     if '.csv' not in name:
#         raise NameError('в архиве нет файла с расширением csv')
# archive_wirh_csv.close()
#
# def deleted():
#     path_to_archive = os.path.join(os.path.abspath(os.path.dirname('C:\\test\\')), 'test1.zip')
#     os.remove(path_to_archive)
#
# deleted()

s = 'ф'
print(s.isnumeric())


