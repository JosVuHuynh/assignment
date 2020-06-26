from models.eigenInstruction import *

arr = [
    {'User_ID': 1, 'Page_Path': 'link_1', 'Referral_Path': 'link_2', 'Time': '2020-06-24 20:58:18'},
    {'User_ID': 1, 'Page_Path': 'link_1', 'Referral_Path': 'link_4', 'Time': '2020-06-24 20:58:18'},
    {'User_ID': 1, 'Page_Path': 'link_1', 'Referral_Path': 'link_5', 'Time': '2020-06-24 20:58:18'},
    {'User_ID': 1, 'Page_Path': 'link_1', 'Referral_Path': 'link_6', 'Time': '2020-06-24 20:58:18'},
    {'User_ID': 1, 'Page_Path': 'link_2', 'Referral_Path': 'link_3', 'Time': '2020-06-24 20:58:18'},
    {'User_ID': 1, 'Page_Path': 'link_2', 'Referral_Path': 'link_4', 'Time': '2020-06-24 20:58:18'},
    {'User_ID': 1, 'Page_Path': 'link_3', 'Referral_Path': 'link_5', 'Time': '2020-06-24 20:58:18'},
    {'User_ID': 1, 'Page_Path': 'link_4', 'Referral_Path': 'link_5', 'Time': '2020-06-24 20:58:18'},
    {'User_ID': 1, 'Page_Path': 'link_5', 'Referral_Path': 'link_1', 'Time': '2020-06-24 20:58:18'},
    {'User_ID': 1, 'Page_Path': 'link_5', 'Referral_Path': 'link_4', 'Time': '2020-06-24 20:58:18'},
    {'User_ID': 1, 'Page_Path': 'link_6', 'Referral_Path': 'link_5', 'Time': '2020-06-24 20:58:18'}

]

def main():
    eigen = EigenInstruction()
    request = Request(1, '2020-06-24 20:58:18', '2020-06-24 20:58:18')
    w, v = eigen.get_eigen(request)
    print(v)


if __name__ == '__main__':
    main()
