﻿#ifndef SHOWWID_H
#define SHOWWID_H

#include <QWidget>
#include <QAction>
#include <QMenu>
#include <QContextMenuEvent>
#include <QImage>
#include <QPoint>

#define STEP_GRAYSCALE      1   //灰度化
#define STEP_UNGRAYSCALE    2   //去灰度化
#define STEP_DENOISE        3   //去噪
#define STEP_SHARPE         4   //锐化
#define STEP_ROTATE_RIGHT   5   //向右旋转
#define STEP_ROTATE_LEFT    6   //向左旋转

enum MousePressStatus { Left, Mid, Right, No };

class ShowWid : public QWidget
{
    Q_OBJECT

public:
    ShowWid(QWidget *parent = Q_NULLPTR);
    ~ShowWid();

    bool Init();    //初始化

    void OpenImage(QString strImagePath);   //打开图片
    void CloseImage();                      //关闭图片

    void OnSaveAs();                        //另存为
signals:
    void SigMessage(QString strMessage);
private slots:
    void on_actSharpen_triggered();                 //锐化
    void on_actDenoise_triggered();                 //去噪
    void on_actGrayscale_triggered();               //灰度化
    void On_menuRotate_triggered(QAction *act);     //旋转
    void On_menuMirrored_triggered(QAction *act);   //镜像
    void On_actPosRestore_triggered();              //位置还原
private:
    void paintEvent(QPaintEvent *event);            //绘制事件

    void contextMenuEvent(QContextMenuEvent *event);    //右键菜单

    void wheelEvent(QWheelEvent *e);                //滚轮事件
    void mouseMoveEvent(QMouseEvent * e);           //鼠标移动
    void mousePressEvent(QMouseEvent * e);          //鼠标点击
    void mouseDoubleClickEvent(QMouseEvent *e);     //鼠标双击

    QImage GetShowImage();                          //由原始图像变换为显示图像


private:

    QPixmap m_pixBase;          //原始图像
    QPixmap m_pixShow;          //效果显示图像

    QString m_strImagePath;     //图片路径
    QImage m_stImage;           //原始图像


    // 菜单功能
    QMenu m_menuMouse;          //鼠标右键菜单
    QAction m_actSharpen;       //锐化
    QAction m_actDenoise;       //去噪
    QAction m_actGrayscale;     //灰度化
    QAction m_actRotateMenu;    //旋转菜单
    QMenu m_menuRotate;         //旋转
    QAction m_actRotateRight;   //向右旋转
    QAction m_actRotateLeft;    //向左旋转
    QAction m_actMirroredMenu;  //镜像菜单
    QMenu m_menuMirrored;       //镜像
    QAction m_actMirroredHorizontal;    //水平镜像
    QAction m_actMirroredVertical;      //垂直镜像
    QAction m_actPosRestore;    //位置还原

    QList<int> m_listStepHistory;       //历史操作步骤

    // 图像状态
    float m_fScale;         //缩放比例
    int xtranslate;         //图像坐标
    int ytranslate;         //图像坐标
     
    int m_nRotateDegrees;       //旋转角度
    bool m_bGrayscale;          //灰度标志

    bool m_bMirroredHorizontal; //水平镜像标志
    bool m_bMirroredVertical;   //垂直镜像标志

    //鼠标状态
    MousePressStatus m_eMousePressStatus;
    QPoint m_stMousePressPos;
    QPoint m_stImageShowPos;
    QPoint m_stImageBeforeMovePos;
};

#endif // SHOWWID_H