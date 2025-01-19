import os
import shutil

base_path = os.path.dirname(os.path.realpath(__file__))


def update_windows_updater():
    top_path = os.path.dirname(base_path)

    # Define paths
    updater_path = os.path.join(base_path, ".ci/update_windows/update.py")
    bat_path = os.path.join(base_path, ".ci/update_windows/update_comfyui.bat")
    dest_updater_path = os.path.join(top_path, "update/update.py")
    dest_bat_path = os.path.join(top_path, "update/update_comfyui.bat")
    dest_bat_deps_path = os.path.join(
        top_path, "update/update_comfyui_and_python_dependencies.bat")

    expected_start = b"..\\python_embeded\\python.exe .\\update.py"

    try:
        # Check if the destination batch file needs updating
        with open(dest_bat_path, 'rb') as f:
            if not f.read().startswith(expected_start):
                shutil.copy(updater_path, dest_updater_path)

                # Update dependencies batch file
                update_dependencies(dest_bat_deps_path)

                # Copy the main batch file
                shutil.copy(bat_path, dest_bat_path)
                print("Updated the windows standalone package updater.")  # noqa: T201

    except (FileNotFoundError, IOError) as e:
        print(f"An error occurred: {e}")


def update_dependencies(dest_bat_deps_path):
    """Update the dependencies batch file."""
    try:
        with open(dest_bat_deps_path, 'rb+') as f:
            contents = f.read()
            updated_contents = contents.replace(
                b'..\\python_embeded\\python.exe .\\update.py ..\\ComfyUI\\',
                b'call update_comfyui.bat nopause'
            )
            f.seek(0)  # Move cursor to the beginning of the file
            f.write(updated_contents)
            f.truncate()  # Truncate the file to the new size
    except (FileNotFoundError, IOError) as e:
        print(f"An error occurred while updating dependencies: {e}")
