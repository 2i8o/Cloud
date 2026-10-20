#!/usr/bin/env python3
"""sample_size.py - how many impressions per arm to detect a difference in a proportion (e.g. stayed-to-watch).

Normal approximation for two independent proportions, two-sided:
    n = (z_{1-a/2} + z_{power})^2 * (p1(1-p1) + p2(1-p2)) / (p1 - p2)^2
Assumes independent viewers and random assignment. Organic posts are NOT randomised, so treat the result as a
lower bound on what you need and a sanity check on whether a test is worth running at all.

Usage: python3 sample_size.py BASELINE_RATE MIN_DETECTABLE_DIFFERENCE [--alpha 0.05] [--power 0.8]
Example: python3 sample_size.py 0.60 0.05   -> about 1468 per arm
"""
import sys
from statistics import NormalDist


def per_arm(p1, delta, alpha=0.05, power=0.8):
    p2 = p1 + delta
    if not (0 < p1 < 1 and 0 < p2 < 1) or delta == 0:
        raise ValueError("rates must be in (0,1) and the difference non-zero")
    z = NormalDist().inv_cdf
    n = (z(1 - alpha / 2) + z(power)) ** 2 * (p1 * (1 - p1) + p2 * (1 - p2)) / delta ** 2
    return int(n) + (0 if n == int(n) else 1)


def main(a):
    if len(a) < 3:
        print(__doc__); return 2
    kw = {"--alpha": 0.05, "--power": 0.8}
    for i, x in enumerate(a):
        if x in kw and i + 1 < len(a): kw[x] = float(a[i + 1])
    n = per_arm(float(a[1]), float(a[2]), kw["--alpha"], kw["--power"])
    print(f"~{n} impressions (viewers shown the video) per arm to detect {a[1]} -> {float(a[1]) + float(a[2]):.3g} "
          f"at alpha={kw['--alpha']}, power={kw['--power']}. Organic posting is not randomised: this is a lower bound.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
