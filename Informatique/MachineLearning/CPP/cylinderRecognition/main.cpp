#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#define W_CONTOUR_MIN 10
#define H_CONTOUR_MIN 10

using namespace std;
using namespace cv;

enum{MATCHMIN, HMIN, HMAX, SMIN, SMAX, VMIN, VMAX};


int main(int argc, char *argv[])
{
    Mat cross = getStructuringElement(MORPH_CROSS, Size(6, 6));
    namedWindow("Cylinder detection");
    namedWindow("Trackbars Colors");
    namedWindow("Match max");
    Mat img = imread("DSC00379.JPG");

    int trackbars[8] = {createTrackbar("Max", "Match max", NULL, 1000),
                        createTrackbar("Hmin", "Trackbars Colors", NULL, 180),
                        createTrackbar("Hmax", "Trackbars Colors", NULL, 180),
                        createTrackbar("Smin", "Trackbars Colors", NULL, 255),
                        createTrackbar("Smax", "Trackbars Colors", NULL, 255),
                        createTrackbar("Vmin", "Trackbars Colors", NULL, 255),
                        createTrackbar("Vmax", "Trackbars Colors", NULL, 255)};

    Mat cylinderRef = imread("cylinderReference.png");
    cvtColor(cylinderRef, cylinderRef, CV_BGR2GRAY);



    vector<vector<Point> > cylinderContours;
    vector<Vec4i> cylinderHierarchy;


    findContours(cylinderRef, cylinderContours, cylinderHierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));



    while(waitKey(10) != 'q')
    {
        int HSVmin[3] = {getTrackbarPos("Hmin", "Trackbars Colors"),
                           getTrackbarPos("Smin", "Trackbars Colors"),
                           getTrackbarPos("Vmin", "Trackbars Colors")};

        int HSVmax[3] = {getTrackbarPos("Hmax", "Trackbars Colors"),
                           getTrackbarPos("Smax", "Trackbars Colors"),
                           getTrackbarPos("Vmax", "Trackbars Colors")};

        vector<vector<Point> > contours;
        vector<Vec4i> hierarchy;

        Mat cropped = Mat::zeros(img.size(), CV_8UC1);
        inRange(img, vector<int>(HSVmin, HSVmin + 3), vector<int>(HSVmax, HSVmax + 3), cropped);
        erode(cropped, cropped, cross);
        dilate(cropped, cropped, cross);

        Mat contoursSupport = cropped.clone();

        findContours(contoursSupport, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));

        Mat drawing = Mat::zeros(img.size(), CV_8UC3);

        float matchMax = ((float)getTrackbarPos("Max", "Match max"))/100;

        for(int i = 0 ; i< contours.size() ; i++)
        {
            Rect rect = boundingRect(contours[i]);
            if(matchShapes(contours[i], cylinderContours[0], 1, 1) < matchMax && rect.width >= W_CONTOUR_MIN && rect.height >= H_CONTOUR_MIN)
            {
                drawContours(drawing, contours, i, Scalar(0, 0, 255), 1, 8, vector<Vec4i>(), 0, Point());
            }
        }

        imshow("Cylinder detection", cropped);
        imshow("Contours", drawing);
    }

    return EXIT_SUCCESS;
}
