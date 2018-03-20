import javafx.scene.control.*;
import javafx.scene.paint.Color;
import javafx.scene.shape.*;
public class Style
{
	public static Button formatButton(String label, double x, double y, double w, double h, Action act)
	{
		Button b = new Button(label);
		b.setLayoutX(x);
		b.setLayoutY(y);
		b.setPrefWidth(w);
		b.setMinWidth(w);
		b.setMaxWidth(w);
		b.setPrefHeight(h);
		b.setMaxHeight(h);
		b.setMinHeight(h);
		b.setOnAction(a->act.act());
		return b;
	}
	public static ComboBox<String> formatComboBox(double h, Action act)
	{
		ComboBox<String> b = new ComboBox<>();
		b.setPrefHeight(h);
		b.setMaxHeight(h);
		b.setMinHeight(h);
		b.setOnAction(a->act.act());
		return b;
	}
	public static Label formatLabel(String label, double h)
	{
		Label b = new Label(label);
		b.setPrefHeight(h);
		b.setMaxHeight(h);
		b.setMinHeight(h);
		return b;
	}
	public static Label formatLabel(String label, double x, double y, double w, double h)
	{
		Label b = new Label(label);
		b.setLayoutX(x);
		b.setLayoutY(y);
		b.setPrefWidth(w);
		b.setMinWidth(w);
		b.setMaxWidth(w);
		b.setPrefHeight(h);
		b.setMaxHeight(h);
		b.setMinHeight(h);
		return b;
	}
	public static Rectangle formatRectangle(double x, double y, double w, double h, Color fill)
	{
		Rectangle b = new Rectangle();
		b.setLayoutX(x);
		b.setLayoutY(y);
		b.setWidth(w);
		b.setHeight(h);
		b.setFill(fill);
		return b;
	}
	public static Ellipse formatCircle(double x, double y, double w, double h, Color fill)
	{
		return formatCircle(x, y, w, h, fill, false);
	}
	public static Ellipse formatCircle(double x, double y, double w, double h, Color fill, boolean border)
	{
		Ellipse b = new Ellipse();
		b.setLayoutX(x + w/2);
		b.setLayoutY(y + h/2);
		b.setRadiusX(w/2);
		b.setRadiusY(h/2);
		if(border)
			b.setStroke(Globals.toColor(Globals.borderColor));
		b.setFill(fill);
		return b;
	}
	public static interface Action
	{
		public void act();
	}
	public static String rgbToHex(int[] rgb)
	{
		return String.format("%02x%02x%02x", rgb[0], rgb[1], rgb[2]);
	}
}
