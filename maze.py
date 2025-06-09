import cv2
import numpy as np


# A class to store the x and y coordinate of a point
# The + and = operators are overloaded to work for it
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if other is None:  # Handle comparison with None if necessary
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)


mouse_click_status = 0
# a flag variable to store status of mouse clicks.
# 0 -> no clicks
# 1 -> first click (start)
# 2 -> second click (end) / BFS ready

rw = 4  # for position of the rectangle drawn on image when clicked

start = Point()  # starting point
end = Point()  # ending point

# directions of surrounding nodes for BFS
directions = [Point(0, -1), Point(0, 1), Point(1, 0), Point(-1, 0)]  # N, S, E, W

# Global variables for image dimensions, to be set after image loading
h, w = 0, 0
img = None
original_processed_img = None  # To store a copy for resetting

# The BFS function:
# All the pixels surrounding the starting pixel acts as neighbouring nodes
# Breadth First Search is performed until the ending point is found
def bfs(s, e):
    global img, h, w  # Use global image and dimensions

    if img is None:
        print("Error: Image not loaded for BFS.")
        return

    # Validate start and end points are within bounds
    if not (0 <= s.y < h and 0 <= s.x < w):
        print(f"Error: Start point ({s.x}, {s.y}) is out of image bounds ({w}, {h}).")
        return
    if not (0 <= e.y < h and 0 <= e.x < w):
        print(f"Error: End point ({e.x}, {e.y}) is out of image bounds ({w}, {h}).")
        return

    # Validate that start and end points are on path pixels (white)
    # In the BGR image, white is (255, 255, 255)
    start_pixel_color = img[s.y][s.x]
    end_pixel_color = img[e.y][e.x]

    # Check if the start point is on a white pixel
    if not (start_pixel_color[0] == 255 and start_pixel_color[1] == 255 and start_pixel_color[2] == 255):
        print(
            f"Error: Start point ({s.x},{s.y}) with color {start_pixel_color} is not on a white path pixel (255,255,255). BFS cannot start.")
        print("Please click on a white path area for the start point.")
        return

    # Check if the end point is on a white pixel (optional, can be a warning)
    if not (end_pixel_color[0] == 255 and end_pixel_color[1] == 255 and end_pixel_color[2] == 255):
        print(
            f"Warning: End point ({e.x},{e.y}) with color {end_pixel_color} is not on a white path pixel (255,255,255). Path may not be found to this specific pixel if it's a wall.")
        # Allow BFS to run, it might find a path to an adjacent white pixel if 'e' itself is a wall.

    print(f"BFS started from ({s.x},{s.y}) to ({e.x},{e.y})")

    found = False
    queue = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    parent = [[None for _ in range(w)] for _ in range(h)]

    queue.append(s)
    visited[s.y][s.x] = 1

    while len(queue) > 0:
        p = queue.pop(0)

        if p == e:
            found = True
            break

        for d in directions:
            cell = p + d
            # Check if cell is in range, not visited, and is a path (not black in BGR)
            if (0 <= cell.x < w and 0 <= cell.y < h and
                    visited[cell.y][cell.x] == 0 and
                    (img[cell.y][cell.x][0] != 0 or img[cell.y][cell.x][1] != 0 or img[cell.y][cell.x][2] != 0)):

                queue.append(cell)
                visited[cell.y][cell.x] = 1
                parent[cell.y][cell.x] = p

                if cell != e and cell != s:
                    img[cell.y][cell.x] = [255, 0, 255]  # Magenta for explored path

                if cell == e:
                    found = True
                    break
        if found:
            break

    del queue[:]

    if found:
        print("Path found by BFS!")
        path = []
        curr = e
        while curr is not None:
            path.append(curr)
            if curr == s:
                break
            curr = parent[curr.y][curr.x]
            if curr is None and path[-1] != s:
                print(
                    f"Warning: Path reconstruction incomplete. Parent not found for point before ({path[-1].x},{path[-1].y}).")
                path.clear()
                break

        if not path or path[-1] != s:
            if path:
                print("Path reconstruction failed or did not reach the start point.")
        else:
            path.reverse()
            for p_point in path:
                if 0 <= p_point.y < h and 0 <= p_point.x < w:
                    img[p_point.y][p_point.x] = [0, 255, 0]  # Green for the final path
            # Ensure start and end points are also green
            if 0 <= s.y < h and 0 <= s.x < w: img[s.y][s.x] = [0, 255, 0]
            if 0 <= e.y < h and 0 <= e.x < w: img[e.y][e.x] = [0, 255, 0]
            print(f"Path drawn with {len(path)} points.")
    else:
        print("Path not found by BFS exploration.")


def mouse_click(event, px, py, flags, param):
    global img, mouse_click_status, start, end, rw, original_processed_img, h, w

    if img is None:
        return

    if not (0 <= px < w and 0 <= py < h):
        print(f"Click ({px},{py}) is outside image bounds ({w},{h}).")
        return

    if event == cv2.EVENT_LBUTTONUP:
        if mouse_click_status == 0:
            if original_processed_img is not None:
                img[:] = original_processed_img[:]

            cv2.rectangle(img, (px - rw, py - rw), (px + rw, py + rw), (0, 0, 255), -1)
            start = Point(px, py)
            mouse_click_status = 1
            print(f"Start point selected: ({start.x}, {start.y})")

        elif mouse_click_status == 1:
            if px == start.x and py == start.y:
                print("End point cannot be the same as start point. Select a different end point.")
                return

            cv2.rectangle(img, (px - rw, py - rw), (px + rw, py + rw), (255, 0, 0), -1)
            end = Point(px, py)
            mouse_click_status = 2
            print(f"End point selected: ({end.x}, {end.y}). Ready for BFS.")


def load_and_process_image(filename="ex.png"):
    global img, h, w, original_processed_img

    loaded_img = cv2.imread(filename)
    if loaded_img is None:
        print(f"Error: Could not read image '{filename}'. Make sure it's in the correct path.")
        return False

    processed_img = cv2.cvtColor(loaded_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.bitwise_not(processed_img)
    processed_img = cv2.resize(processed_img, (1080, 720), interpolation=cv2.INTER_NEAREST)

    # Thresholding
    _, processed_img = cv2.threshold(processed_img, 171, 255, cv2.THRESH_BINARY)

    # --- Morphological Closing to remove small black dots in white paths ---
    # A kernel is a small matrix of 1s that defines the neighborhood for the operation.
    # A 3x3 or 5x5 kernel is usually good for small noise.
    kernel_size = 3  # Try 3 or 5. Larger kernels close larger holes but can also distort paths.
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Apply morphological closing: Dilation followed by Erosion
    # This helps to close small holes inside the foreground objects (white paths)
    processed_img = cv2.morphologyEx(processed_img, cv2.MORPH_CLOSE, kernel, iterations=1)
    # You can increase iterations if one pass is not enough, but start with 1.
    print(f"Applied morphological closing with a {kernel_size}x{kernel_size} kernel.")
    # --- End of morphological operation ---

    img = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2BGR)
    original_processed_img = img.copy()

    h, w = img.shape[:2]
    print(f"Image '{filename}' loaded and processed. Dimensions: {w}x{h}")
    return True


def main():
    global img, mouse_click_status, start, end

    image_filename = ""
    while True:
        try:
            choice = input("Enter maze number to solve (1-8): ")
            if 1 <= int(choice) <= 8:
                image_filename = f"{choice}.png"
                break
            else:
                print("Invalid input. Please enter a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    if not load_and_process_image(image_filename):
        return

    cv2.namedWindow("Maze Solver")
    cv2.setMouseCallback("Maze Solver", mouse_click)

    bfs_has_run = False

    while True:
        if img is not None:
            cv2.imshow("Maze Solver", img)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            print("Exiting...")
            break

        if key == ord('r'):
            print("Resetting maze...")
            if not load_and_process_image(image_filename):
                print("Failed to reload image for reset. Exiting.")
                break
            mouse_click_status = 0
            bfs_has_run = False
            start = Point()
            end = Point()
            print("Maze reset. Select new start and end points.")

        if mouse_click_status == 2 and not bfs_has_run:
            print("Preparing to run BFS...")
            if original_processed_img is not None:
                img[:] = original_processed_img[:]

                # Before running BFS, ensure the start/end points are still valid on the *potentially cleaned* original_processed_img
            # The mouse_click function draws on 'img', but BFS should ideally operate on the clean state.
            # However, the current BFS reads directly from global 'img' which has start/end markers.
            # For simplicity, we'll let BFS run on the image that might have markers.
            # A more robust approach would be for BFS to take a copy of original_processed_img.

            # Validate start/end points on the current 'img' state before BFS
            # This check is now also inside BFS, but an early check here can be useful.
            if img is not None:
                start_valid = (0 <= start.y < h and 0 <= start.x < w and \
                               img[start.y][start.x][0] == 255 and img[start.y][start.x][1] == 255 and
                               img[start.y][start.x][2] == 255)
                if not start_valid:
                    print(
                        f"Warning: Start point ({start.x},{start.y}) may not be on a clear path after processing. Please re-select if BFS fails.")

            bfs(start, end)
            bfs_has_run = True
            # mouse_click_status = 3 # Or some other state to indicate "solved"

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
