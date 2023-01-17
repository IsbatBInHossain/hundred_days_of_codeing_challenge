import colorgram


def color_list():
    colors = colorgram.extract('image.jpg', 30)
    colors_rgb = []
    for i in range(len(colors)):
        color = colors[i]
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]
        if r < 245 and g < 245 and b < 245:
            rgb = (r, g, b)
            colors_rgb.append(rgb)
    return colors_rgb


print(color_list())