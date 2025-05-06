import kagglehub

# Download latest version
path = kagglehub.dataset_download("filas1212/cyberpunk-2077-steam-reviews-as-of-aug-8-2024")

print("Path to dataset files:", path)