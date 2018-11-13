import matplotlib.pyplot as plt


def demo1():
    x = range(4)
    y = (20, 25, 40, 30)
    avg = sum(y) / 4
    print(avg)
    xtick = ("mocha", "latte", "espresso", "tea")
    plt.bar(x, y, color="green")
    plt.xticks(x, xtick)
    plt.axhline(avg, color="red", linestyle="--")
    plt.title("Orders by menu\nFeb 2017", color="orange", fontsize=17)
    plt.ylabel("# orders")
    plt.show()


if __name__ == '__main__':
    demo1()