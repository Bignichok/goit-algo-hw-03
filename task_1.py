import os
import shutil
import argparse

def copy_files_recursively(src_dir, dst_dir):
    try:
        for item in os.listdir(src_dir):
            src_item_path = os.path.join(src_dir, item)
            if os.path.isdir(src_item_path):
                copy_files_recursively(src_item_path, dst_dir)
            else:
                file_extension = os.path.splitext(item)[1][1:]
                extension_dir = os.path.join(dst_dir, file_extension)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)
                dst_item_path = os.path.join(extension_dir, item)
                shutil.copy2(src_item_path, dst_item_path)
                print(f"Copied {src_item_path} to {dst_item_path}")
    except Exception as e:
        print(f"Error while processing {src_item_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension")
    parser.add_argument("src_dir", type=str, help="Source directory path")
    parser.add_argument("dst_dir", type=str, nargs='?', default="dist", help="Destination directory path (default: 'dist')")
    args = parser.parse_args()

    src_dir = os.path.abspath(args.src_dir)
    dst_dir = os.path.abspath(args.dst_dir)

    if not os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist.")
        return

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    copy_files_recursively(src_dir, dst_dir)

if __name__ == "__main__":
    main()
