def trapezoid_integrate_method(f,a,b,N):
    deltX = (b-a)/N
    s=0
    for i in range(1,N):
        s += f(a + i*deltX)
    return (b-a)/(2*N)*(f(a)+f(b)+2*s)


print("trapezoids give", trapezoid_integrate_method(lambda x: x**4-2*x+1,0,2,1000))
