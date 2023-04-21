import csv
import os

from termcolor import colored


surrounding = "==============================================="

while True:
    # first_Question
    name = input(colored(f"{surrounding}\nこんにちは!私の名前はROBOです。あなたの名前は？\n{surrounding}\n", "light_green"))
    name = name.title()
    
    # Second_Question
    def get_favorite_restaurant():
        while bool(name.strip()):
            favorite_restaurant = input(colored(f"{surrounding}\n{name}さん、どこのレストランが好きですか？\n{surrounding}\n", "light_green"))
            favorite_restaurant = favorite_restaurant.title()
            if bool(favorite_restaurant.strip()):    
                return favorite_restaurant
    favorite_restaurant = get_favorite_restaurant()

    # ファイル有無確認
    if os.path.exists('restaurant_count.csv'):
        
        recommend_restaurant = ""
        # Question(Y/N)
        print(colored(f"{surrounding}\n私のおすすめのレストランは、{recommend_restaurant}です。", "light_green"))
        restaurant_answer = input(colored(f"このレストランは好きですか？[Yes/No]\n{surrounding}\n", "light_green"))

        with open('restaurant_count.csv', 'r') as r_csvfile:
            reader = csv.DictReader(r_csvfile)
            data = list(reader)
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
 