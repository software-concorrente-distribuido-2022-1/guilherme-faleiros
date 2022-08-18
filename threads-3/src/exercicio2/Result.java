package exercicio2;

public class Result {
    private int wantedIndex = -1;
    private boolean completed = false;

    public synchronized void setWantedIndex(int wantedIndex) {
        if(!this.completed) {
            this.wantedIndex = wantedIndex;
            this.completed = true;
        }
    }

    public synchronized int getWantedIndex() {
        return wantedIndex;
    }

    public synchronized boolean isCompleted() {
        return completed;
    }
}
