package exercicio2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) throws InterruptedException {
        parallelSearch( 1, new Integer[] {1, 3, 2, 1, 5, 6, 7, 8, 1, 1}, 2);
    }

    public static int parallelSearch(int x, Integer[] A, int numThreads) throws InterruptedException {
        var lists = splitIntoParts(A, numThreads);
        var result = new Result();
        List<Finder> workerThreads = new ArrayList<>();
        for (var list : lists) {
            var thread = new Finder(result, list, x);
            workerThreads.add(thread);
            thread.start();
        }

        for (var t : workerThreads) {
            t.join();
        }

        System.out.println("Indice: " + result.getWantedIndex());
        return result.getWantedIndex();
    }

    public static List<List<Unit>> splitIntoParts(Integer[] array, Integer parts) {
        List<Integer> list = Arrays.asList(array);
        List<List<Unit>> listOfLists = new ArrayList<>();
        for (int i = 0; i < parts; i++) {
            listOfLists.add(new ArrayList<>());
        }
        var total = list.size();
        var currentIndex = 0;
        while (total > 0) {
            for (var currentList : listOfLists) {
                if(currentIndex < list.size()) {
                    currentList.add(new Unit(list.get(currentIndex), currentIndex));
                }
                currentIndex++;
                total--;
            }
        }
        return listOfLists;
    }

}
