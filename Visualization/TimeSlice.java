import javafx.scene.layout.Pane;
import java.util.ArrayList;
public class TimeSlice
{
	public final String timestamp;
	
// 	public double percentl;
// 	public double percentc;
// 	public double percentr;

	private double cellwidth;
	private double cellheight;
	public ArrayList<Person> people = new ArrayList<>();
	public TimeSlice(String text, double width, double height)
	{
		cellwidth = width;
		cellheight = height;
		String[] parts = text.split(":");
		timestamp = parts[0];

// 		parts = parts[1].split("/");
// 		percentl = Double.parseDouble(parts[0]);
// 		percentc = Double.parseDouble(parts[1]);
// 		percentr = Double.parseDouble(parts[2]);
// 		double t = percentc + percentl + percentr;
// 		if(t < 0.00001)
// 		{
// 			percentl = percentc = percentr = t = 1;
// 		}
// 		percentc/=t;
// 		percentl/=t;
// 		percentr/=t;

		parts = parts[1].split("\\)");
		for(int i = 0; i < parts.length; i++)
		{
			people.add(new Person(parts[i].substring(1).split(",")));
		}
	}
	public void applyTo(Pane pane)
	{
		for(Person p: people)
		{
			pane.getChildren().add(Style.formatCircle(Globals.gridPadding + cellwidth*p.x, Globals.gridPadding + cellheight*p.y, cellwidth-Globals.gridPadding*2, cellheight-Globals.gridPadding*2,
				Globals.toColor(Globals.getColor(p.v))));
			pane.getChildren().add(Style.formatLabel(p.label, Globals.gridPadding + cellwidth*p.x, Globals.gridPadding + cellheight*p.y, cellwidth-Globals.gridPadding*2, cellheight-Globals.gridPadding*2,
						Globals.getDiplomacyColor(p.diplomacy), Globals.labelSize));
		}
	}
	public class Person
	{
		public final int x;
		public final int y;
		public final double v;
		public double diplomacy = 0;
		public String label = "";
		public Person(String... parts)
		{
			this.x = Integer.parseInt(parts[0]);
			this.y = Integer.parseInt(parts[1]);
			this.v = Double.parseDouble(parts[2]);
			if(parts.length == 5)
			{
				this.diplomacy = Double.parseDouble(parts[3]);
				label = Globals.toString(Integer.parseInt(parts[4]));
			}
		}
	}
}
