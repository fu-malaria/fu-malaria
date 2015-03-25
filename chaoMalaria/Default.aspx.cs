using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using System.Drawing;
using Emgu.CV;
using Emgu.Util;
using Emgu.CV.UI;
using Emgu.CV.Structure;
using Emgu.CV.CvEnum;

namespace chaoMalaria
{
    public partial class _Default : Page
    {
        public string DefaultFileName = "Upload/";
        public string DefaultFileName2 = "Processed/";
        public string DefaultFileName3 = "Processed2/";

        protected void Page_Load(object sender, EventArgs e)
        {
            
        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            if (FileUploader.HasFile)
                try
                {
                    FileUploader.SaveAs(Server.MapPath(DefaultFileName) + FileUploader.FileName);
                    
                    Image<Bgr, Byte> originalImage = new Image<Bgr, byte>(Server.MapPath(DefaultFileName) + FileUploader.FileName);
                    int width, height, channels = 0;
                    width = originalImage.Width;
                    height = originalImage.Height;
                    channels = originalImage.NumberOfChannels;

                    Image<Bgr, byte> colorImage = new Image<Bgr, byte>(originalImage.ToBitmap());
                    Image<Gray, byte> grayImage = colorImage.Convert<Gray, Byte>();

                    float[] GrayHist;
                    DenseHistogram Histo = new DenseHistogram(255, new RangeF(0, 255));
                    Histo.Calculate(new Image<Gray, Byte>[] { grayImage }, true, null);
                    GrayHist = new float[256];
                    Histo.MatND.ManagedArray.CopyTo(GrayHist, 0);
                    float largestHist = GrayHist[0];
                    int thresholdHist = 0;
                    for (int i = 0; i < 255; i++)
                    {
                        if (GrayHist[i] > largestHist)
                        {
                            largestHist = GrayHist[i];
                            thresholdHist = i;
                        }
                    }

                    grayImage = grayImage.ThresholdAdaptive(new Gray(255), ADAPTIVE_THRESHOLD_TYPE.CV_ADAPTIVE_THRESH_MEAN_C, THRESH.CV_THRESH_BINARY, 85, new Gray(4));
                    colorImage = colorImage.Copy();
                    int countRedCells = 0;
                    using (MemStorage storage = new MemStorage())
                    {
                        for (Contour<Point> contours = grayImage.FindContours(Emgu.CV.CvEnum.CHAIN_APPROX_METHOD.CV_CHAIN_APPROX_SIMPLE, Emgu.CV.CvEnum.RETR_TYPE.CV_RETR_LIST, storage); contours != null; contours = contours.HNext)
                        {
                            Contour<Point> currentContour = contours.ApproxPoly(contours.Perimeter * 0.015, storage);
                            if (currentContour.BoundingRectangle.Width > 20)
                            {
                                CvInvoke.cvDrawContours(colorImage, contours, new MCvScalar(0, 0, 255), new MCvScalar(0, 0, 255), -1, 2, Emgu.CV.CvEnum.LINE_TYPE.EIGHT_CONNECTED, new Point(0, 0));
                                colorImage.Draw(currentContour.BoundingRectangle, new Bgr(0, 255, 0), 1);
                                countRedCells++;
                            }
                        }
                    }

                    Image<Gray, byte> grayImageCopy2 = originalImage.Convert<Gray, Byte>();
                    grayImageCopy2 = grayImageCopy2.ThresholdBinary(new Gray(100), new Gray(255));
                    colorImage = colorImage.Copy();
                    int countMalaria = 0;
                    using (MemStorage storage = new MemStorage())
                    {
                        for (Contour<Point> contours = grayImageCopy2.FindContours(Emgu.CV.CvEnum.CHAIN_APPROX_METHOD.CV_CHAIN_APPROX_SIMPLE, Emgu.CV.CvEnum.RETR_TYPE.CV_RETR_TREE, storage); contours != null; contours = contours.HNext)
                        {
                            Contour<Point> currentContour = contours.ApproxPoly(contours.Perimeter * 0.015, storage);
                            if (currentContour.BoundingRectangle.Width > 20)
                            {
                                CvInvoke.cvDrawContours(colorImage, contours, new MCvScalar(255, 0, 0), new MCvScalar(255, 0, 0), -1, 2, Emgu.CV.CvEnum.LINE_TYPE.EIGHT_CONNECTED, new Point(0, 0));
                                colorImage.Draw(currentContour.BoundingRectangle, new Bgr(0, 255, 0), 1);
                                countMalaria++;
                            }
                        }
                    }

                    colorImage.Save(Server.MapPath(DefaultFileName2) + FileUploader.FileName);

                    inputDiv.Attributes["style"] = "display: block; margin-left: auto; margin-right: auto";
                    outputDiv.Attributes["style"] = "display: block; margin-left: auto; margin-right: auto";
                    Image1.ImageUrl = this.ResolveUrl(DefaultFileName + FileUploader.FileName);
                    Image2.ImageUrl = this.ResolveUrl(DefaultFileName2 + FileUploader.FileName);
                    Chart1.DataBindTable(GrayHist);
                    Label1.Text = "Uploaded Successfully";
                    Label2.Text = "File name: " +
                        FileUploader.PostedFile.FileName + "<br>" + "File Size: " +
                        FileUploader.PostedFile.ContentLength + " kb<br>" + "Content type: " + FileUploader.PostedFile.ContentType + "<br>"
                        + "Resolution: " + width.ToString() + "x" + height.ToString() + "<br>"
                        + "Number of channels: " + channels.ToString() + "<br>"
                        + "Histogram (maximum value): " + largestHist + " @ " + thresholdHist;

                    LabelRed.Text = countRedCells.ToString();
                    LabelMalaria.Text = countMalaria.ToString();
                }
                catch (Exception ex)
                {
                    Label1.Text = "ERROR: " + ex.Message.ToString();
                    Label2.Text = "";
                }
            else
            {
                Label1.Text = "You have not specified a file.";
                Label2.Text = "";
            }

        }

        protected void LoginButton_Click(object sender, EventArgs e)
        {
            if (PasswordTextBox.Text == "h88mnjlx")
            {
                MainDiv.Visible = true;
                LoginDiv.Visible = false;
            }
        }
    }
}