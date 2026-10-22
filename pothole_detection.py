
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "images" / "road2.jpg"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Step 1: Load the road image
image = cv2.imread(str(IMAGE_PATH))

if image is None:
    raise FileNotFoundError(
        f"Could not load {IMAGE_PATH}. Check the image filename and folder."
    )

# Resize large images while preserving aspect ratio
max_width = 1000
if image.shape[1] > max_width:
    scale = max_width / image.shape[1]
    image = cv2.resize(
        image, None, fx=scale, fy=scale,
        interpolation=cv2.INTER_AREA
    )

# Step 2: Convert BGR image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Reduce noise using Gaussian smoothing
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 4: Detect edges using Canny
edges = cv2.Canny(blurred, 50, 150)

# Step 5: Threshold dark regions
_, threshold = cv2.threshold(
    blurred, 0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# Step 6: Combine threshold and edge information
combined = cv2.bitwise_and(threshold, threshold, mask=edges)
# If too few candidates appear, we will tune this method.

# Step 7: Find candidate regions
contours, _ = cv2.findContours(
    threshold.copy(),
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

result = image.copy()
candidate_count = 0

for contour in contours:
    area = cv2.contourArea(contour)

    # Ignore very small regions and huge background regions
    if area < 500 or area > 0.20 * image.shape[0] * image.shape[1]:
        continue

    x, y, w, h = cv2.boundingRect(contour)

    # Ignore very thin regions
    if w < 15 or h < 15:
        continue

    candidate_count += 1
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(
        result, "Candidate",
        (x, max(y - 8, 20)),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2
    )

# Step 8: Save intermediate and final outputs
cv2.imwrite(str(OUTPUT_DIR / "grayscale.jpg"), gray)
cv2.imwrite(str(OUTPUT_DIR / "filtered.jpg"), blurred)
cv2.imwrite(str(OUTPUT_DIR / "edges.jpg"), edges)
cv2.imwrite(str(OUTPUT_DIR / "threshold.jpg"), threshold)
cv2.imwrite(str(OUTPUT_DIR / "final_result.jpg"), result)

print("Image processing completed!")
print(f"Image size: {image.shape[1]} x {image.shape[0]}")
print(f"Candidate regions detected: {candidate_count}")
print(f"Results saved in: {OUTPUT_DIR}")

# Step 9: Display the processing stages
titles = [
    "Original Image", "Grayscale",
    "Gaussian Filter", "Canny Edges",
    "Threshold", "Candidate Detection"
]

images = [
    cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
    gray, blurred, edges, threshold,
    cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
]

plt.figure(figsize=(14, 8))

for i, (title, img) in enumerate(zip(titles, images), start=1):
    plt.subplot(2, 3, i)
    plt.imshow(img, cmap="gray" if img.ndim == 2 else None)
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()