#main.py
#部分料金計算
import csv


count = 0 #件数
sum_Price = 0 #価格の合計
address_input = input("検索する都市を入力してください : ")

# adressが東京都の場合
if address_input.find('東京') != -1:
    price = 95
# adressが千葉の場合
elif address_input.find('千葉') != -1:
    price = 105
# adressが埼玉の場合
elif address_input.find('埼玉') != -1:
    price = 105
# adressが神奈川の場合
elif address_input.find('神奈川') != -1:
    price = 105
# その他の場合
else:
    if address_input.__eq__("京都"): #京都と検索すると東京も一緒に検索されて結果が出る間違い修正
        address_input += '府'
    price = 115
# csv File encoding utf-8
# shitf-jis
with open('SampleData.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # アドレスを変数に保存
        address = row['住所']
        if address.find(address_input) != -1:
            print('会社名:' + row['会社名'])
            print('住所:' + row['住所'])
            print('料金:' + str(price) + '円')
            count += 1
            sum_Price += price
        else :
            continue
        print()

print(address_input+"件: "+str(count)+"件,\t総価格:"+str(sum_Price)+"円")



# 全体料金計算

# import csv
# price = [0,95,105,115] #件別料金
# count1 = 0; sum_Price1 = 0 #東京都
# count2 = [0,0,0]; sum_Price2 = [0,0,0] #千葉県,埼玉県,神奈川県
# count3 = 0; sum_Price3 = 0 #その他
#
# # csv File encoding utf-8
# # shitf-jis
# with open('SampleData.csv', encoding='utf-8', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         # アドレスを変数に保存
#         address = row['住所']
#
#         # adressが東京都の場合
#         if address.find('東京都') != -1:
#             print('会社名:' + row['会社名'])
#             print('住所:' + row['住所'])
#             print('料金:' + str(price[1]) + '円')
#             count1 += 1
#             sum_Price1 += price[1]
#
#         # adressが千葉の場合
#         elif address.find('千葉県') != -1:
#             print('会社名:' + row['会社名'])
#             print('住所:' + row['住所'])
#             print('料金:' + str(price[2]) + '円')
#             count2[0] += 1
#             sum_Price2[0] += price[2]
#
#         # adressが埼玉の場合
#         elif address.find('埼玉県') != -1:
#             print('会社名:' + row['会社名'])
#             print('住所:' + row['住所'])
#             print('料金:' + str(price[2]) + '円')
#             count2[1] += 1
#             sum_Price2[1] += price[2]
#         # adressが神奈川の場合
#         elif address.find('神奈川県') != -1:
#             print('会社名:' + row['会社名'])
#             print('住所:' + row['住所'])
#             print('料金:' + str(price[2]) + '円')
#             count2[2] += 1
#             sum_Price2[2] += price[2]
#         # その他の場合
#         else:
#             print('会社名:' + row['会社名'])
#             print('住所:' + row['住所'])
#             print('料金:' + str(price[3]) + '円')
#             count3 += 1
#             sum_Price3 += price[3]
#         print()
#
#
# print("東京都件 :"+str(count1)+"件\t総価格:"+str(sum_Price1)+"円")
# print("千葉県件 :"+str(count2[0])+"件\t総価格:"+str(sum_Price2[0])+"円")
# print("埼玉県件 :"+str(count2[1])+"件\t総価格:"+str(sum_Price2[1])+"円")
# print("神奈川県件 :"+str(count2[2])+"件\t総価格:"+str(sum_Price2[2])+"円")
# print("その他件 :"+str(count3)+"件\t総価格:"+str(sum_Price3)+"円")