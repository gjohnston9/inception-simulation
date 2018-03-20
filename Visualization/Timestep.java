import javafx.scene.layout.Pane;
import javafx.scene.layout.HBox;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.ScrollPane.ScrollBarPolicy;
import javafx.scene.Node;
import javafx.scene.control.ScrollBar;
import javafx.application.Platform;
import java.io.File;
import java.util.HashMap;
import java.util.Set;
public class Timestep
{
	private HBox fileButtons;
	private ScrollPane scrollPane;
	private int pos = 0;
	private HashMap<File, Tab> tabMap = new HashMap<>();
	private Pane contentPane;
	public void update()
	{
		while(true)
		{
			for(String s : Globals.directories)
			{
				File[] listOfFiles = new File(s).listFiles();
				for(File f : listOfFiles)
				{
					if(!tabMap.containsKey(f))
					{
						try
						{
							Tab t = new Tab(f);
							tabMap.put(f, t);
							Platform.runLater(()->
							{
								String fname = f.getName();
								fileButtons.getChildren().add(Style.formatButton(fname.substring(0, fname.indexOf(".")), 0, 0, Globals.tabWidth, Globals.tabHeight, ()->{
									contentPane.getChildren().setAll(t.createPane());
								}));
							});
						}
						//If a file isn't written enough to be read at all
						catch(IllegalArgumentException e)
						{}
					}
					else if(tabMap.get(f).getTimeRead() < f.lastModified())
					{
						Platform.runLater(()->
						{
							tabMap.get(f).update();
						});
					}
				}
			}
			try
			{
				Thread.sleep(Globals.updateTime);
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
		
		contentPane = new Pane();
		contentPane.setLayoutY(Globals.tabHeight);
		contentPane.setPrefHeight(Globals.contentHeight);
		contentPane.setMaxHeight(Globals.contentHeight);
		contentPane.setMinHeight(Globals.contentHeight);
		contentPane.setPrefWidth(Globals.width);
		contentPane.setMaxWidth(Globals.width);
		contentPane.setMinWidth(Globals.width);
		
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
		p.getChildren().add(scrollPane);
		p.getChildren().add(contentPane);
		return p;
	}
}
