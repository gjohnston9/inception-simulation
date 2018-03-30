import java.io.File;
import java.util.HashMap;
import javafx.scene.layout.Pane;
import javafx.scene.control.Label;
import java.util.Scanner;
import javafx.scene.canvas.Canvas;
import java.util.ArrayList;
import javafx.scene.canvas.GraphicsContext;
import java.util.Arrays;
import javafx.scene.image.PixelWriter;
public class Tab
{
	private ArrayList<TimeSlice> timeSlices = new ArrayList<>();
	private long time;
	private File f;
	private Label timestamplabel;
	private Pane chart;
	private Pane base;
	private int index = -1;
	public HashMap<String, Double> inputs = new HashMap<>();
	public HashMap<String, Double> outputs = new HashMap<>();
	private Canvas timechart;
	public Tab(File f)
	{
		
		timestamplabel = Style.formatLabel("Time: 0", Globals.nameLabelWidth, 0, Globals.timeStampWidth, Globals.statusBarHeight);
		this.time = System.currentTimeMillis();
		chart = new Pane();
		chart.setLayoutY(Globals.tabHeight);
		chart.setPrefHeight(Globals.gridHeight);
		chart.setMaxHeight(Globals.gridHeight);
		chart.setMinHeight(Globals.gridHeight);
		chart.setPrefWidth(Globals.gridWidth);
		chart.setMaxWidth(Globals.gridWidth);
		chart.setMinWidth(Globals.gridWidth);
		base = new Pane();
		base.setPrefHeight(Globals.gridHeight);
		base.setMaxHeight(Globals.gridHeight);
		base.setMinHeight(Globals.gridHeight);
		base.setPrefWidth(Globals.gridWidth);
		base.setMaxWidth(Globals.gridWidth);
		base.setMinWidth(Globals.gridWidth);
		timechart = new Canvas(Globals.timeChartWidth, Globals.timeChartHeight);
		timechart.setLayoutX(Globals.gridWidth);
		timechart.setLayoutY(0);
		timechart.setOnMousePressed((tp)->
		{
			int oldindex = index;
			index = (int)(tp.getY()*timeSlices.size() / Globals.timeChartHeight);
			if(index!=oldindex)
				paint();
		});
		timechart.setOnMouseDragged((tp)->
		{
			int oldindex = index;
			index = (int)(tp.getY()*timeSlices.size() / Globals.timeChartHeight);
			if(index!=oldindex)
				paint();
		});
		this.f = f;
		update();
	}
	public Pane createPane()
	{
		Pane pane = new Pane();
		pane.getChildren().add(Style.formatLabel(f.getPath(), 0, 0, Globals.nameLabelWidth, Globals.statusBarHeight));
		pane.getChildren().add(timestamplabel);
		pane.getChildren().add(chart);
		pane.getChildren().add(timechart);
		pane.getChildren().add(Style.formatButton("< Previous",Globals.gridWidth, Globals.timeChartHeight, Globals.nextPrevButtonWidth, Globals.nextPrevButtonHeight, ()->
		{
			index = (index + timeSlices.size() - 1)%timeSlices.size(); 
			paint();
		}));
		pane.getChildren().add(Style.formatButton("Next >",Globals.gridWidth+Globals.nextPrevButtonWidth, Globals.timeChartHeight, Globals.nextPrevButtonWidth, Globals.nextPrevButtonHeight, ()->
		{
			index = (index + 1)%timeSlices.size();
			paint();
		}));
		return pane;
	}
	public long getTimeRead()
	{
		return time;
	}
	public void paint()
	{
		TimeSlice t = timeSlices.get(Math.min(index, timeSlices.size()-1));
		chart.getChildren().clear();
		chart.getChildren().add(base);
		t.applyTo(chart);
		timestamplabel.setText("Time: "+t.timestamp);
 		GraphicsContext gc = timechart.getGraphicsContext2D();
// 		gc.setFill(Globals.toColor(Globals.maxColor));
// 			gc.fillRect(0,0,Globals.timeChartWidth, Globals.timeChartHeight);
		PixelWriter pw = timechart.getGraphicsContext2D().getPixelWriter();
		for(int i = 0; i < Globals.timeChartHeight; i++)
		{
			TimeSlice ts = timeSlices.get((int)(i*timeSlices.size()/Globals.timeChartHeight));
			double[] people = new double[ts.people.size()];
			for(int j = 0; j < people.length; j++)
			{
				people[j] = ts.people.get(j).v;
			}
			Arrays.sort(people);
			for(int j = 0; j < Globals.timeChartWidth; j++)
			{
				double d = people[(int)(j*people.length*1.0/Globals.timeChartWidth)];
				int[] igrs = Globals.getColor(d);
				pw.setColor(j, i, Globals.toColor(igrs));
			}

// 			double x = ts.percentl*Globals.timeChartWidth;
// 			gc.setFill(Globals.toColor(Globals.minColor));
// 			gc.fillRect(0,i,x, 1);
// 			gc.setFill(Globals.toColor(Globals.getColor(0.5)));
// 			gc.fillRect(x,i,ts.percentc*Globals.timeChartWidth, 3);
		}
		gc.setFill(Globals.toColor(0, 0, 0));
		gc.fillRect(0,(int)((0.5+index)*Globals.timeChartHeight/timeSlices.size())-1,Globals.timeChartWidth, 3);
	}
	public void update()
	{
		try
		{
			inputs = new HashMap<>();
			outputs = new HashMap<>();
			this.time = System.currentTimeMillis();
			if(index == timeSlices.size() - 1)
				index = -1;
			Scanner scan = new Scanner(f);
			String s = null;
			while(!(s=scan.nextLine()).equals("speakers"))
			{
				String[] parts = s.replaceAll("_"," ").split(":");
				inputs.put(parts[0], Double.parseDouble(parts[1]));
			}
			double width = inputs.get("width");
			double height = inputs.get("height");
			double cellwidth = Globals.gridWidth / width;
			double cellheight = Globals.gridHeight / height;
			double halfpad = Globals.gridPadding / 2.0;
			base.getChildren().clear();
			if(width*height > Globals.cellCutoff)
			{
				base.getChildren().add(Style.formatLabel("Graph too large to display", 0, 0, Globals.gridWidth, Globals.gridHeight));
			}
			else for(int i = 0; i < width; i++)
			{
				for(int j = 0; j < height; j++)
				{
					base.getChildren().add(Style.formatRectangle(halfpad + cellwidth*i, halfpad + cellheight*j, cellwidth-Globals.gridPadding, cellheight-Globals.gridPadding, Globals.toColor(Globals.cellFillColor)));
				}
			}
			while(!(s=scan.nextLine()).equals("begin"))
			{
				String[] parts = s.substring(1, s.length()-1).split(",");
				int x = Integer.parseInt(parts[0]);
				int y = Integer.parseInt(parts[1]);
				double c = Double.parseDouble(parts[2]);
				base.getChildren().add(Style.formatCircle(Globals.gridPadding + cellwidth*x, Globals.gridPadding + cellheight*y, cellwidth-Globals.gridPadding*2, cellheight-Globals.gridPadding*2,
					Globals.toColor(Globals.getColor(c)), true));
			}
			timeSlices = new ArrayList<>();
			try
			{
				while(!(s=scan.nextLine()).equals("end"))
				{
					timeSlices.add(new TimeSlice(s, cellwidth, cellheight));
				}
				while(scan.hasNextLine())
				{
					String[] parts = scan.nextLine().replaceAll("_"," ").split(":");
					outputs.put(parts[0], Double.parseDouble(parts[1]));
				}
			}
			catch(Exception e)
			{
			}
			if(index == -1)
				index = timeSlices.size() - 1;
			paint();
		}
		catch(Exception e)
		{
			throw new IllegalArgumentException(e);
		}
	}
}
