#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/calib3d/calib3d.hpp>

#include <iostream>

#include "tablePicture.h"

#define NB_PICT 3

using namespace std;
using namespace cv;

void drawCircles(Point2f points[NB_PICT], Mat *table, Mat tableOriginal)
{
    Point2f bary(0, 0);

    Scalar colors[NB_PICT] = {Scalar(255, 0, 0), Scalar(0, 255, 0), Scalar(0, 0, 255)};
    *table = tableOriginal.clone();
    for(int i = 0 ; i < NB_PICT ; i++)
    {
        circle(*table, points[i], 4, colors[i], 2);
        bary += points[i];
    }
    bary = Point2f(bary.x/3, bary.y/3);

    circle(*table, bary, 4, Scalar(255, 255, 255), 2);

}


int main(int argc, char *argv[])
{
    TablePicture tablePict[3] = {TablePicture("tablePict1.JPG", "TablePict1"),
                                 TablePicture("tablePict2.JPG", "TablePict2"),
                                 TablePicture("tablePict3.JPG", "TablePict3")};
    Mat table = imread("schema_table.png");
    Mat tableOriginal = table.clone();

    for(int i = 0 ; i < 3 ; i++)
        tablePict[i].calibrate(table);

    for(int i = 0 ; i < 3; i++)
        tablePict[i].enableDrawMode();

    bool quit = false;

    while(!quit)
    {
        Point2f points[NB_PICT];
        for(int i = 0 ; i < NB_PICT ; i++)
        {
            points[i] = tablePict[i].getSelectedPoint();
        }
        drawCircles(points, &table, tableOriginal);
        imshow("Table", table);

        if(waitKey(1) == 'q')
        {
            quit = true;
        }
    }


    return EXIT_SUCCESS;
}

