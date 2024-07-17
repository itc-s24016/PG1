#円の面積を計算する関数を作る　円周率が3.14
def make_circle_area(pi = 3.14):
    
    #円の面積を計算する関数
    def circle_area(radius):
        return radius * radius * pi #半径ｘ半径ｘ3,14
        
    return circle_area
    
area_default = make_circle_area()
area_precise = make_circle_area(3.1415926535)

print(area_default(2))
print(area_precise(2))
