"""
Case-study №1
Developers: Kuznetsov N. 65%
            $hishko S. 70%
"""

from textblob import *
from deep_translator import GoogleTranslator

s = input()
s_en = GoogleTranslator(source='auto', target='en', ).translate(s)


text = TextBlob(s_en)
result = str(text.sentiment).replace('Sentiment(polarity=', '')
result = result.replace(', subjectivity=', ' ')
result = result.replace(')', '')
pol, sub = map(float, result.split())
if pol >0.33: polarity = 'позитивный'
elif -0.33<= pol <= 0.33: polarity  = 'нейтральный'
else: polarity = 'негативный'
subjectivity = str(round((1-sub)*100, 1))+'%'


x=s
t='.'
v='?'
d='!'
s=x.count(t)
m=x.count(v)
l=x.count(d)
print('Количество предложений', s+m+l)
words=x.split()
print('Количество слов', len(words))
k=['у', 'е', 'а', 'о', 'э', 'я', 'и', 'ю', 'ы', 'ё', 'a', 'e', 'i', 'o', 'u', 'y', 'У', 'Е', 'А', 'О', 'Э', 'Я', 'И', 'Ю', 'Ё', 'A', 'E', 'I', 'O', 'U', 'Y']
n=0
sogl=0
for i in range (0, len(k)):
    n=x.count(k[i])
    sogl=sogl+n
    n=0
print('Количество слогов', sogl)
print('Средняя длина предложения в словах', len(words)/(s+m+l))
print('Средняя длина слова в слогах', sogl/(len(words)))
angl='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
r=list(angl)
x1=list(x)
english=0
for q in range (0, len(x1)):
    for z in range (0, len(r)):
        if x1[q]==r[z]:
            english=1
            break
    break
if english==1:
    flesh = 206.835 - 1.015 * (len(words) / (s + m + l)) - 84.6 * (sogl / len(words))
else:
    flesh = 206.835 - 1.3 * (len(words) / (s + m + l)) - 60.1 * (sogl / len(words))

print('Индекс удобочитаемости Флеша', flesh)
if flesh>80:
    print('Текст очень легко читается (для младших школьников).')
if flesh>50 and flesh<=80:
    print('Простой текст (для школьников).')
if flesh>25 and flesh<=50:
    print('Текст немного трудно читать (для студентов).')
if flesh<=25:
    print('Текст трудно читается (для выпускников ВУЗов).')

print('Тональность текста:', polarity, '\n', 'Объективность:', subjectivity)
