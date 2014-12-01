#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/calib3d/calib3d.hpp>

#include <iostream>

using namespace std;
using namespace cv;

struct CallbackParam
{
    Mat *table;
    Mat tableOriginal;
    Mat M;
};

static void drawCircleProj(int event, int x, int y, int, void* vParam)
{
    if(event == EVENT_MOUSEMOVE)
    {
        CallbackParam *param = (CallbackParam*)vParam;
        float tab[2] = {x, y};
        Mat dst = Mat::zeros(1, 1, CV_32FC2);

        perspectiveTransform(Mat(1, 1, CV_32FC2, tab), dst, param->M);
        *(param->table) = param->tableOriginal.clone();
        circle(*(param->table), Point2f(dst.at<float>(0), dst.at<float>(1)), 4, Scalar(0, 0, 255), 2);
    }
}

int main(int argc, char *argv[])
{
    Mat img, table;
    img = imread("table_small.JPG", CV_LOAD_IMAGE_COLOR);
    table = imread("schema_table.png", CV_LOAD_IMAGE_COLOR);

    namedWindow("Table");

    float src_pts[][2] = {{142,96}, {588,87},{125,290},{232,143}};
    Mat mat_src_pts(4, 2, CV_32F, src_pts);
    float dst_pts[][2] = {{0,0}, {418,0},{121,424},{121,202}};
    Mat mat_dst_pts(4, 2, CV_32F, dst_pts);

    CallbackParam param;
    param.M = findHomography(mat_src_pts, mat_dst_pts, RANSAC, 5.0);
    param.table = &table;
    param.tableOriginal = table.clone();

    setMouseCallback("Table", drawCircleProj, &param);

    bool quit = false;

    while(!quit)
    {
        imshow("Table", img);
        imshow("Top", table);

        if(waitKey(1) == 'q')
        {
            quit = true;
        }
    }

    return EXIT_SUCCESS;
}
