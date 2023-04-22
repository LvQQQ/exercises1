import csv
import os

from termcolor import colored


surrounding = "==============================================="

while True:
    # first_Question
    name = input(colored(f"{surrounding}\nこんにちは!私の名前はROBOです。あなたの名前は？\n{surrounding}\n", "light_green"))
    name = name.title()

    if bool(name.strip()):
    
        if not os.path.exists('restaurant_count.csv'):
            # Second_Question
            favorite_restaurant = input(colored(f"{surrounding}\n{name}さん、どこのレストランが好きですか？\n{surrounding}\n", "light_green"))
            if bool(favorite_restaurant.strip()):
                favorite_restaurant = favorite_restaurant.title()

        # ファイル有無確認
        if os.path.exists('restaurant_count.csv'):

            with open('restaurant_count.csv', 'r') as r_csvfile:
                reader = csv.DictReader(r_csvfile)
                data = list(reader)
     
                row_count = 0
                for now_row in data:
                    row_count += 1

                # おすすめレストラン
                max_num = 0
                for count_row in data:
                    num = count_row["count"]
                    num = int(num)
                    if num > max_num:
                        max_num = num
                        top_count_row = count_row

                recommend_restaurant = top_count_row["restaurant_name"]

                no = 0
                while True:
                    # Question(Y/N)
                    print(colored(f"{surrounding}\n私のおすすめのレストランは、{recommend_restaurant}です。", "light_green"))
                    restaurant_answer = input(colored(f"このレストランは好きですか？[Yes/No]\n{surrounding}\n", "light_green")).upper()
                    if bool(restaurant_answer.strip()):
                        if no == 1 or row_count == 1:
                            break
                        elif restaurant_answer == "NO" or "N":
                            no = 1
                            row_count -= 1
                            max_num = 0
                            top_count_num = top_count_row["count"]
                            top_count_num = int(top_count_num)
                            # second_row_count = 0
                            for count_row in data:
                                # second_row_count += 1
                                num = count_row["count"]
                                num = int(num)
                                if top_count_num > num > max_num:
                                    max_num = num
                                    second_count_row = count_row
                                    recommend_restaurant = second_count_row["restaurant_name"]

                                elif not top_count_row == count_row:
                                    recommend_restaurant = count_row["restaurant_name"]
                                # else:
                                #     recommend_restaurant = count_row["restaurant_name"]
                                # elif second_row_count >= 2:
                                #     recommend_restaurant = count_row["restaurant_name"]

                        elif restaurant_answer == "YES" or "Y":
                            break


                # Second_Question
                if bool(name.strip()):
                    favorite_restaurant = input(colored(f"{surrounding}\n{name}さん、どこのレストランが好きですか？\n{surrounding}\n", "light_green"))
                    if bool(favorite_restaurant.strip()):
                        favorite_restaurant = favorite_restaurant.title()

                a = False
                for row in data:
                    # count編集
                    if row["restaurant_name"] == favorite_restaurant:
                        count_value = row["count"]
                        count_value = int(count_value)
                        count_value += 1
                        row["count"] =count_value
                        a = True

                # CSVfile編集
                with open('restaurant_count.csv', 'w', newline='') as re_csvfile:
                    fieldnames = ['restaurant_name', 'count']
                    writer = csv.DictWriter(re_csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data)  

                # "restaurant_name追加"
                if a == False:
                    with open('restaurant_count.csv', 'a', newline='') as a_csvfile:
                        writer = csv.writer(a_csvfile)
                        row = [favorite_restaurant, 1]
                        writer.writerow(row)

        # ファイル新規追加
        else:
            with open('restaurant_count.csv', 'w', newline="") as w_csvfile:
                fieldnames = ["restaurant_name", "count"]
                writer = csv.DictWriter(w_csvfile, fieldnames= fieldnames)
                writer.writeheader()
                writer.writerow({"restaurant_name": favorite_restaurant, "count": 1})

        # end
        if bool(favorite_restaurant):
            print(colored(f"{surrounding}\n{favorite_restaurant}ですね!\n{name}さん、ありがとうございました。\n良い一日を!さようなら。\n{surrounding}", "light_green"))
            break
 