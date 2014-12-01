#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/calib3d/calib3d.hpp>

#include <iostream>

#include "tablePicture.h"

using namespace std;
using namespace cv;

void TablePicture::drawCallback(int event, int x, int y, int, void* vParam)
{
    DrawCallbackParam *param = (DrawCallbackParam*)vParam;
    if(event == EVENT_LBUTTONDOWN)
    {
        float tab[2] = {x, y};
        Mat dst = Mat::zeros(1, 1, CV_32FC2);

        perspectiveTransform(Mat(1, 1, CV_32FC2, tab), dst, param->m);
        param->selectedPoint = Point2f(dst.at<float>(0), dst.at<float>(1));
    }
}

void TablePicture::srcCallback(int event, int x, int y, int, void* vParam)
{
    CallbackParam *param = (CallbackParam*)vParam;

    if(event == EVENT_LBUTTONDOWN && !param->srcPointPlaced)
    {
        param->srcPointPlaced = true;
        param->lastSrcPoint = Point2f(x, y);
    }
}

void TablePicture::dstCallback(int event, int x, int y, int, void* vParam)
{
    CallbackParam *param = (CallbackParam*)vParam;

    if(event == EVENT_LBUTTONDOWN && param->srcPointPlaced)
    {
        param->srcPointPlaced = false;
        param->tablePict->addRefPoint(param->lastSrcPoint, Point2f(x, y));
    }
}

TablePicture::TablePicture(char *path, char *uName)
{
    pict = imread(path);
    name = uName;
    drawParam = NULL;
}

void TablePicture::addRefPoint(Point src, Point dst)
{
    refPointSrc.push_back(src);
    refPointDst.push_back(dst);

    cout << refPointSrc.back() << " to " << refPointDst.back() << endl;
}

void TablePicture::calibrate(Mat table)
{
    char key = 0;
    CallbackParam param;

    param.srcPointPlaced = false;
    param.tablePict = this;

    namedWindow(name);
    setMouseCallback(name, TablePicture::srcCallback, &param);

    namedWindow("Table");
    setMouseCallback("Table", TablePicture::dstCallback, &param);

    while(key != 'n' || refPointSrc.size() < 4)
    {
        imshow(name, pict);
        imshow("Table", table);
        key = waitKey(10);
    }

    setMouseCallback(name, NULL, NULL);
    setMouseCallback("Table", NULL, NULL);
    destroyAllWindows();

    m = findHomography(refPointSrc, refPointDst);
}

void TablePicture::enableDrawMode(void)
{
    drawParam = new DrawCallbackParam;
    drawParam->m = m;

    namedWindow(name);
    imshow(name, pict);
    setMouseCallback(name, TablePicture::drawCallback, drawParam);
}

Point2f TablePicture::getSelectedPoint(void)
{
    if(drawParam != NULL)
    {
        return drawParam->selectedPoint;
    }
    else
    {
        return Point2f(0, 0);
    }
}

TablePicture::~TablePicture(void)
{
    delete drawParam;
}
