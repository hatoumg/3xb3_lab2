import matplotlib.pyplot as plot
from exp1 import probability
from graph import is_connected

def main():
    v, p = [], []
    t = probability(n=100, min=100, inc=5, e=500, r=1000, f=is_connected)
    for key in t:
        v.append(key)
        p.append(t[key])
    plot.plot(v, p)
    plot.xlabel("Number of Edges")
    plot.ylabel("Connected Probability")
    plot.show()

if __name__ == "__main__":
    main()