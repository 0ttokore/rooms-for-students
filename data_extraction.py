import requests


def data_extraction_from_git_hub(file_url, save_as):
    raw_url = file_url.replace("github.com", "raw.githubusercontent.com").replace(
        "/blob/", "/"
    )
    response = requests.get(raw_url)

    if response.status_code == 200:
        with open(save_as, "wb") as f:
            f.write(response.content)
        print(f"File saved as {save_as}.")
    else:
        print(f"Error {response.status_code}: Failed to upload file.")
