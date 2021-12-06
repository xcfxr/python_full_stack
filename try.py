from psd_tools import PSDImage
img = PSDImage.open('./2228910733574.PSD')
for layer in img:
    layer.topil().save(f'{layer.name}.png')
    print(layer.top)
    print(layer.bottom)
    print(layer.left)
    print(layer.right)