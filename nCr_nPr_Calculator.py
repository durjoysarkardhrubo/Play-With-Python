n=int(input("n:"))
r=int(input("r(r<n):"))
v=n-r+1
f=1
while v<=n :
  f=f*v
  v+=1
print(f"nPr: {f}")


x=1
i=1
while i<=r:
  x=x*i
  i+=1
  c=int(f/x)
print(f"nCr: {c}")
