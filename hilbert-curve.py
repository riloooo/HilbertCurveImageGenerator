from PIL import Image
#evantard
def rotate_right(l):
    out = l.copy()
    out=transpose(out)
    out=reverse_rows(out)
    return out
def rotate_left(l):
    out=l.copy()
    out=reverse_rows(out)
    out=transpose(out)
    return out
def transpose(l):
    out=[[None for x in range(len(l[0]))]for y in range(len(l))]
    for y in range(len(out)):
        for x in range(y,len(out[0])):
            out[y][x]=l[x][y]
            out[x][y]=l[y][x]
    return out
def reverse_rows(l):
    out=[[None for x in range(len(l[0]))]for y in range(len(l))]
    for y in range(len(l)):
        out[y]=l[y][::-1]
    return out
def hilbert_curve(detail_level):
    curve=[[1,1,1],
          [1,0,1], 
          [1,0,1]]
    for curr_detail_level in range(1,detail_level+1):
        right_curve=rotate_right(curve)
        left_curve=rotate_left(curve)
        new_curve_size = 7*2**(curr_detail_level-1)+2**(curr_detail_level-1)-1
        new_curve=[[None for x in range(new_curve_size)] for y in range(new_curve_size)]
        for y in range(len(curve)):
            new_curve[y] = curve[y] +[0]+ curve[y]
        new_curve[new_curve_size//2 - 1][new_curve_size//2]=1
        new_curve[new_curve_size//2]=[1]+[0 for _ in range(new_curve_size-2)]+[1]
        for i in range(len(curve)):
            y= i+new_curve_size//2+1
            new_curve[y]=right_curve[i] + [0] + left_curve[i]
        curve= new_curve.copy()
    return curve

detail = int(input("Detail level: "))
curve = hilbert_curve(detail)
size = len(curve)
img = Image.new('1',(size,size))
for y in range(size):
    for x in range(size):
        val = curve[y][x]
        if val == 1:
            img.putpixel((x,y),0)
        else:
            img.putpixel((x,y),1)
location=input("Enter image name: ")
if len(location) <= 4 or location[-4:].lower() != ".png":
    location += ".png"
img.save(location)





