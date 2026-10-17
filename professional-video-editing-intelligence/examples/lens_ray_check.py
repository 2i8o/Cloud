#!/usr/bin/env python3
"""Physics QC for a lens-ray graphic: trace parallel rays through a plano-convex lens
(curved face toward the light) with Snell's law, so animated ray paths can be generated
or checked from numbers instead of drawn by eye.

Used by examples/motion-graphics-sequence.md as a worked "physical correctness" test.
Pure standard library. Units: millimetres.

  python lens_ray_check.py            # defaults: n=1.5, R=50, thickness 6, heights 4..20
  python lens_ray_check.py --n 1.52 --R 60 --t 5
"""
import argparse
import math


def refract(d, n_hat, n1, n2):
    """Vector Snell refraction. d = unit incident direction; n_hat = unit normal pointing
    against the incident ray (toward the side the ray comes from). Returns unit direction
    or None on total internal reflection."""
    cos_i = -(d[0] * n_hat[0] + d[1] * n_hat[1])
    eta = n1 / n2
    k = 1.0 - eta * eta * (1.0 - cos_i * cos_i)
    if k < 0:
        return None
    s = eta * cos_i - math.sqrt(k)
    return (eta * d[0] + s * n_hat[0], eta * d[1] + s * n_hat[1])


def trace(y0, n, R, t):
    """Ray travelling +x at height y0. Curved surface: sphere of radius R centred at (R, 0),
    vertex at x=0. Flat surface at x=t. Returns (axis_crossing_x, path points)."""
    x1 = R - math.sqrt(R * R - y0 * y0)                      # hit on curved surface
    # outward normal at P points away from centre; incident side normal = (P - C)/R
    nx, ny = (x1 - R) / R, y0 / R
    d1 = refract((1.0, 0.0), (nx, ny), 1.0, n)
    if d1 is None:
        return None, []
    # propagate inside glass to the flat face x = t
    s = (t - x1) / d1[0]
    y2 = y0 + s * d1[1]
    # flat face: normal against the incident ray is (-1, 0)
    d2 = refract(d1, (-1.0, 0.0), n, 1.0)
    if d2 is None:
        return None, []
    # cross with the axis y = 0 after the flat face
    if abs(d2[1]) < 1e-12:
        return None, []
    sx = -y2 / d2[1]
    xf = t + sx * d2[0]
    return xf, [(-10.0, y0), (x1, y0), (t, y2), (xf, 0.0)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=float, default=1.5)
    ap.add_argument("--R", type=float, default=50.0)
    ap.add_argument("--t", type=float, default=6.0, help="centre thickness (flat face at x=t)")
    ap.add_argument("--heights", default="4,8,12,16,20")
    a = ap.parse_args()

    f_thin = a.R / (a.n - 1.0)                    # thin-lens focal length (lensmaker, plano-convex)
    bfl_paraxial = f_thin - a.t / a.n             # approx. back focal length from the flat face
    print(f"n={a.n}  R={a.R} mm  t={a.t} mm")
    print(f"Thin-lens estimate  f = R/(n-1) = {f_thin:.1f} mm; paraxial back focus ~ {bfl_paraxial:.1f} mm "
          f"behind the flat face (approximation).\n")
    print("ray height  axis-crossing (mm behind flat face)  offset from paraxial")
    for h in [float(v) for v in a.heights.split(",")]:
        xf, _ = trace(h, a.n, a.R, a.t)
        if xf is None:
            print(f"{h:>9.1f}  no exit ray (total internal reflection)")
            continue
        behind = xf - a.t
        print(f"{h:>9.1f}  {behind:>10.2f}                              {behind - bfl_paraxial:+.2f}")
    print("\nReading: rays near the axis cross near the paraxial focus; marginal rays cross closer to "
          "the lens (spherical aberration). A diagram where all rays meet at one point is a deliberate "
          "simplification - say so, or show the spread if accuracy is the point.")


if __name__ == "__main__":
    main()
