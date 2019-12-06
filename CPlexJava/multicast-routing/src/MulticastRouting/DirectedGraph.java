package MulticastRouting;

public class DirectedGraph {
	public int numVertex;
	public int numEdge;
	public int[][] weight;
	
	public void updateEdgesWeight() {
		for (int k = 0; k < numVertex; k++) {
			for (int i = 0; i < numVertex; i++) {
				for (int j = 0; j < numVertex; j++) {
					weight[i][j] = Math.min(weight[i][j], weight[i][k] + weight[k][j]);
				}
			}
		}
	}
}
