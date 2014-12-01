#ifndef TABLE_PICTURE_H
#define TABLE_PICTURE_H

class TablePicture;

struct CallbackParam
{
    bool srcPointPlaced;
    TablePicture *tablePict;
    cv::Point lastSrcPoint;
};

struct DrawCallbackParam
{
    cv::Mat m;
    cv::Point2f selectedPoint;
};


class TablePicture
{
public:
    TablePicture(char *path, char *uName);
    void calibrate(cv::Mat table);
    void addRefPoint(cv::Point src, cv::Point dst);
    void enableDrawMode(void);
    cv::Mat getMatrix(void);
    static void srcCallback(int event, int x, int y, int, void* vParam);
    static void dstCallback(int event, int x, int y, int, void* vParam);
    static void drawCallback(int event, int x, int y, int, void* vParam);
    cv::Point2f getSelectedPoint(void);
    ~TablePicture(void);

private :
    char* name;
    cv::Mat pict;
    std::vector<cv::Point2f> refPointSrc;
    std::vector<cv::Point2f> refPointDst;
    cv::Mat m;
    DrawCallbackParam *drawParam;
};

#endif
