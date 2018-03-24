import java.io.File;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import javafx.scene.layout.Pane;
import javafx.scene.layout.HBox;
import javafx.scene.control.ComboBox;
import java.util.Arrays;
public class Chart
{
	private HashMap<File, Tab> tabs;
	private Pane outer = new Pane();
	private ComboBox<String> inbox = Style.formatComboBox(Globals.graphAxesMenuHeight, ()->getPane(tabs));
	private ComboBox<String> outbox = Style.formatComboBox(Globals.graphAxesMenuHeight, ()->getPane(tabs));
	private boolean inprogress = false;
	private String in = "";
	private String out = "";
	public Pane getPane(HashMap<File, Tab> tabs)
	{
		outer.requestFocus();
		Pane pane = new Pane();
		if(inprogress)
			return pane;
		inprogress = true;
		this.tabs = tabs;
		in = inbox.getValue();
		out = outbox.getValue();
		HBox hbox = new HBox();
		hbox.getChildren().add(Style.formatLabel("Displaying ", Globals.graphAxesMenuHeight));
		HashSet<String> set = new HashSet<>();
		for(File f : tabs.keySet())
		{
			set.addAll(tabs.get(f).inputs.keySet());
		}
		String[] list = set.toArray(new String[]{});
		Arrays.sort(list);
		inbox.getItems().setAll(list);
		hbox.getChildren().add(inbox);
		hbox.getChildren().add(Style.formatLabel(" versus ", Globals.graphAxesMenuHeight));
		set = new HashSet<>();
		for(File f : tabs.keySet())
		{
			set.addAll(tabs.get(f).outputs.keySet());
		}
		list = set.toArray(new String[]{});
		Arrays.sort(list);
		outbox.getItems().setAll(list);
		hbox.getChildren().add(outbox);
		inbox.setValue(in);
		outbox.setValue(out);
		pane.getChildren().add(hbox);
		if((!"".equals(in)) && in != null && out != null && (!"".equals(out)))
		{
			double minX = Double.MAX_VALUE;
			double maxX = Double.MIN_VALUE;
			double minY = Double.MAX_VALUE;
			double maxY = Double.MIN_VALUE;
			for(File f : tabs.keySet())
			{
				if(tabs.get(f).inputs.containsKey(in))
				{
					minX = Math.min(minX, tabs.get(f).inputs.get(in));
					maxX = Math.max(maxX, tabs.get(f).inputs.get(in));
				}
				if(tabs.get(f).outputs.containsKey(out))
				{
					minY = Math.min(minY, tabs.get(f).outputs.get(out));
					maxY = Math.max(maxY, tabs.get(f).outputs.get(out));
				}
			}
			pane.getChildren().add(Style.formatRectangle(Globals.chartX ,Globals.graphAxesMenuHeight, Globals.chartWidth, 
					Globals.chartHeight, Globals.toColor(Globals.chartBackgroundColor)));
			pane.getChildren().add(Style.formatLabel(in, Globals.chartX ,Globals.chartXLabelY, Globals.chartWidth, 
					Globals.chartXLabelHeight, true));
			pane.getChildren().add(Style.formatLabel(out, 0 ,Globals.graphAxesMenuHeight, Globals.chartYLabelHeight, 
					Globals.chartHeight, true, true));
			for(int i = 0; i < 5; i++)
			{
				pane.getChildren().add(Style.formatRectangle(Globals.chartX ,Globals.graphAxesMenuHeight + (Globals.chartHeight*(i+0.5)/5), Globals.chartWidth, Globals.gridlineWidth, Globals.toColor(Globals.chartLineColor)));
				pane.getChildren().add(Style.formatRectangle(Globals.chartX + (Globals.chartWidth*(i+0.5)/5) ,Globals.graphAxesMenuHeight, Globals.gridlineWidth, Globals.chartHeight, Globals.toColor(Globals.chartLineColor)));
				pane.getChildren().add(Style.formatLabel((minX*(4-i)/4+maxX*(i)/4)+"", Globals.chartX + (Globals.chartWidth*i/5) ,Globals.chartHeight + Globals.graphAxesMenuHeight, Globals.chartWidth/5, Globals.chartXScale, true));
				pane.getChildren().add(Style.formatLabel((minY*(i)/4+maxY*(4-i)/4)+"", Globals.chartYLabelHeight , Globals.graphAxesMenuHeight + (Globals.chartHeight*i/5), Globals.chartYScale, Globals.chartHeight/5, true, true));
			}
			for(File f : tabs.keySet())
			{
				if(tabs.get(f).inputs.containsKey(in) && tabs.get(f).outputs.containsKey(out))
				{
					pane.getChildren().add(Style.formatCircle(Globals.chartX + (Globals.chartWidth*(getPercent(minX, maxX, tabs.get(f).inputs.get(in))+0.5)/5) - Globals.pointDiameter/2, Globals.graphAxesMenuHeight + (Globals.chartHeight*(4-getPercent(minY, maxY, tabs.get(f).outputs.get(out))+0.5)/5) - Globals.pointDiameter/2, Globals.pointDiameter, Globals.pointDiameter, Globals.toColor(Globals.pointColor)));
				}
			}
		}
		outer.getChildren().setAll(pane);
		inprogress = false;
		return outer;
	}
	public double getPercent(double min, double max, double val)
	{
		if(max - min < Globals.threshold)
			return 2;
		return (val-min)*4.0/(max-min);
	}
}
