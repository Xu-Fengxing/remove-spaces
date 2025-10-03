import os

def main():
    folder = os.path.dirname(os.path.abspath(__file__))

    for name in os.listdir(folder):
        old_path = os.path.join(folder, name)

        # 跳过文件夹和脚本自身
        if not os.path.isfile(old_path) or name == os.path.basename(__file__):
            continue

        new_name = name.replace(" ", "")
        if new_name != name:
            new_path = os.path.join(folder, new_name)
            # 避免覆盖
            if os.path.exists(new_path):
                base, ext = os.path.splitext(new_name)
                i = 1
                while os.path.exists(os.path.join(folder, f"{base}_{i}{ext}")):
                    i += 1
                new_path = os.path.join(folder, f"{base}_{i}{ext}")
            os.rename(old_path, new_path)
            print(f"{name} -> {os.path.basename(new_path)}")

    input("\n处理完成，按回车退出...")

if __name__ == "__main__":
    main()