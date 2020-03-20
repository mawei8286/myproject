import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(figsize=(15, 8), dpi=80)
l1, = plt.plot(x, y1, label='up')
l2, = plt.plot(x, y2, color='red', linewidth=5, linestyle='--', label='down')
plt.legend(handles=[l1, l2, ], labels=['aaa', 'bbb'], loc='best')

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('i am x')
plt.ylabel('i am y')

new_ticks = np.linspace(-1, 2, 5)

plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$',
                                     r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

plt.show()
