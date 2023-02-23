# Challange too hard - used posted solution and reviewed the code
with open('input.txt') as file:
    data = file.read().replace(',', '').replace('Sensor at x=', '').replace('y=', '').replace(': closest beacon is at x=', ' ').split('\n')
lines = [[int(y) for y in x.split()] for x in data]

A = 2000000
dist = lambda xs,ys,xb,yb: abs(xs-xb)+abs(ys-yb)
print(max(xs-abs(A-ys)+dist(xs,ys,xb,yb) for xs,ys,xb,yb in lines)-min(xs+abs(A-ys)-dist(xs,ys,xb,yb) for xs,ys,xb,yb in lines))

B =  4000000
func = lambda a,b,c,d,e,f: ((d+e+f+a-b-c)//2, (d+e+f-a+b+c)//2+1)

for X, Y in [func(a[0], a[1], dist(*a), b[0], b[1], dist(*b)) for a in lines for b in lines]:
    if 0<X<B and 0<Y<B and all(dist(X,Y,xs,ys)>dist(xs,ys,xb,yb) for xs,ys,xb,yb in lines):
        print(B*X + Y)