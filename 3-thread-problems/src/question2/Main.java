package question2;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        var fruits = List.of("Banana", "Laranja", "Maçã", "Melancia", "Coco");
        fruits.forEach(fruit -> new FruitPrinter(fruit).start());
    }

}
