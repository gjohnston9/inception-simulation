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
	private ComboBox<String> inbox = Style.formatComboBox(Globals.axisHeight, ()->getPane(tabs));
	private ComboBox<String> outbox = Style.formatComboBox(Globals.axisHeight, ()->getPane(tabs));
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
		hbox.getChildren().add(Style.formatLabel("Displaying ", Globals.axisHeight));
		HashSet<String> set = new HashSet<>();
		for(File f : tabs.keySet())
		{
			set.addAll(tabs.get(f).inputs.keySet());
		}
		String[] list = set.toArray(new String[]{});
		Arrays.sort(list);
		inbox.getItems().setAll(list);
		hbox.getChildren().add(inbox);
		hbox.getChildren().add(Style.formatLabel(" versus ", Globals.axisHeight));
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
		outer.getChildren().setAll(pane);
		inprogress = false;
		return outer;
	}
}
