from itertools import count

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity 
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

text_adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n"," ")
print("The result of changes 1:", text_adwentures_of_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""
new_adwentures_of_tom_sawer = text_adwentures_of_tom_sawer.replace(" ...."," ")
print("The result of changes 2:", new_adwentures_of_tom_sawer)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
second_adwentures_of_tom_sawer = adwentures_of_tom_sawer.split(' ', 1)
print("The result of changes 3:", second_adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("The letter h occurs in the text:", adwentures_of_tom_sawer.count("h"), "times")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
list_of_words = adwentures_of_tom_sawer.split()
capitalized_word_count = 0
for word in list_of_words:
    if word[0].isupper():
        capitalized_word_count += 1
print(f'The count of words that starts with a capital letter: {capitalized_word_count}')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_position = adwentures_of_tom_sawer.find("Tom")
second_position = adwentures_of_tom_sawer.find("Tom", first_position+1 )
print(f"Find 'Tom' on position: {second_position}")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
#adwentures_of_tom_sawer_sentences = new_adwentures_of_tom_sawer.split('. ')
#print(adwentures_of_tom_sawer_sentences)

pre_adwentures_of_tom_sawer_sentences = new_adwentures_of_tom_sawer.replace("\n"," ")
adwentures_of_tom_sawer_sentences = pre_adwentures_of_tom_sawer_sentences.split('. ')
for sentence in adwentures_of_tom_sawer_sentences:
    print("Sentence:",sentence)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
fourth_sentence_lower = fourth_sentence.lower()
print("Fourth sentence in lower registr:", fourth_sentence_lower)


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith(' By the time '):
        print(f'Sentence starts with "By the time": "{sentence}"')
        break
else:
    print('No sentence begins with "By the time".')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print(f'Кількість слів в сотанньому реченні:{word_count}')