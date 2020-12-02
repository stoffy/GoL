import h5py
import os


SIZE = 100
FRAMES = 10
DATA_FILE_PATH = os.path.abspath(
    __file__ + f'/../../data/game_of_life_{SIZE}-{FRAMES}.h5')
H5PY_DATASET_NAME = 'gol_frames'


f = h5py.File(DATA_FILE_PATH, 'r')
dataset = f[H5PY_DATASET_NAME]

print(dataset[0])
