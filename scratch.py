f = open('test1.csv', 'w')
a = input()
lines = []
x = 1
while a:
    a = float(a.replace(',', '.'))
    line = f'{x};{a}\n'
    lines.append(line)
    a = input()
    x += 1

f.writelines(lines)
f.close()
