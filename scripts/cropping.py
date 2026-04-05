import os
import csv
import cv2

# ======================
# CONFIG
# ======================
BASE_PATH = "syntax-findit/data/train"
FOLDER_NAME = "fakemask"
IMG_EXT = ('.jpg', '.jpeg', '.png')

MAX_WIDTH = 1000   # batas lebar window
MAX_HEIGHT = 700   # batas tinggi window

img_dir = os.path.join(BASE_PATH, FOLDER_NAME)
csv_path = f"syntax-findit/data/cropped/{FOLDER_NAME}.csv"

os.makedirs(os.path.dirname(csv_path), exist_ok=True)

print("Folder:", img_dir)
print("CSV:", csv_path)

# ======================
# GET IMAGE LIST
# ======================
image_files = [
    f for f in os.listdir(img_dir)
    if f.lower().endswith(IMG_EXT)
]

image_files.sort()
print(f"Total images: {len(image_files)}")

# ======================
# RESIZE FUNCTION
# ======================
def resize_to_fit(img, max_w, max_h):
    h, w = img.shape[:2]

    scale = min(max_w / w, max_h / h, 1.0)
    new_w, new_h = int(w * scale), int(h * scale)

    return cv2.resize(img, (new_w, new_h)), scale

# ======================
# CSV SETUP
# ======================
file_exists = os.path.isfile(csv_path)
csv_file = open(csv_path, mode="a", newline="")
writer = csv.writer(csv_file)

if not file_exists:
    writer.writerow(["img_path", "x", "y", "w", "h"])

# ======================
# LOOP IMAGES
# ======================
for idx, img_name in enumerate(image_files):
    img_path = os.path.join(img_dir, img_name)
    print(f"\n[{idx+1}/{len(image_files)}] {img_name}")

    img = cv2.imread(img_path)

    if img is None:
        print("Gagal load:", img_path)
        continue

    # ======================
    # RESIZE BIAR GA GEDE
    # ======================
    display_img, scale = resize_to_fit(img, MAX_WIDTH, MAX_HEIGHT)

    # ======================
    # SELECT ROI
    # ======================
    cv2.namedWindow("Select ROI", cv2.WINDOW_NORMAL)
    cv2.imshow("Select ROI", display_img)

    x, y, w, h = cv2.selectROI("Select ROI", display_img, showCrosshair=True, fromCenter=False)
    cv2.destroyWindow("Select ROI")

    if w == 0 or h == 0:
        print("Skip / kemungkinan window ditutup")
        continue

    # ======================
    # BALIKIN KE UKURAN ASLI
    # ======================
    x = int(x / scale)
    y = int(y / scale)
    w = int(w / scale)
    h = int(h / scale)

    # ======================
    # SAVE CSV
    # ======================
    writer.writerow([img_path, x, y, w, h])
    csv_file.flush()
    print(f"Saved: x={x}, y={y}, w={w}, h={h}")

    # ======================
    # PREVIEW CROP
    # ======================
    cropped = img[y:y+h, x:x+w]
    preview, _ = resize_to_fit(cropped, MAX_WIDTH, MAX_HEIGHT)

    cv2.namedWindow("Cropped", cv2.WINDOW_NORMAL)
    cv2.imshow("Cropped", preview)

    print("SPACE/ENTER → next | ESC → stop | ❌ → stop")

    while True:
        key = cv2.waitKey(1)

        # kalau window ditutup manual
        if cv2.getWindowProperty("Cropped", cv2.WND_PROP_VISIBLE) < 1:
            print("Window closed → stop")
            csv_file.close()
            cv2.destroyAllWindows()
            exit()

        if key == 27:  # ESC
            print("Stopped by user")
            csv_file.close()
            cv2.destroyAllWindows()
            exit()

        if key in [13, 32]:  # ENTER / SPACE
            break

    cv2.destroyWindow("Cropped")

# ======================
# CLEANUP
# ======================
csv_file.close()
cv2.destroyAllWindows()

print("\nDone.")