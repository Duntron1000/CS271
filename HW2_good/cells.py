import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import skimage.io
from skimage.transform import resize
from skimage.color import rgb2gray
import time
from unionrankpc import *

def load_cells_grayscale(filename, n_pixels = 0):
    """
    Load in a grayscale image of the cells, where 1 is maximum brightness
    and 0 is minimum brightness

    Parameters
    ----------
    filename: string
        Path to image holding the cells
    n_pixels: int
        Number of pixels in the image
    
    Returns
    -------
    ndarray(N, N)
        A square grayscale image
    """
    cells_original = skimage.io.imread(filename)
    cells_gray = rgb2gray(cells_original)
    # Denoise a bit with a uniform filter
    cells_gray = ndimage.uniform_filter(cells_gray, size=10)
    cells_gray = cells_gray - np.min(cells_gray)
    cells_gray = cells_gray/np.max(cells_gray)
    N = int(np.sqrt(n_pixels))
    if n_pixels > 0:
        # Resize to a square image
        cells_gray = resize(cells_gray, (N, N), anti_aliasing=True)
    return cells_gray


def permute_labels(labels):
    """
    Shuffle around labels by raising them to a prime and
    modding by a large-ish prime, so that cells are easier
    to see against their backround
    Parameters
    ----------
    labels: ndarray(M, N)
        An array of labels for the pixels in the image
    Returns
    -------
    labels_shuffled: ndarray(M, N)
        A new image where the labels are different but still
        the same within connected components
    """
    return (labels**31) % 833


## TODO: Fill in your code here
def get_cell_labels(img, threshold):
    u = UnionFind()
    cellNum = {}
    
    # make a new set for every pixel 
    for x in range(len(img)):
        for y in range(len(img[x])):
            u.makeset((x,y))
            # if any of the adjacent pixels are above the threshold too then union them 
            if x < 399 and x != 0 and img[(x,y)] > threshold and img[(x-1, y)] > threshold:
                u.union((x,y), (x-1, y))
            if y < 399 and y != 0 and img[(x,y)] > threshold and img[(x, y-1)] > threshold:
                u.union((x,y), (x, y-1))
            
                
    # create a 2d array filled with the cell number of each pixel
    cells = np.zeros((len(img), len(img[1])))
    for x in range(len(img)):
        for y in range(len(img[x])):
            if u.root((x,y)) in cellNum:
                cells[x, y] = cellNum[u.root((x,y))]
            else:
                root = u.root((x,y)) 
                cells[x,y] = len(cellNum) + 1
                cellNum[u.root((x,y))] = len(cellNum) + 1
    return cells

def get_cluster_centers(img):
    avgs = {}
    for x in range(len(img)):
        for y in range(len(img[x])):
            if img[x,y] in avgs:
                avgs[img[x,y]].append([x,y])
            else:
                avgs[img[x,y]] = [[x,y]]
    res = []
    for key in avgs:
        if len(avgs[key]) > 1:  
            avgx = 0
            avgy = 0
            num = len(avgs[key])  # Counting the number of points in the cluster
            for i in avgs[key]:
                avgx += i[0]
                avgy += i[1]
            
            # Calculate the average coordinates
            avgx /= num
            avgy /= num
            res.append((avgx, avgy))
    return res

                     
if __name__ == '__main__':
    I = load_cells_grayscale("Cells.jpg")
    plt.imshow(I, cmap='magma')
    plt.show()