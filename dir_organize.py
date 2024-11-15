import os
import shutil

def move_file(source_file_path,target_folder,file):    
    file_extension = os.path.splitext(file)[1] 
    
    # Create target folder if it doesn't exist
    target_folder_path = os.path.join(target_folder, file_extension[1:].upper())
    os.makedirs(target_folder_path, exist_ok=True)
    
    target_file = os.path.join(target_folder_path,file)
    if os.path.exists(target_file):
        # Handle existing file, e.g., rename or skip
        print(f"File already exists at {target_file}. Skipping...")
    else:
        shutil.move(source_file_path, target_folder_path)


def sort_files(source_folder, target_folder):
    """
    Sorts files within a source folder into target folders based on their file extension.

    Args:
        source_folder (str): Path to the source folder.
        target_folder (str): Path to the target folder.
    """
    file_counter = 0

    print(f'Start checking source folder: {source_folder}')
    print(f'This could take some time, please wait...')
    for file in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file)
        
        # Check if the current path is a directory
        if os.path.isdir(source_path):
            for sub_file in os.listdir(source_path):
                source_file_path = os.path.join(source_path, sub_file)           
                
                # Move file to the appropriate target folder
                move_file(source_file_path,target_folder,sub_file)
                file_counter+=1

        else:
            source_file_path = os.path.join(source_folder, file)
            
            # Move file to the appropriate target folder
            move_file(source_file_path,target_folder,file)
            file_counter+=1
        
    print('Files organization completed.')
    print(f'Total files moved: {file_counter}')

            




if __name__ == "__main__":
    source_folder = "/media/hartmmy/B876BC7F76BC3FC4/recup_dir/"
    target_folder = "/media/hartmmy/B876BC7F76BC3FC4/Datos Maricela/"

    sort_files(source_folder, target_folder)
