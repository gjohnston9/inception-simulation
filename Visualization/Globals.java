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
	public static final double maxIdeology = 100;
	public static final double minIdeology = -100;
	public static final int[] maxColor = {150, 0, 0};
	public static final int[] minColor = {0, 0, 150};
	public static final double graphAxesMenuHeightPercent = 0.1;
	//computed constants
	public static final Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
	public static final double width = screenSize.getWidth();
	public static final double height = screenSize.getHeight();
	public static final double modeHeight = modeHeightPercent*height;
	public static final double tabHeight = tabHeightPercent*height;
	public static final double tabWidth = tabWidthPercent*width;
	public static final double statusBarHeight = statusBarHeightPercent*height;
	public static final double nextPrevButtonHeight = nextPrevButtonHeightPercent*height;
	public static final double gridWidth = gridWidthPercent*width;
	public static final double graphAxesMenuHeight = graphAxesMenuHeightPercent*height;
	//helper methods
	public double[] getColor(double val)
	{
		double a = maxIdeology - val;
		double b = val - minIdeology;
		double total = maxIdeology + minIdeology;
		a /= total;
		b /= total;
		return new double[]{minColor[0]*b + maxColor[0]*a, minColor[1]*b + maxColor[1]*a, minColor[2]*b + maxColor[2]*a};
	}
	public static Color toColor(int[] color)
	{
		return Color.rgb(color[0], color[1], color[2]);
	}
}
