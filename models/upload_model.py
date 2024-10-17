from huggingface_hub import HfApi
api = HfApi()

api.upload_folder(
    folder_path="/home/thebiglion/Downloads/thefalcon",
    repo_id="theantiquepiece/thefalcon",
    repo_type="model"
)

print("Uploaded")