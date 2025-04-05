#cmyk to rgb
def cmyk_to_rgb(c, m, y, k, cmyk_scale=100, rgb_scale=255): 
    r = round(rgb_scale * (1.0 - c) * (1.0 - k))
    g = round(rgb_scale * (1.0 - m) * (1.0 - k))
    b = round(rgb_scale * (1.0 - y) * (1.0 - k)) 
    return r, g, b

res = cmyk_to_rgb(float(input()),float(input()),float(input()),float(input()))

print(str(res[0])+','+str(res[1])+','+str(res[2]))
