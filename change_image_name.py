import os

image_folder_list = ['train','valid']

for image_folder in image_folder_list:
    image_folder_path=os.path.join(os.getcwd(),image_folder)
    image_files=os.listdir(image_folder_path)
    for filename in image_files:
        if filename.endswith(".jpg") and filename[0].isdigit():
            # 숫자로 시작하고 .jpg로 끝나는 파일에 대해서만 작업 수행
            file_number = filename.split(".")[0]
            new_filename = f"{image_folder}_blur_2_{file_number}.jpg"
            
            # 파일 이름 변경
            old_path = os.path.join(image_folder_path, filename)
            new_path = os.path.join(image_folder_path, new_filename)
            os.rename(old_path, new_path)
