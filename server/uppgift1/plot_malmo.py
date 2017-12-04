#!/usr/bin/env python3
"""
Compute stuff
"""
# pylint: disable=C0103
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from uppgift1.smhi_temp_series import fetch_temp_data, temp_series

MALMOLATEST = ("https://opendata-download-metobs.smhi.se/api/version/" +
               "latest/parameter/1/station/52350/period/latest-day/data.json")
NaN = float('nan')


def epoch_to_date(ms):
    """
    Epoch in milliseconds to python datetime localized.

    Assumes epoc in utc-timezone.
    """
    return datetime.utcfromtimestamp(ms // 1000)


def derive_forward(ys, a):
    """
    derive forward
    """
    return ys[a + 1] - ys[a]  # / (x - x + 1)


def derive_backwards(ys, a):
    """
    derive backward
    """
    return ys[a] - ys[a - 1]  # / (x - x + 1)


def derive_center(ys, a):
    """
    central derivation
    """
    return (ys[a + 1] - ys[a - 1]) / 2


def derive_series(xs, ys, derive_func):
    """
    Derivate a series
    """
    return [derive_func(ys, x) for x in xs]


def avarage(ns):
    """
    avarage for a numbers array
    """
    return sum(ns) / len(ns)


def simple_moving_avarage(ys, ws):
    """
    Moving avarage
    ws: window size
    """
    front = (ws // 2) if ws % 2 != 0 else (ws // 2) - 1
    back = ws // 2
    ma = [
        avarage(ys[x - back:x + front + 1])
        for x in range(back,
                       len(ys) - front)
    ]
    # ma = []
    # for x in range(back, len(ys) - front):
    #     ma += [avarage(ys[x - back:x + front + 1])]
    return ([None for _ in range(back)] + ma + [None for _ in range(front)])


def main():
    """
    Run stuff
    """
    temp_data = fetch_temp_data((MALMOLATEST))
    ts = temp_series(temp_data)
    ys = ts["temp"]
    xs = range(len(ts["temp"]))

    plt.plot(xs, ys, "ro-", label="Temperatur")
    plt.xlabel("Timme")
    plt.ylabel("Temperatur")

    # Forward derivation
    fyp = derive_series(xs[0:-1], ys, derive_forward) + [NaN]
    plt.plot(xs, fyp, "o-", color="green", label="Differanskvot framåt")

    # Backwards derivation
    byp = [NaN] + derive_series(xs[1:], ys, derive_backwards)
    plt.plot(xs, byp, "o-", color="orange", label="Differanskvot bakåt")

    # Central derivation
    cyp = [NaN] + derive_series(xs[1:-1], ys, derive_center) + [NaN]
    plt.plot(xs, cyp, "o-", color="deeppink", label="Central differanskvot")

    smp5 = simple_moving_avarage(ys, 5)
    plt.plot(xs, smp5, label="Glidande medelvärde, fönster 5")

    smp2 = simple_moving_avarage(ys, 2)
    plt.plot(xs, smp2, label="Glidande medelvärde, fönster 2")

    # Print stuff
    df = pd.DataFrame({
        "Hour": xs,
        "Temp": ys,
        "Forward derive": fyp,
        "Backwards derive": byp,
        "Central derive": cyp,
        "Moving avarage 5": smp5,
        "Moving avarage 2": smp2
    })
    with open("./malmonow.txt", "w+") as fp:
        fp.write(df.to_string())

    from_time = epoch_to_date(ts["from"]).strftime("%Y-%m-%d %H:%M")
    to_time = epoch_to_date(ts["to"]).strftime("%Y-%m-%d %H:%M")
    plt.suptitle(ts["station"] + ", " + from_time + " till " + to_time)
    plt.legend(loc="upper left", fontsize="xx-small")

    plt.ylim(ymax=(max(ys) + 3))
    plt.grid(True)
    plt.savefig("./malmonow.png")
    plt.clf()


if __name__ == "__main__":
    main()
