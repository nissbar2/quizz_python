# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



    # Replace 'your_image_path.jpg' with the path to your image file
    # image_path = 'newrender.png'
    #
    # pixel_picker = PixelPicker(image_path)
    # plt.show()
import requests
from bs4 import BeautifulSoup


def print_container_labels(container):
    # Find the heading within the container
    container_head = container.find('h2')
    print(container_head.text)

    # Find all links within the container
    container_links = container.find_all('a')

    # Extract and print the labels of each link within the container
    for link in container_links:
        label = link.get_text(strip=True)
        if label:
            link_url = link.get('href')
            print(label)
            print('https://www.kolzchut.org.il' + link_url)

            # Make a request to the link URL
            response_ = requests.get('https://www.kolzchut.org.il' + link_url)

            # Check if the request was successful (status code 200)
            if response_.status_code == 200:
                soup = BeautifulSoup(response_.text, 'html.parser')

                # Find and print labels in nested containers
                nested_containers = soup.find_all('div', class_='portal-box')
                for nested_container in nested_containers:
                    print_container_labels(nested_container)
                    print('/n')

if __name__ == "__main__":

# Replace 'https://example.wikipedia.org' with the actual URL of the Wikimedia website you want to scrape
    url = 'https://www.kolzchut.org.il/he/סטודנטים'

# Send a GET request to the URL
    response = requests.get(url)

# Check if the request was successful (status code 200)
    if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

    # Find all containers on the page (replace with the actual class or tag of your containers)
    containers = soup.find_all('div', class_='portal-box')

    # Iterate over each container and print the labels of links within each container
    for container in containers:
        print_container_labels(container)
        print('/n')

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Additional commented-out code:
# ...
