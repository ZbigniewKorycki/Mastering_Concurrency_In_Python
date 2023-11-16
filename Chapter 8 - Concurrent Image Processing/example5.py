from multiprocessing import Pool
import cv2

import sys
from timeit import default_timer as timer

THRESH_METHOD = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
INPUT_PATH = 'large_input/'
OUTPUT_PATH = 'large_output/'

n = 20

names = [f'ship_{i}_{j}.png' for i in range(n) for j in range(n)]


def process_threshold(im, output_name, thresh_method):
    gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    thresh_im = cv2.adaptiveThreshold(gray_im, 255, thresh_method, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite(OUTPUT_PATH + output_name, thresh_im)


if __name__ == "__main__":
    for n_processes in range(1, 7):
        start = timer()

        with Pool(n_processes) as p:
            p.starmap(process_threshold, [(cv2.imread(INPUT_PATH + name), name, THRESH_METHOD) for name in names])

        print(f'Took {timer() - start} seconds with {n_processes} process(es)')

    print('Done')

