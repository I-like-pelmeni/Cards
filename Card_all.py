from cards2 import Card

with open('class1.py') as f1, open('class2.py') as f2, open('class3.py') as f3, open('class4.py') as f4, open('class5.py') as f5, open('Card_all.py')as out:
    for f1line, f2line, f3line, f4line, f5line in Card(f1, f2, f3, f4, f5):
        out.write('{},{}'.format(f1line.strip(), f2line, f3line, f4line, f5line))

card1 = Card("T", Card.SUITS[0])
card2 = Unprintable_Card("T", Card.SUITS[1])
card3 = Positionable_Card("T", Card.SUITS[2])
print("Печатаю объект Card:")
print(card1)
print("\nПечатаю объект Unprintable_card:")
print(card2)
print("\nПечатаю объект Positionable_Card:")
print(card3)
print("Переворачиваю объект Positionable_Card.")
card3.flip()
print("Печатаю объект Posionable_Card:")
print(card3)


