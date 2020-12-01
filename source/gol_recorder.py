import numpy as np
import h5py

ON = 255
OFF = 0
vals = [ON, OFF]

SIZE = 100
FRAMES = 10
OUTPUT_FILE_PATH = 'game_of_life_frames.h5'
DATASET_NAME = 'gol_frames'


def randomGrid(size):
    return np.random.choice(vals, size=size*size, p=[0.2, 0.8]).reshape(size, size)


def updateGrid(grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1) % N] + grid[i, (j+1) % N] +
                         grid[(i-1) % N, j] + grid[(i+1) % N, j] +
                         grid[(i-1) % N, (j-1) % N] + grid[(i-1) % N, (j+1) % N] +
                         grid[(i+1) % N, (j-1) % N] + grid[(i+1) % N, (j+1) % N])/255)

            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    return newGrid


def main():
    grid = randomGrid(SIZE)

    with h5py.File(OUTPUT_FILE_PATH, 'w') as f:
        dst = f.create_dataset(DATASET_NAME, shape=(FRAMES, SIZE, SIZE),
                               dtype=np.uint8)
        for frame in range(FRAMES):
            dst[frame] = grid
            grid = updateGrid(grid, SIZE)
    print(
        f'Saved at destination: {OUTPUT_FILE_PATH}. Dataset name: {DATASET_NAME}.')


if __name__ == '__main__':
    main()
