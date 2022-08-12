#main.py
import csv


count1 = 0; price1 = 0 #東京都
count2 = [0,0,0]; price2 = [0,0,0] #千葉県,埼玉県,神奈川県
count3 = 0; price3 = 0 #その他

# csv File encoding utf-8
# shitf-jis
with open('SampleData.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # アドレスを変数に保存
        address = row['住所']

        # adressが東京都の場合
        if address.find('東京都') != -1:
            print('会社名:' + row['会社名'])
            print('住所:' + row['住所'])
            print('料金:' + str(95) + '円')
            count1 += 1
            price1 += 95

        # adressが千葉の場合
        elif address.find('千葉県') != -1:
            print('会社名:' + row['会社名'])
            print('住所:' + row['住所'])
            print('料金:' + str(95) + '円')

            count2[0] += 1
            price2[0] += 105

        # adressが埼玉の場合
        elif address.find('埼玉県') != -1:
            print('会社名:' + row['会社名'])
            print('住所:' + row['住所'])
            print('料金:' + str(95) + '円')
            count2[1] += 1
            price2[1] += 105
        # adressが神奈川の場合
        elif address.find('神奈川県') != -1:
            print('会社名:' + row['会社名'])
            print('住所:' + row['住所'])
            print('料金:' + str(95) + '円')
            count2[2] += 1
            price2[2] += 105
        # その他の場合
        else:
            print('会社名:' + row['会社名'])
            print('住所:' + row['住所'])
            print('料金:' + str(95) + '円')
            count3 += 1
            price3 += 115
        print()

print()
print("東京都件 :"+str(count1)+"件\t総価格:"+str(price1)+"円")
print("千葉県件 :"+str(count2[0])+"件\t総価格:"+str(price2[0])+"円")
print("埼玉県件 :"+str(count2[1])+"件\t総価格:"+str(price2[1])+"円")
print("神奈川県件 :"+str(count2[2])+"件\t総価格:"+str(price2[2])+"円")
print("その他件 :"+str(count3)+"件\t総価格:"+str(price3)+"円")
