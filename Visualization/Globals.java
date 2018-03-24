import java.awt.Toolkit;
import java.awt.Dimension;
import javafx.scene.paint.Color;
public class Globals
{
	//parameters
	public static String[] directories = {"../Logs"};
	//constants
	public static final double modeHeightPercent = 0.1;
	public static final double tabHeightPercent = 0.1;
	public static final double tabWidthPercent = 0.2;
	public static final double statusBarHeightPercent = 0.1;
	public static final double nextPrevButtonHeightPercent = 0.1;
	public static final double gridWidthPercent = 0.6;
	public static final double gridPadding = 2;
	public static final double maxIdeology = 100;
	public static final double minIdeology = -100;
	public static final int[] maxColor = {150, 0, 0};
	public static final int[] minColor = {0, 0, 150};
	public static final int[] borderColor = {200, 200, 200};
	public static final int[] cellFillColor = {14, 14, 24};
	public static final double graphAxesMenuHeightPercent = 0.1;
	public static final double bufferHeight = 50;
	public static final double nameLabelWidthPercent = 0.5;
	public static final int updateTime = 1000;
	public static final int cellCutoff = 120*120;
	public static final double axisHeightPercent = 0.1;
	public static final double threshold = 0.0000001;
	public static final double chartHeightPercent = 0.7;
	public static final double chartXScalePercent = 0.04;
	public static final double chartYScalePercent = 0.06;
	public static final double chartWidthPercent = 0.85;
	public static final int[] chartBackgroundColor = {14, 14, 24};
	public static final int gridlineWidth = 2;
	public static final int[] chartLineColor = {24, 24, 54};
	public static final int pointDiameter = 11;
	public static final int[] pointColor = {150, 150, 200};
	//computed constants
	public static final Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
	public static final double width = screenSize.getWidth();
	public static final double height = screenSize.getHeight() - bufferHeight;
	public static final double modeHeight = modeHeightPercent*height;
	public static final double tabHeight = tabHeightPercent*height;
	public static final double axisHeight = axisHeightPercent*height;
	public static final double tabWidth = tabWidthPercent*width;
	public static final double statusBarHeight = statusBarHeightPercent*height;
	public static final double nextPrevButtonHeight = nextPrevButtonHeightPercent*height;
	public static final double gridWidth = gridWidthPercent*width;
	public static final double gridHeight = height - (statusBarHeight+tabHeight+modeHeight);
	public static final double timeChartHeight = height - (nextPrevButtonHeight+tabHeight+modeHeight);
	public static final double timeChartWidth = width-gridWidth;
	public static final double nextPrevButtonWidth = timeChartWidth/2;
	public static final double graphAxesMenuHeight = graphAxesMenuHeightPercent*height;
	public static final double contentHeight = height - (modeHeight + tabHeight);
	public static final double nameLabelWidth = nameLabelWidthPercent * width;
	public static final double timeStampWidth = gridWidth - nameLabelWidth;
	public static final double chartHeight = chartHeightPercent*height;
	public static final double chartWidth = chartWidthPercent*width;
	public static final double chartX = width - chartWidth;
	public static final double chartXScale = chartXScalePercent*height;
	public static final double chartXLabelY = chartXScale + chartHeight + graphAxesMenuHeight;
	public static final double chartXLabelHeight = height - (chartXScale + chartHeight + modeHeight + graphAxesMenuHeight);
	public static final double chartYScale = chartYScalePercent*width;
	public static final double chartYLabelHeight = width - (chartYScale + chartWidth);
	//helper methods
	public static int[] getColor(double val)
	{
		double a = maxIdeology - val;
		double b = val - minIdeology;
		double total = a + b;
		a /= total;
		b /= total;
		return new int[]{(int)(minColor[0]*b + maxColor[0]*a), (int)(minColor[1]*b + maxColor[1]*a), (int)(minColor[2]*b + maxColor[2]*a)};
	}
	public static Color toColor(int... color)
	{
		return Color.rgb(color[0], color[1], color[2]);
	}
}
