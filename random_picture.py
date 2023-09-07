import os
import requests
import uuid

def download_random_images(num_images, output_folder):
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    for i in range(num_images):
        try:
            # Generate a unique filename using UUID
            unique_filename = str(uuid.uuid4())
            image_url = f"https://source.unsplash.com/random/{unique_filename}"
            response = requests.get(image_url)

            if response.status_code == 200:
                
                # Save the image to the output folder
                image_path = os.path.join(output_folder, f"{unique_filename}.jpg")
                
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                    
                print(f"Downloaded image {i + 1}/{num_images}: {image_url}")
                
        except Exception as e:
            print(f"Error downloading image {i + 1}/{num_images}: {str(e)}")
            
    print("--- Download Done ---")

if __name__ == "__main__":
    num_images = int(input("Enter the number of random images to download: "))
    output_folder = input("Enter the folder where you want to save the images: ")

    download_random_images(num_images, output_folder)
