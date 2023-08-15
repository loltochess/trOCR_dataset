import os

labels_file_list = ["labels_background.txt", "labels_basic.txt", "labels_blur_1.txt", "labels_blur_2.txt"]

# 원본 레이블 파일 경로
# labels_file_path = "labels.txt"

image_folder_list = ["train_background","train_basic","train_blur_1","train_blur_2e"]

# 원본 이미지 파일 경로
# image_folder = "valid"

no_image_dict = {}

# 레이블 파일 열기
for labels_file_path, image_folder in zip(labels_file_list,image_folder_list):
    with open(labels_file_path, 'r', encoding='utf-8') as labels_file:
        lines = labels_file.readlines()

# 라벨 정보를 반복하며 이미지 파일 이름 변경
    for line in lines:
        line_parts = line.split(" ")
        image_number = line_parts[0][:-4]  # 이미지 번호 추출 (숫자).jpg에서 .jpg 제거
        new_image_name = f"{image_folder}_{image_number}.jpg"  # 새로운 이미지 파일 이름

        original_image_path = os.path.join(image_folder, line_parts[0])
        new_image_path = os.path.join(image_folder, new_image_name)

        # 이미지 파일 이름 변경
        try:
            os.rename(original_image_path, new_image_path)
        except:
            if os.path.isfile(new_image_path): continue
            else:
                no_image_dict[new_image_name]=1
                #os.remove(original_image_path)

print("이미지 파일 이름 변경 완료!")

# 원본 레이블 파일 경로
# labels_file_path = "labels_blur_2.txt"

new_files_list = ["labels_background_renamed.txt", "labels_basic_renamed.txt", "labels_blur_1_renamed.txt", "labels_blur_2_renamed.txt"]

# 변경된 레이블 파일이 저장될 경로
# new_labels_file_path = "labels_blur_2_renamed.txt"

for (labels_file_path,new_labels_file_path) in zip(labels_file_list,new_files_list):
    # 레이블 파일 열기
    with open(labels_file_path, 'r', encoding='utf-8') as labels_file:
        lines = labels_file.readlines()

    # 새로운 레이블 파일 생성 및 기존 레이블 정보를 반복하며 변환하여 저장
    with open(new_labels_file_path, 'w', encoding='utf-8') as new_labels_file:
        for line in lines:
            line_parts = line.split(" ")
            image_number = line_parts[0][:-4]  # 이미지 번호 추출 (숫자).jpg에서 .jpg 제거
            new_image_name = f"{labels_file_path[6:-4]}_{image_number}.jpg"  # 새로운 이미지 파일 이름
            if new_image_name in no_image_dict:
                continue
            new_line = f"{new_image_name} {' '.join(line_parts[1:])}"  # 새로운 라인 생성
            new_labels_file.write(new_line)

print("레이블 파일 변환 및 저장 완료!")