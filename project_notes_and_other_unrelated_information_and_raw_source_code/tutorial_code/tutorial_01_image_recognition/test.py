from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy

# now, if we want to use the trained model on our custom image
raw_pic = Image.open( "custom_trousers.jpg" ).convert( "L" )
raw_pic = ImageOps.invert( raw_pic )
max_size = ( 28, 28 )
#raw_pic.thumbnail( max_size, Image.ANTIALIAS )
raw_pic = ImageOps.fit( raw_pic, max_size, Image.ANTIALIAS )
pic_array = numpy.array( raw_pic )
pic_array = pic_array / 250.0
print( "resolution of our image: ", pic_array.shape )

plt.figure()                                                                                                                       
plt.grid(True)
plt.imshow( pic_array )
plt.savefig( "converted_custom_image.png" )

test_batch = ( numpy.expand_dims( pic_array, 0 ) )
print( test_batch.shape )


