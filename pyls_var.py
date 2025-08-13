import os

def show_extension_stats(directory: str) -> None:
    """
    Print the count and total size of files grouped by extension in the given
    directory.
    """
    files = get_files_in_directory(directory)
    stats = collect_extension_stats(directory, files)
    display_extension_stats(stats)

def get_files_in_directory(directory: str) -> list[str]:
    """Return a list of all non-directory files in the directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_file_extension(filename: str) -> str:
    """Return the file extension or 'NO_EXT' if none."""
    parts = filename.rsplit('.', 1)
    return parts[1].lower() if len(parts) > 1 else "NO_EXT"

def collect_extension_stats(directory: str, files: list[str]) -> dict:
    """
    Build and return a dictionary mapping each file extension to a tuple (count,
    total_size). No use of defaultdict.
    """
    stats = {}
    for f in files:
        ext = get_file_extension(f)
        size = os.path.getsize(os.path.join(directory, f))
        if ext not in stats:
            stats[ext] = (1, size)
        else:
            current_count, current_size = stats[ext]
            stats[ext] = (current_count + 1, current_size + size)
    return stats

def display_extension_stats(stats: dict) -> None:
    """Print the extension, count, and total size for each entry."""
    for ext in sorted(stats):
        count, size = stats[ext]
        print(f".{ext}: {count} files, {size} bytes")

if __name__ == "__main__":
    show_extension_stats(".")
