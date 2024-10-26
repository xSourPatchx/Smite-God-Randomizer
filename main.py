#from bs4 import BeautifulSoup
#import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
import pandas as pd
import random


## uncomment below when ready to scrape
"""
# Getting past the "403 Forbidden" error
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

print('-' * 65)

source = requests.get('https://smite.fandom.com/wiki/List_of_gods', headers=headers)
source.raise_for_status()
soup = BeautifulSoup(source.text, 'html.parser')

scraped_list = [] 
gods_dict = {}

for item in soup.find('div', class_='mw-parser-output'):
    scraped_list.append(item.text)

# print(scraped_list)

scraped_list = scraped_list[3].split('\n')
scraped_list[:] = [x for x in scraped_list if x != ''] 

# print(scraped_list)
"""

## temp variable, can be removed when ready to scrape
scraped_list = [
    'God', 'Pantheon', 'Attack Type', 'Power Type', 'Class', 'Difficulty',
    'Favor Cost', 'Gems Cost', 'Release Date', 'Achilles', ' Greek', ' Melee',
    ' Physical', ' Warrior', 'Average', '5500 ', '200 ', '2018-02-27', 'Agni',
    ' Hindu', ' Ranged', ' Magical', ' Mage', 'Hard', '1250 ', '200 ',
    '2012-05-31', 'Ah Muzen Cab', ' Maya', ' Ranged', ' Physical', ' Hunter',
    'Average', '5500 ', '200 ', '2013-11-07', 'Ah Puch', ' Maya', ' Ranged',
    ' Magical', ' Mage', 'Average', '5500 ', '200 ', '2015-04-28', 'Amaterasu',
    ' Japanese', ' Melee', ' Physical', ' Warrior', 'Average', '5500 ', '200 ',
    '2016-01-12', 'Anhur', ' Egyptian', ' Ranged', ' Physical', ' Hunter',
    'Average', '5500 ', '200 ', '2012-08-03', 'Anubis', ' Egyptian', ' Ranged',
    ' Magical', ' Mage', 'Easy', '5500 ', '200 ', '2012-05-31', 'Ao Kuang',
    ' Chinese', ' Melee', ' Magical', ' Mage', 'Hard', '5500 ', '200 ',
    '2014-11-19', 'Aphrodite', ' Greek', ' Ranged', ' Magical', ' Mage',
    'Hard', '5500 ', '200 ', '2013-03-13', 'Apollo', ' Greek', ' Ranged',
    ' Physical', ' Hunter', 'Easy', '5500 ', '200 ', '2013-03-28', 'Arachne',
    ' Greek', ' Melee', ' Physical', ' Assassin', 'Average', '5500 ', '200 ',
    '2012-05-31', 'Ares', ' Greek', ' Melee', ' Magical', ' Guardian', 'Easy',
    '5500 ', '200 ', '2012-10-04', 'Artemis', ' Greek', ' Ranged', ' Physical',
    ' Hunter', 'Average', '575 ', '200 ', '2012-05-31', 'Artio', ' Celtic',
    ' Melee', ' Magical', ' Guardian', 'Average', '5500 ', '200 ',
    '2017-08-01', 'Athena', ' Greek', ' Melee', ' Magical', ' Guardian',
    'Easy', '5500 ', '200 ', '2013-06-05', 'Atlas', ' Greek', ' Melee',
    ' Magical', ' Guardian', 'Easy', '5500 ', '200 ', '2021-12-14', 'Awilix',
    ' Maya', ' Melee', ' Physical', ' Assassin', 'Hard', '5500 ', '200 ',
    '2014-12-17', 'Baba Yaga', ' Slavic', ' Ranged', ' Magical', ' Mage',
    'Average', '5500 ', '200 ', '2020-04-21', 'Bacchus', ' Roman', ' Melee',
    ' Magical', ' Guardian', 'Average', 'Free', 'Free', '2012-11-19',
    'Bakasura', ' Hindu', ' Melee', ' Physical', ' Assassin', 'Easy', '5500 ',
    '200 ', '2012-07-20', 'Bake Kujira', ' Japanese', ' Melee', ' Magical',
    ' Guardian', 'Average', '5500 ', '200 ', '2023-12-12', 'Baron Samedi',
    ' Voodoo', ' Ranged', ' Magical', ' Mage', 'Hard', '5500 ', '200 ',
    '2018-06-26', 'Bastet', ' Egyptian', ' Melee', ' Physical', ' Assassin',
    'Easy', '5500 ', '200 ', '2012-05-31', 'Bellona', ' Roman', ' Melee',
    ' Physical', ' Warrior', 'Average', 'Free', 'Free', '2015-02-25',
    'Cabrakan', ' Maya', ' Melee', ' Magical', ' Guardian', 'Average', '5500 ',
    '200 ', '2014-08-19', 'Camazotz', ' Maya', ' Melee', ' Physical',
    ' Assassin', 'Average', '5500 ', '200 ', '2016-10-11', 'Cerberus',
    ' Greek', ' Melee', ' Magical', ' Guardian', 'Easy', '5500 ', '200 ',
    '2018-01-09', 'Cernunnos', ' Celtic', ' Ranged', ' Physical', ' Hunter',
    'Average', '5500 ', '200 ', '2017-03-14', 'Chaac', ' Maya', ' Melee',
    ' Physical', ' Warrior', 'Average', 'Free', 'Free', '2013-12-18',
    "Chang'e", ' Chinese', ' Ranged', ' Magical', ' Mage', 'Average', '5500 ',
    '200 ', '2013-07-24', 'Charon', ' Greek', ' Ranged', ' Magical',
    ' Guardian', 'Average', '5500 ', '200 ', '2023-07-11', 'Charybdis',
    ' Greek', ' Ranged', ' Physical', ' Hunter', 'Average', '5500 ', '200 ',
    '2021-08-24', 'Chernobog', ' Slavic', ' Ranged', ' Physical', ' Hunter',
    'Hard', '5500 ', '200 ', '2018-05-15', 'Chiron', ' Greek', ' Ranged',
    ' Physical', ' Hunter', 'Easy', '5500 ', '200 ', '2015-11-17', 'Chronos',
    ' Greek', ' Ranged', ' Magical', ' Mage', 'Hard', '5500 ', '200 ',
    '2013-07-10', 'Cliodhna', ' Celtic', ' Melee', ' Physical', ' Assassin',
    'Average', '5500 ', '200 ', '2021-10-19', 'Cthulhu', ' Great Old Ones',
    ' Melee', ' Magical', ' Guardian', 'Average', '5500 ', '200 ',
    '2020-06-16', 'Cu Chulainn', ' Celtic', ' Melee', ' Physical', ' Warrior',
    'Average', '5500 ', '200 ', '2017-06-20', 'Cupid', ' Roman', ' Ranged',
    ' Physical', ' Hunter', 'Easy', '1500 ', '200 ', '2012-08-17', 'Da Ji',
    ' Chinese', ' Melee', ' Physical', ' Assassin', 'Average', '5500 ', '200 ',
    '2017-05-24', 'Danzaburou', ' Japanese', ' Ranged', ' Physical', ' Hunter',
    'Average', '5500 ', '200 ', '2020-12-15', 'Discordia', ' Roman', ' Ranged',
    ' Magical', ' Mage', 'Average', '5500 ', '200 ', '2017-11-06',
    'Erlang Shen', ' Chinese', ' Melee', ' Physical', ' Warrior', 'Average',
    '5500 ', '200 ', '2016-07-06', 'Eset', ' Egyptian', ' Ranged', ' Magical',
    ' Mage', 'Average', '5500 ', '200 ', '2013-05-15', 'Fafnir', ' Norse',
    ' Melee', ' Magical', ' Guardian', 'Average', '5500 ', '200 ',
    '2016-06-07', 'Fenrir', ' Norse', ' Melee', ' Physical', ' Assassin',
    'Average', '5500 ', '200 ', '2013-05-01', 'Freya', ' Norse', ' Melee',
    ' Magical', ' Mage', 'Average', '5500 ', '200 ', '2012-10-18', 'Ganesha',
    ' Hindu', ' Melee', ' Magical', ' Guardian', 'Average', '5500 ', '200 ',
    '2017-04-25', 'Geb', ' Egyptian', ' Melee', ' Magical', ' Guardian',
    'Average', '5500 ', '200 ', '2014-01-16', 'Gilgamesh', ' Babylonian',
    ' Melee', ' Physical', ' Warrior', 'Average', '5500 ', '200 ',
    '2021-04-20', 'Guan Yu', ' Chinese', ' Melee', ' Physical', ' Warrior',
    'Average', '5500 ', '200 ', '2012-06-29', 'Hachiman', ' Japanese',
    ' Ranged', ' Physical', ' Hunter', 'Easy', '5500 ', '200 ', '2017-09-13',
    'Hades', ' Greek', ' Ranged', ' Magical', ' Mage', 'Easy', '2000 ', '200 ',
    '2012-05-31', 'He Bo', ' Chinese', ' Ranged', ' Magical', ' Mage', 'Easy',
    '5500 ', '200 ', '2012-05-31', 'Heimdallr', ' Norse', ' Ranged',
    ' Physical', ' Hunter', 'Hard', '5500 ', '200 ', '2019-12-11', 'Hel',
    ' Norse', ' Ranged', ' Magical', ' Mage', 'Hard', '5500 ', '200 ',
    '2012-05-31', 'Hera', ' Greek', ' Ranged', ' Magical', ' Mage', 'Average',
    '5500 ', '200 ', '2018-10-15', 'Hercules', ' Roman', ' Melee', ' Physical',
    ' Warrior', 'Easy', '5500 ', '200 ', '2013-01-09', 'Horus', ' Egyptian',
    ' Melee', ' Physical', ' Warrior', 'Average', '5500 ', '200 ',
    '2019-04-30', 'Hou Yi', ' Chinese', ' Ranged', ' Physical', ' Hunter',
    'Hard', '5500 ', '200 ', '2015-01-14', 'Hun Batz', ' Maya', ' Melee',
    ' Physical', ' Assassin', 'Easy', '5500 ', '200 ', '2012-05-31', 'Ishtar',
    ' Babylonian', ' Ranged', ' Physical', ' Hunter', 'Average', '5500 ',
    '200 ', '2022-08-23', 'Ix Chel', ' Maya', ' Ranged', ' Magical', ' Mage',
    'Average', '5500 ', '200 ', '2023-04-18', 'Izanami', ' Japanese',
    ' Ranged', ' Physical', ' Hunter', 'Average', 'Free', 'Free', '2016-08-30',
    'Janus', ' Roman', ' Ranged', ' Magical', ' Mage', 'Average', '5500 ',
    '200 ', '2014-05-28', 'Jing Wei', ' Chinese', ' Ranged', ' Physical',
    ' Hunter', 'Easy', '5500 ', '200 ', '2016-04-12', 'Jormungandr', ' Norse',
    ' Ranged', ' Magical', ' Guardian', 'Average', '5500 ', '200 ',
    '2019-03-05', 'Kali', ' Hindu', ' Melee', ' Physical', ' Assassin',
    'Average', '5500 ', '200 ', '2012-05-31', 'Khepri', ' Egyptian', ' Melee',
    ' Magical', ' Guardian', 'Average', '5500 ', '200 ', '2015-08-04',
    'King Arthur', ' Arthurian', ' Melee', ' Physical', ' Warrior', 'Average',
    '5500 ', '200 ', '2019-01-07', 'Kukulkan', ' Maya', ' Ranged', ' Magical',
    ' Mage', 'Easy', 'Free', 'Free', '2012-05-31', 'Kumbhakarna', ' Hindu',
    ' Melee', ' Magical', ' Guardian', 'Easy', '5500 ', '200 ', '2014-04-16',
    'Kuzenbo', ' Japanese', ' Melee', ' Magical', ' Guardian', 'Easy', '5500 ',
    '200 ', '2017-02-14', 'Lancelot', ' Arthurian', ' Melee', ' Physical',
    ' Assassin', 'Hard', '5500 ', '200 ', '2022-06-14', 'Loki', ' Norse',
    ' Melee', ' Physical', ' Assassin', 'Easy', '5500 ', '200 ', '2012-11-02',
    'Maman Brigitte', ' Voodoo', ' Melee', ' Magical', ' Mage', 'Average',
    '5500 ', '200 ', '2023-09-26', 'Martichoras', ' Greek', ' Ranged',
    ' Physical', ' Hunter', 'Average', '5500 ', '200 ', '2023-02-21', 'Maui',
    ' Polynesian', ' Melee', ' Magical', ' Guardian', 'Average', '5500 ',
    '200 ', '2022-10-18', 'Medusa', ' Greek', ' Ranged', ' Physical',
    ' Hunter', 'Easy', '5500 ', '200 ', '2015-04-01', 'Mercury', ' Roman',
    ' Melee', ' Physical', ' Assassin', 'Average', '5500 ', '200 ',
    '2013-10-02', 'Merlin', ' Arthurian', ' Ranged', ' Magical', ' Mage',
    'Hard', '5500 ', '200 ', '2019-02-11', 'Morgan Le Fay', ' Arthurian',
    ' Ranged', ' Magical', ' Mage', 'Average', '5500 ', '200 ', '2021-06-15',
    'Mulan', ' Chinese', ' Melee', ' Physical', ' Warrior', 'Average', '5500 ',
    '200 ', '2020-02-25', 'Ne Zha', ' Chinese', ' Melee', ' Physical',
    ' Assassin', 'Average', '5500 ', '200 ', '2013-04-17', 'Neith',
    ' Egyptian', ' Ranged', ' Physical', ' Hunter', 'Easy', 'Free', 'Free',
    '2013-02-13', 'Nemesis', ' Greek', ' Melee', ' Physical', ' Assassin',
    'Average', 'Free', 'Free', '2014-02-06', 'Nike', ' Greek', ' Melee',
    ' Physical', ' Warrior', 'Easy', '5500 ', '200 ', '2016-12-06', 'Nox',
    ' Roman', ' Ranged', ' Magical', ' Mage', 'Average', '5500 ', '200 ',
    '2014-10-29', 'Nu Wa', ' Chinese', ' Ranged', ' Magical', ' Mage', 'Easy',
    '5500 ', '200 ', '2013-12-05', 'Nut', ' Egyptian', ' Ranged', ' Physical',
    ' Hunter', 'Average', '5500 ', '200 ', '2024-02-20', 'Odin', ' Norse',
    ' Melee', ' Physical', ' Warrior', 'Easy', '5500 ', '200 ', '2012-05-31',
    'Olorun', ' Yoruba', ' Ranged', ' Magical', ' Mage', 'Average', 'Free',
    'Free', '2019-06-25', 'Osiris', ' Egyptian', ' Melee', ' Physical',
    ' Warrior', 'Hard', '5500 ', '200 ', '2014-05-06', 'Pele', ' Polynesian',
    ' Melee', ' Physical', ' Assassin', 'Average', '5500 ', '200 ',
    '2018-08-06', 'Persephone', ' Greek', ' Ranged', ' Magical', ' Mage',
    'Hard', '5500 ', '200 ', '2019-08-20', 'Poseidon', ' Greek', ' Ranged',
    ' Magical', ' Mage', 'Easy', 'Free', 'Free', '2013-02-28', 'Ra',
    ' Egyptian', ' Ranged', ' Magical', ' Mage', 'Average', '5500 ', '200 ',
    '2012-05-31', 'Raijin', ' Japanese', ' Ranged', ' Magical', ' Mage',
    'Average', '5500 ', '200 ', '2016-02-16', 'Rama', ' Hindu', ' Ranged',
    ' Physical', ' Hunter', 'Average', '5500 ', '200 ', '2014-06-24',
    'Ratatoskr', ' Norse', ' Melee', ' Physical', ' Assassin', 'Easy', '5500 ',
    '200 ', '2015-06-02', 'Ravana', ' Hindu', ' Melee', ' Physical',
    ' Assassin', 'Average', '5500 ', '200 ', '2015-06-30', 'Scylla', ' Greek',
    ' Ranged', ' Magical', ' Mage', 'Easy', '5500 ', '200 ', '2014-03-05',
    'Serqet', ' Egyptian', ' Melee', ' Physical', ' Assassin', 'Average',
    '5500 ', '200 ', '2014-07-15', 'Set', ' Egyptian', ' Melee', ' Physical',
    ' Assassin', 'Average', '5500 ', '200 ', '2019-04-30', 'Shiva', ' Hindu',
    ' Melee', ' Physical', ' Warrior', 'Average', '5500 ', '200 ',
    '2022-02-22', 'Skadi', ' Norse', ' Ranged', ' Physical', ' Hunter', 'Hard',
    '5500 ', '200 ', '2016-03-15', 'Sobek', ' Egyptian', ' Melee', ' Magical',
    ' Guardian', 'Easy', '5500 ', '200 ', '2012-05-31', 'Sol', ' Norse',
    ' Ranged', ' Magical', ' Mage', 'Hard', '5500 ', '200 ', '2015-10-06',
    'Sun Wukong', ' Chinese', ' Melee', ' Physical', ' Warrior', 'Average',
    '5500 ', '200 ', '2013-10-23', 'Surtr', ' Norse', ' Melee', ' Physical',
    ' Warrior', 'Average', '5500 ', '200 ', '2023-01-24', 'Susano',
    ' Japanese', ' Melee', ' Physical', ' Assassin', 'Hard', '5500 ', '200 ',
    '2016-05-10', 'Sylvanus', ' Roman', ' Ranged', ' Magical', ' Guardian',
    'Average', '5500 ', '200 ', '2014-10-01', 'Terra', ' Roman', ' Melee',
    ' Magical', ' Guardian', 'Hard', '5500 ', '200 ', '2016-08-02', 'Thanatos',
    ' Greek', ' Melee', ' Physical', ' Assassin', 'Average', 'Free', 'Free',
    '2013-09-18', 'The Morrigan', ' Celtic', ' Ranged', ' Magical', ' Mage',
    'Very Hard', '5500 ', '200 ', '2017-01-10', 'Thor', ' Norse', ' Melee',
    ' Physical', ' Assassin', 'Hard', '5500 ', '200 ', '2012-09-06', 'Thoth',
    ' Egyptian', ' Ranged', ' Magical', ' Mage', 'Average', '5500 ', '200 ',
    '2016-11-08', 'Tiamat', ' Babylonian', ' Ranged', ' Magical', ' Mage',
    'Hard', '5500 ', '200 ', '2021-02-23', 'Tsukuyomi', ' Japanese', ' Melee',
    ' Physical', ' Assassin', 'Average', '5500 ', '200 ', '2020-08-11', 'Tyr',
    ' Norse', ' Melee', ' Physical', ' Warrior', 'Hard', '5500 ', '200 ',
    '2013-08-07', 'Ullr', ' Norse', ' Ranged', ' Physical', ' Hunter', 'Hard',
    '5500 ', '200 ', '2014-03-19', 'Vamana', ' Hindu', ' Melee', ' Physical',
    ' Warrior', 'Average', '5500 ', '200 ', '2012-05-31', 'Vulcan', ' Roman',
    ' Ranged', ' Magical', ' Mage', 'Average', '5500 ', '200 ', '2013-01-30',
    'Xbalanque', ' Maya', ' Ranged', ' Physical', ' Hunter', 'Average',
    '5500 ', '200 ', '2012-12-21', 'Xing Tian', ' Chinese', ' Melee',
    ' Magical', ' Guardian', 'Average', '5500 ', '200 ', '2015-09-01',
    'Yemoja', ' Yoruba', ' Ranged', ' Magical', ' Guardian', 'Average', 'Free',
    'Free', '2019-10-15', 'Ymir', ' Norse', ' Melee', ' Magical', ' Guardian',
    'Easy', 'Free', 'Free', '2012-05-31', 'Yu Huang', ' Chinese', ' Ranged',
    ' Magical', ' Mage', 'Average', '5500 ', '200 ', '2022-04-19', 'Zeus',
    ' Greek', ' Ranged', ' Magical', ' Mage', 'Average', '5500 ', '200 ',
    '2012-05-31', 'Zhong Kui', ' Chinese', ' Ranged', ' Magical', ' Mage',
    'Easy', '5500 ', '200 ', '2013-08-28'
]

scraped_list = [item.strip(' ') for item in scraped_list]

# print(scraped_list)

keys = []
values = []

for key, item in enumerate(scraped_list):
    if key == 0 or key % 9 == 0:
        keys.append(item)
# print(keys)

for item in scraped_list:
    if item not in keys:
        values.append(item)
# print(values)

values = [values[i:i + 8] for i in range(0, len(values), 8)]
gods_dict = dict(zip(keys, values))

## removing white spaces
old_list = gods_dict['God']
new_list = [i.replace(' ', '') for i in old_list]
gods_dict['God'] = new_list

## Pandas DataFrame
df = pd.DataFrame(gods_dict).T
df.columns = df.iloc[0]
df.drop(df.index[0], inplace=True)


## Defining The Form Framework
class GodFilterForm(FlaskForm):
    # Pantheon SelectField
    filterPantheonChoice = []
    filterPantheonChoice.insert(0, ('Any' + df.columns[0] + 'Filter', 'Any'))
    for index, item in enumerate(sorted(df['Pantheon'].unique())):
        filterPantheonChoice.insert(index + 1, (item + 'Filter', item))
    pantheon = SelectField('Pantheon', choices=filterPantheonChoice)
    # print(pantheon)

    # Attack Type SelectField
    filterAttackTypeChoice = []
    filterAttackTypeChoice.insert(0, ('Any' + df.columns[1] + 'Filter', 'Any'))
    for index, item in enumerate(sorted(df['AttackType'].unique())):
        filterAttackTypeChoice.insert(index + 1, (item + 'Filter', item))
    attackType = SelectField('Attack Type', choices=filterAttackTypeChoice)

    # Power Type SelectField
    filterPowerTypeChoice = []
    filterPowerTypeChoice.insert(0, ('Any' + df.columns[2] + 'Filter', 'Any'))
    for index, item in enumerate(sorted(df['PowerType'].unique())):
        filterPowerTypeChoice.insert(index + 1, (item + 'Filter', item))
    powerType = SelectField('Power Type', choices=filterPowerTypeChoice)

    # Class Type SelectField
    filterClassChoice = []
    filterClassChoice.insert(0, ('Any' + df.columns[3] + 'Filter', 'Any'))
    for index, item in enumerate(sorted(df['Class'].unique())):
        filterClassChoice.insert(index + 1, (item + 'Filter', item))
    classType = SelectField('Class', choices=filterClassChoice)

    # Difficulty SelectField
    filterDifficultyChoice = []
    filterDifficultyChoice.insert(0, ('Any' + df.columns[4] + 'Filter', 'Any'))
    for index, item in enumerate(sorted(df['Difficulty'].unique())):
        filterDifficultyChoice.insert(index + 1, (item + 'Filter', item))
    difficulty = SelectField('Difficulty', choices=filterDifficultyChoice)

    # SubmitField Button
    submit = SubmitField("Submit")


## Flask Front end
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_secret'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = GodFilterForm()
    if request.method == 'POST':
        result = request.form
        # print(request.form['pantheon'])

        pantheon = request.form[
            'pantheon']  # e.g. -> request.form['pantheon'] = 'anyPantheonFilter'
        print(pantheon)
        attackType = request.form['attackType']
        print(attackType)
        powerType = request.form['powerType']
        print(powerType)
        classType = request.form['classType']
        print(classType)
        difficulty = request.form['difficulty']
        print(difficulty)

        all_filtered_values = [pantheon] + [attackType] + [powerType] + [
            classType
        ] + [difficulty]
        # print(all_filtered_values)

        cleaned_all_filtered_values = []
        for item in all_filtered_values:
            if 'Any' in item:
                cleaned_all_filtered_values.append(item[0:3])
                continue
            cleaned_all_filtered_values.append(item[0:item.index('Filter')])
        # print(cleaned_all_filtered_values)

        filtered_indexing = []
        for index, item in enumerate(cleaned_all_filtered_values):
            if item != 'Any':
                filtered_indexing.append(index)

        filtered_values = []
        for index, item in enumerate(cleaned_all_filtered_values):
            if index in filtered_indexing:
                filtered_values.append(item)
        # print(filtered_values)

        filtered_keys = []
        for index, item in enumerate(gods_dict['God']):
            if index in filtered_indexing:
                filtered_keys.append(item)
        # print(filtered_keys)

        ## check for no filter applied
        if filtered_keys == []:
            print('yes')
            filtered_df = df
        else:
            ## 'PowerType == ["Physical"] & Difficulty == ["Average"]'
            query = ' & '.join(f'{i} == {repr(k)}'
                               for i, k in zip(filtered_keys, filtered_values))
            print(query)
            filtered_df = df.query(query)

        if filtered_df.empty == True:
            random_choice = "Invalid Filter, Please Try Again"
        else:
            random_choice = random.choice(filtered_df.index)
        # print(random.choice(filtered_df.index))

        return render_template('random.html',
                               result=result,
                               random_choice=random_choice)
    else:
        return render_template('form_filter.html', form=form)


#print(request.form['pantheon'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
