package MulticastRouting;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class IO {
	public void inputGraph(String inputPath, DirectedGraph graph) {

		File inputFile = new File(inputPath);
		
		try {
			Scanner sc = new Scanner(inputFile);
			graph.numVertex = sc.nextInt();
			graph.numEdge = sc.nextInt();
			sc.close();		
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
	}
}
