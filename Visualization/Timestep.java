import javafx.scene.layout.Pane;
import javafx.scene.layout.HBox;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.ScrollPane.ScrollBarPolicy;
import javafx.scene.Node;
import javafx.scene.control.ScrollBar;
import java.util.Set;
public class Timestep
{
	private HBox fileButtons;
	private ScrollPane scrollPane;
	private int pos = 0;
	public void update()
	{
		while(true)
		{
			try
			{
				Thread.sleep(1000);
			}
			catch(Exception e){}
		}
	}
	public Timestep()
	{        
		fileButtons = new HBox();
		fileButtons.setPrefHeight(Globals.tabHeight);
		fileButtons.setMaxHeight(Globals.tabHeight);
		fileButtons.setMinHeight(Globals.tabHeight);
		
		scrollPane = new ScrollPane();
		scrollPane.setVbarPolicy(ScrollBarPolicy.NEVER);
		scrollPane.setHbarPolicy(ScrollBarPolicy.AS_NEEDED);
		scrollPane.setPannable(false);
		scrollPane.setMaxWidth(Globals.width);
		scrollPane.setMinWidth(Globals.width);
		scrollPane.setPrefWidth(Globals.width);
		scrollPane.setMaxHeight(Globals.tabHeight);
		scrollPane.setMinHeight(Globals.tabHeight);
		scrollPane.setPrefHeight(Globals.tabHeight);
		scrollPane.setContent(fileButtons);
		scrollPane.setVmin(0);
		scrollPane.setVmax(0);
		scrollPane.setOnScroll(event->
		{
			if(event.getDeltaX() == 0 && event.getDeltaY() != 0) {
				scrollPane.setHvalue(scrollPane.getHvalue() - event.getDeltaY() / fileButtons.getWidth());
				event.consume();
			}
		});

		Thread thread = new Thread(()->update());
		thread.setDaemon(true);
		thread.start();
	}
	public Pane getPane()
	{
		Pane p  = new Pane();
		fileButtons.getChildren().add(Style.formatButton("Test", 0, 0, Globals.tabWidth, Globals.tabHeight, ()->{}));
		p.getChildren().add(scrollPane);
		return p;
	}
}
