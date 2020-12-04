import h5py
import os


SIZE = 100
FRAMES = 100000

DATA_FILE_PATH = os.path.abspath(
    __file__ + f'/../../data/game_of_life_{SIZE}-{FRAMES}.h5')
H5PY_DATASET_NAME = 'gol_frames'


def preview_dataset(frame):
    file = h5py.File(DATA_FILE_PATH, 'r')
    dataset = file[H5PY_DATASET_NAME]
    print(f'\nShape: {dataset.shape}')
    print(f'Preview for dataset (frame: {frame}):\n{dataset[frame]}')


preview_dataset(0)
