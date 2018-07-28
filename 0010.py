
def circumcenter(vert1, vert2, vert3):
    # H/T: wikipedia.org/wiki/Circumscribed_circle
    # refer from https://gist.github.com/dhermes/9ce057da49df63345c33
    Ax, Ay = vert1
    Bx, By = vert2
    Cx, Cy = vert3

    D = 2 * (Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By))
    norm_A = Ax**2 + Ay**2
    norm_B = Bx**2 + By**2
    norm_C = Cx**2 + Cy**2

    Ux = norm_A * (By - Cy) + norm_B * (Cy - Ay) + norm_C * (Ay - By)
    Uy = -(norm_A * (Bx - Cx) + norm_B * (Cx - Ax) + norm_C * (Ax - Bx))

    r = (Ax - Ux/D)*(Ax - Ux/D) + (Ay - Uy/D)* (Ay - Uy/D)
    r = float(r)**0.5
    return [Ux/D, Uy/D, r]

n  = int(input())
for i in range(n):
  xs = list(map(float, input().split()))
  a = circumcenter(xs[0:2], xs[2:4], xs[4:6])
  print(' '.join(map(lambda x:f'{x:0.03f}', a)))
