import javafx.scene.control.*;
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
	public static interface Action
	{
		public void act();
	}
	public static String rgbToHex(int[] rgb)
	{
		return String.format("%02x%02x%02x", rgb[0], rgb[1], rgb[2]);
	}
}
