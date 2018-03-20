import java.util.*;
import javafx.application.Application;
import javafx.stage.*;
import javafx.stage.FileChooser.ExtensionFilter;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.control.*;
import javafx.scene.canvas.*;
import javafx.scene.text.*;
import javafx.scene.paint.*;
public class Main extends Application
{
	public static void main(String[] args)
	{
		if(args.length > 0)
			Globals.directories = args;
		launch();
	}
	public void start(Stage stage)
	{
		Pane all = new Pane();
		Pane pane = new Pane();
		pane.setLayoutY(Globals.modeHeight);
		Timestep timestep = new Timestep();
		Chart chart = new Chart();
		all.getChildren().add(pane);
		all.getChildren().add(Style.formatButton("Timestep", 0, 0, Globals.width/2, Globals.modeHeight, ()->pane.getChildren().setAll(timestep.getPane())));
		all.getChildren().add(Style.formatButton("Analytics", Globals.width/2, 0,Globals.width/2, Globals.modeHeight, ()->pane.getChildren().setAll(chart.getPane(timestep.tabMap))));
		pane.getChildren().setAll(timestep.getPane());
		Scene scene = new Scene(all, Globals.width, Globals.height);
		scene.getStylesheets().add("style.css");
		stage.setScene(scene);
		stage.setTitle("Visualizer");
		stage.setMaximized(true);
		stage.show();
	}
}
