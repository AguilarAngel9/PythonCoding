import math

def interplane_distance(theta_2):
    '''
    A function that calculate the sc, bcc and fcc given an array of theta angles.
    '''
    theta = [i/2 for i in theta_2]
    sin_theta = [math.sin(math.radians(t)) for t in theta]
    sqr_theta = [math.sin(math.radians(t))**2 for t in theta]
    rel_sc = [s/sqr_theta[0] for s in sqr_theta]
    rel_bcc = [round(r*2) for r in rel_sc]
    rel_fcc = [round(r*3) for r in rel_sc]
    d = [0.7107/(2*t) for t in sin_theta]

    return rel_sc, rel_bcc, rel_fcc, d

datos = [20.20, 28.72, 35.36, 41.07, 46.19, 50.90, 55.28, 59.42]

rel_sc, rel_bcc, rel_fcc, d = interplane_distance(datos)

print(f'sc: {rel_sc}')
print(f'bcc: {rel_bcc}')
print(f'fcc: {rel_fcc}')
print(f'd: {d}')
