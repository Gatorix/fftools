import subprocess
import os


def get_all_filepath(folder, filetype):
    file_path = []
    try:
        for fpathe, dirs, fs in os.walk(folder):
            for f in fs:
                if '.DS_Store' in os.path.join(fpathe, f):
                    pass
                elif os.path.join(fpathe, f)[-4:] != filetype:
                    pass
                else:
                    file_path.append(os.path.join(fpathe, f))
    except TypeError as e:
        print('路径输入错误，检查后重新输入！')

    file_path.sort()

    return file_path


videos = get_all_filepath('/Users/caosheng/Downloads', '.mp4')
subtitles = get_all_filepath('/Users/caosheng/Downloads', '.ass')



def mainloop(lib='libx265', preset=4, crf=24):
    if len(videos) != len(subtitles):
        print('指定文件夹中的视频文件数量和字幕文件数量不一致')
    else:
        for i in range(len(videos)):

            cmd = 'ffmpeg -i %s -c:v %s -preset %s -crf %s -vf ass=%s %s' % (
                videos[i], lib, preset, crf, subtitles[i], videos[i][:videos[i].rfind('.')]+'.h265'+videos[i][videos[i].rfind('.'):])

            sub = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

            print(sub.stdout.read())

if __name__ =='__main__':
    mainloop()