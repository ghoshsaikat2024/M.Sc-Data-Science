# """
# -----------------------------------------------------------------------------
# Statelite image(band4.gif) point annotation
# -----------------------------------------------------------------------------
# AUTHOR: Soumitra Samanta (soumitra.samanta@gm.rkmvu.ac.in)
# -----------------------------------------------------------------------------
# Package required:
# Numpy: https://numpy.org/
# scikit-image: https://scikit-image.org/
# OpenCV: https://opencv.org/
# pandas: https://pandas.pydata.org/
# -----------------------------------------------------------------------------
# """

# import numpy as np
# import skimage.io as io
# import cv2
# import pandas as pd
# import matplotlib.pyplot as plt


# def draw_point(event, x, y, flags, param):
#     """Take one point"""
    
#     global points_pos, count_points
    
#     if event == plt.EVENT_LBUTTONDBLCLK:   
# #     if event == plt.EVENT_LBUTTONDOWN: #For macOS High Sierra


#         plt.drawMarker(img, (x, y), color=(255,255,255), markerType=plt.MARKER_CROSS, markerSize=5)
#         points_pos.append((y, x))
#         count_points += 1
#         print('Position of {}-th point: ({}, {})' .format(count_points, x,y))
        
        
# if __name__ == '__main__':
    
#     # IMAGE FILE NAME YOU WANT TO READ
#     image_path = r'C:\Users\Saikat\Downloads\naive_bayes_assgn_materials\\'  #change your dataset path
    
#     img_filename = 'band4.gif'

#     img = plt.imread(''.join([image_path, img_filename]))
#     print('Input image size: {}' .format(img.shape))

#     # TO STORE ANNOTATED POINTS
#     points_pos = []
#     count_points = 0

#     num_poins = int(input('How many points would you like to annotate? '))

#     plt.namedWindow('Move mouse pointer and double click to locate the position')
#     plt.setMouseCallback('Move mouse pointer and double click to locate the position', draw_point)

#     while(1):
#         plt.imshow('Move mouse pointer and double click to locate the position', img)
#         k = plt.waitKey(20) & 0xFF
#         if(k == 27 or count_points==num_poins):
#             # WRITE ANNOTATED IMAGE
#             img_save_filename = ''.join([
#                 image_path, 
#                 'annotated_', img_filename.split('.')[0], 
#                 '_np_', str(len(points_pos)), 
#                 '.gif'
#             ])
#             plt.imsave(img_save_filename, img)
            
#             # SAVE ANNOTATED POINTS AS CSV FILE
#             pd.DataFrame(
#                 data=np.asarray(points_pos), 
#                 columns = ['row', 'column']
#             ).to_csv(''.join([
#                 image_path, 
#                 'annotated_points_', img_filename.split('.')[0], 
#                 '_np_', str(len(points_pos)), 
#                 '.csv'
#             ]), index=False)
            
#             break
            
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def draw_point(event):
    """Take one point"""
    
    global points_pos, count_points
    
    if event.button == 1:  # Check if left mouse button is clicked
        x, y = event.xdata, event.ydata
        plt.scatter(x, y, color='white', marker='x')
        points_pos.append((y, x))
        count_points += 1
        print('Position of {}-th point: ({}, {})' .format(count_points, x, y))
        plt.draw()
        
        if count_points == num_points:
            plt.close()
        

if __name__ == '__main__':
    
    # IMAGE FILE NAME YOU WANT TO READ
    image_path = r'C:\Users\Saikat\Downloads\naive_bayes_assgn_materials\\'  # change your dataset path
    img_filename = 'band4.gif'

    img = plt.imread(''.join([image_path, img_filename]))
    print('Input image size: {}' .format(img.shape))

    # TO STORE ANNOTATED POINTS
    points_pos = []
    count_points = 0

    num_points = int(input('How many points would you like to annotate? '))

    plt.figure()
    plt.imshow(img)
    plt.title('Move mouse pointer and left-click to locate the position')
    plt.connect('button_press_event', draw_point)
    plt.show()

    # SAVE ANNOTATED POINTS AS CSV FILE
    pd.DataFrame(
        data=np.asarray(points_pos), 
        columns=['row', 'column']
    ).to_csv(''.join([
        image_path, 
        'annotated_points_', img_filename.split('.')[0], 
        '_np_', str(len(points_pos)), 
        '.csv'
    ]), index=False)

