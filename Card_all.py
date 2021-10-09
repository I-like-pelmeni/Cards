from cards2 import Card

with open('class1.py') as f1, open('class2.py') as f2, open('class3.py') as f3, open('class4.py') as f4, open('class5.py') as f5 out:
    for f1line, f2line, f3line, f4line, f5line in Card(f1, f2, f3, f4, f5):
        out.write('{},{}'.format(f1line.strip(), f2line, f3line, f4line, f5line))


