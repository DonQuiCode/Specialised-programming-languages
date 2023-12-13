from cube import Cube
import sys

def main():
    cube = Cube(width=10, speed=2)

    try:
        sys.stdout.write('\x1b[2J')
        while True:
            sys.stdout.write('\x1b[H')

            cube.update()
            cube.draw()
    except KeyboardInterrupt:
        sys.stdout.write('\x1b[2J')
        sys.stdout.write('\x1b[H')
        
if __name__ == '__main__':
    main()