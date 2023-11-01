import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from scipy import misc

bases = 0



def grad_energy(img, sigma = 3):
    """
    Compute the gradient magnitude of an image by doing
    1D convolutions with the derivative of a Gaussian
    
    Parameters
    ----------
    img: ndarray(M, N, 3)
        A color image
    sigma: float
        Width of Gaussian to use for filter
    
    Returns
    -------
    ndarray(M, N): Gradient Image
    """
    I = 0.2125*img[:, :, 0] + 0.7154*img[:, :, 1] + 0.0721*img[:, :, 2]
    I = I/255
    N = int(sigma*6+1)
    t = np.linspace(-3*sigma, 3*sigma, N)
    dgauss = -t*np.exp(-t**2/(2*sigma**2))
    IDx = convolve2d(I, dgauss[None, :], mode='same')
    IDy = convolve2d(I, dgauss[:, None], mode='same')
    GradMag = np.sqrt(IDx**2 + IDy**2)
    return GradMag


def plot_seam(img, seam):
    """
    Plot a seam on top of the image
    Parameters
    
    ----------
    I: ndarray(nrows, ncols, 3)
        An RGB image
    seam: ndarray(nrows, dtype=int)
        A list of column indices of the seam from
        top to bottom
    """
    plt.imshow(img)
    X = np.zeros((len(seam), 2))
    X[:, 0] = np.arange(len(seam))
    X[:, 1] = np.array(seam, dtype=int)
    plt.plot(X[:, 1], X[:, 0], 'r')

def read_image(path):
    """
    A wrapper around matplotlib's image loader that deals with
    images that are grayscale or which have an alpha channel

    Parameters
    ----------
    path: string
        Path to file
    
    Returns
    -------
    ndarray(M, N, 3)
        An RGB color image in the range [0, 1]
    """
    img = plt.imread(path)
    if np.issubdtype(img.dtype, np.integer):
        img = np.array(img, dtype=float)/255
    if len(img.shape) == 3:
        if img.shape[1] > 3:
            # Cut off alpha channel
            img = img[:, :, 0:3]
    if img.size == img.shape[0]*img.shape[1]:
        # Grayscale, convert to rgb
        img = np.concatenate((img[:, :, None], img[:, :, None], img[:, :, None]), axis=2)
    return img


def getOptimalCost(E, i, j, mem):
    if (i,j) in mem:
        res = mem[(i,j)]

    elif i == 0:
        global bases
        bases += 1
        mem[(0, j)] = E[0, j]
        res = E[i, j]

    else:
        ul = 1
        if j > 0:
            ul = getOptimalCost(E, i-1, j-1, mem)
        u = getOptimalCost(E, i-1, j, mem)
        ur = 1
        if j < len(E[i]) - 1:
            ur = getOptimalCost(E, i-1, j+1, mem)
        res = E[i, j] + min(ul, u, ur)
        mem[(i, j)] = res
    return res

def getOptimalCostDyn(E):
    """
    E: two dimentional Array representing the energy image of an image
    """
    C = np.zeros([len(E), len(E[0])])
    for i in range(0, len(C)):
        for j in range(len(C[i])):
            if i == 0:
                C[0, j] = E[0, j]
            else:
                case1 = 10
                case2 = 10
                case3 = 10
                if j > 0:
                    case1 = C[i-1, j-1]
                if j < len(C[i]) - 1:
                    case3 = C[i-1, j+1]
                case2 = C[i-1,j]
                
                C[i, j] = E[i,j] + min(case1, case2, case3)
    return C

def image_seam(C, E):
    seam = []
    min = 100
    i = len(C) - 1
    j = 0
    for m in range(i):
        if C[-1][m] < min:
            min = C[-1][m]
            j = m
            
    while i > 0:
        seam.append(j)
        case1 = E[i,j]
        case2 = E[i,j]
        case3 = E[i,j]

        if j > 0:
            case1 += C[i - 1, j - 1]
        case2 += C[i - 1, j]
        if j < len(C[i]):
            case3 += C[i - 1, j + 1] 

        if case1  == C[i,j]:
            i = i - 1
            j = j - 1
        elif case2  == C[i,j]:
            i = i - 1
        elif case3 == C[i, j]:
            i = i - 1
            j = j + 1
    seam.reverse()
    print(seam)
    return seam

def remove_seam(img, seam):
    return img

# |%%--%%| <NONE|w0MxjtqOIf>
img = read_image("HW3_SeamCarving-main/LivingRoom.jpg")

for i in range(1):
    print(i)
    G = grad_energy(img)
    C = getOptimalCostDyn(G)
    seam = image_seam(C, G)
    print(img)
    img = remove_seam(img, seam)
plot_seam(img, seam)
plt.show()
