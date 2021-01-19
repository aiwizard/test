import sys
import json



def main():
    if( len(sys.argv) != 2 ):
        print("\tusage: python json2yolo <jsonfile>")

    src = sys.argv[1]
    #rst = src.replace('.json', '.txt')
    #print(src, rst)

    #'''
    fr = open(src, 'r', encoding="utf-8").read()
    jsonStr = json.loads(fr)

    cnt = len(jsonStr)
    #print(cnt)

    for i in range(cnt):
        class_val = i
        x, y = jsonStr[i].get("Point(x,y)").split(',')
        w = jsonStr[i].get("W")
        h = jsonStr[i].get("H")

        format_str = "{} {} {} {} {}".format(class_val, x, y, w, h)
        #print(format_str)

        serving_size = jsonStr[i].get("Serving Size")
        camera_angle = jsonStr[i].get("Camera Angel")
        cardinal_angel = jsonStr[i].get("Cardinal Angle")
        color_of_container = jsonStr[i].get("Color of Container")
        material_of_container = jsonStr[i].get("Material of Container")
        illuminance = jsonStr[i].get("Illuminance")

        rstname, rstext = src.split('.')
        idx = "%04d"%(i+1)
        rst = "{}_{}{}{}{}{}{}_{}.txt".format(rstname, serving_size, camera_angle, cardinal_angel, color_of_container, material_of_container, illuminance, idx)

        fw = open(rst, 'w', encoding="utf-8")
        fw.write(format_str)
        fw.close()

    print(".")

    '''
    data = '{"title": "Book1", "ISBN": "12345", "author": [{"name": "autho1", "age": 30}, {"name": "autho2", "age": 25}]}'
    json_data = json.loads(data)

    print(json_data['title'])
    print(json_data['ISBN'])

    #for author in json_data['author']:
    #    print(author['name'])
    #    print(author['age'])
    '''

    pass


if __name__ == '__main__':
	main()