#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

// TASK2：将彩色图片转换成灰度图（C++ 版本）
int main() {
    Mat img = imread("input.png");
    if (img.empty()) {
        cout << "图片读取失败，请检查 input.png" << endl;
        return -1;
    }

    // 彩色转灰度：BGR 三通道合并成单通道灰度图
    Mat gray;
    cvtColor(img, gray, COLOR_BGR2GRAY);

    imwrite("gray_cpp.png", gray);

    imshow("original", img);
    imshow("gray", gray);
    waitKey(0);
    destroyAllWindows();

    cout << "灰度图已保存为 gray_cpp.png" << endl;
    return 0;
}
