from PIL import Image
from os import path, listdir

saved_image_name = "! illusion image.png"


def print_size(image):
    return f"(size: {image.size[0]} x {image.size[1]})"


def make_photo(images, final_path):  # Creates the optical illusion image
    # Check the images are all the same size
    for i in range(1, len(images)):
        if images[0].size != images[i].size:
            print("Please make sure the images are same size")
            print(f"Image number {i + 1} {print_size(images[i])} is different size than the first image {print_size(images[0])}")
            return

    pixels = []
    for i in range(len(images)):
        pixels.append(images[i].load())

    # Overwrite the first image, make strips in it. Then save it as a new image
    image_index = 0
    for x in range(int(images[0].size[0])):
        # Fill out the strip
        for y in range(int(images[0].size[1])):
            pixels[0][x, y] = pixels[image_index][x, y]

        # Increment image_index
        image_index += 1
        if image_index >= len(images):
            image_index -= len(images)

    # Save the image
    images[0].save(final_path)
    print("Made an image from " + str(len(images)) + " images")
    print("Image saved at " + str(final_path))


def get_user_data():
    answer = input("Do you want to see the instructions? (yes, no) ")
    if answer.lower() != "no":
        print("\nInstructions:")
        print("Create a folder that holds the images you want to use. Make sure they all are the same size")
        print("Then run this program, say 'no' and then type the location of that folder")
        print("The new image will be created in that same folder.")
        print("The animation order of the images is top down in the folder, so make sure they are in the correct order")
        print("\nNote:")
        print("The amount of images usually depends on the paper with the strips")
        print("Remember to print the image in the correct size. Otherwise it won't work")
        return

    folder_path = input("Please provide the folder path: ")

    # If inputs nonsense
    if not path.exists(folder_path):
        print("Please input a valid path")
        return

    # If it isn't a directory
    if not path.isdir(folder_path):
        print("Please input a directory")
        return

    # Create a tuple with the paths
    paths = listdir(folder_path)

    # Remove the final image from the list if it exists
    for i in range(len(paths)):
        if path.basename(paths[i]) == saved_image_name:
            paths.pop(i)
            break

    try:
        for i in range(len(paths)):
            absolute_path = path.join(folder_path, paths[i])
            if path.isdir(absolute_path):
                print("Please put only images in the folder")
                return
            paths[i] = Image.open(absolute_path)
    except:
        print("Please make sure all the files are images")
        return

    make_photo(paths, path.join(folder_path, saved_image_name))


get_user_data()
