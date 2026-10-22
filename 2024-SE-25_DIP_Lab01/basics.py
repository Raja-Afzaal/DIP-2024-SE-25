# ==========================================
# Exercise 1: Variables and Data Types
# ==========================================
width = 640
height = 480
image_name = "sample.png"
is_color = True

print(f"width: {width}, type: {type(width)}")
print(f"height: {height}, type: {type(height)}")
print(f"image_name: {image_name}, type: {type(image_name)}")
print(f"is_color: {is_color}, type: {type(is_color)}")

total_pixels = width * height
print(f"Total pixels: {total_pixels}")
print("-" * 40)

# ==========================================
# Exercise 2: if, elif, and else
# ==========================================
def classify_pixel(intensity):
    if intensity < 0 or intensity > 255:
        return "Invalid"
    elif intensity >= 128:
        return "Bright pixel"
    else:
        return "Dark pixel"

test_values = [-1, 0, 127, 128, 255, 256]
for val in test_values:
    print(f"Intensity {val}: {classify_pixel(val)}")
    print("-" * 40)

# ==========================================
# Exercise 3: for and while Loops
# ==========================================
# for loop
pixel_list = [20, 130, 255]
print("For loop output:")
for px in pixel_list:
    label = "Bright pixel" if px >= 128 else "Dark pixel"
    print(f"Pixel {px}: {label}")

# while loop
print("\nWhile loop output:")
count = 0
while count < 3:
    print(count)
    count += 1
print("-" * 40)    

# ==========================================
# Exercise 4: Functions
# ==========================================
def is_bright(pixel, threshold=128):
    return pixel >= threshold

print("is_bright(127):", is_bright(127))
print("is_bright(128):", is_bright(128))
print("is_bright(200, 210):", is_bright(200, 210))
print("-" * 40)

# ==========================================
# Exercise 5: Lists and Tuples
# ==========================================
pixels = [0, 128, 255]
print("First item:", pixels[0])

# Replace middle item (index 1) with 150
pixels[1] = 150

# Append 64
pixels.append(64)

print("Updated list:", pixels)
print("List length:", len(pixels))

# Tuple unpacking
size = (640, 480)
width_val, height_val = size
print(f"Unpacked tuple -> Width: {width_val}, Height: {height_val}")

# Note on mutability: Lists are mutable (can be changed after creation), 
# whereas tuples are immutable (cannot be modified after creation).
print("-" * 40)

# ==========================================
# Exercise 6: Dictionaries and Sets
# ==========================================
image = {"width": 640, "height": 480}
image["mode"] = "RGB"

print("Width from dictionary:", image["width"])
print("Mode from dictionary:", image["mode"])

labels_list = ["cat", "dog", "cat", "bird"]
unique_labels = set(labels_list)
print("Unique set:", unique_labels)
print("Number of unique labels:", len(unique_labels))