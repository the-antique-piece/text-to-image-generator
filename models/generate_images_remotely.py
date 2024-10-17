import requests

repo_id = "theantiquepiece/thefalcon"
prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"

url = f"https://huggingface.co/api/inference/v2/models/{repo_id}/generate"
payload = {"inputs": {"prompt": prompt}}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    image_url = data["output"][0]
    image_name = "generated_image.png"

    # Download image
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(image_name, "wb") as image_file:
            image_file.write(image_response.content)
        print(f"Image saved as {image_name}")
    else:
        print("Error downloading image")
        print(image_response.text)
else:
    print("Error generating image")
    print(response.text)