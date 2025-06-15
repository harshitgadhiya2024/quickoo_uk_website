import requests
import os
from urllib.parse import urlparse


def download_image(url, save_path):
    """
    Download an image from URL and save to specified path

    Args:
        url (str): Image URL
        save_path (str): Local path where image will be saved
    """
    try:
        # Send GET request
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise exception for bad status codes

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Save the image
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Image saved successfully to: {save_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return False


def download_multiple_images(url_list, save_directory):
    """
    Download multiple images from a list of URLs

    Args:
        url_list (list): List of image URLs
        save_directory (str): Directory where images will be saved
    """
    for i, url in enumerate(url_list):
        # Extract filename from URL or create one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename in URL, create one
        if not filename or '.' not in filename:
            filename = f"image_{i + 1}.jpg"

        save_path = os.path.join(save_directory, filename)
        download_image(url, save_path)


# Example usage
if __name__ == "__main__":
    # Single image download
    image_url = "https://images.unsplash.com/photo-1619767886558-efdc259cde1a?q=80&w=12000"
    save_location = "static/images/css2.jpg"
    download_image(image_url, save_location)

    # # Multiple images download
    # urls = [
    #     "https://example.com/image1.jpg",
    #     "https://example.com/image2.png",
    #     "https://example.com/image3.gif"
    # ]
    # download_multiple_images(urls, "downloads/batch/")