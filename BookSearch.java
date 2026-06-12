import java.util.ArrayList;
import java.util.Scanner;

public class BookSearch {

    public static void main(String[] args) {

        // Create ArrayList to store book titles
        ArrayList<String> books = new ArrayList<>();

        // Add at least 5 books
        books.add("Introduction to Java Programming");
        books.add("Data Structures and Algorithms");
        books.add("Operating System Concepts");
        books.add("Computer Networks");
        books.add("Artificial Intelligence Basics");
        books.add("Advanced Java Techniques");

        // Display all books
        System.out.println("Available Books:");
        for (String book : books) {
            System.out.println("- " + book);
        }

        // Take input from user
        Scanner sc = new Scanner(System.in);
        System.out.print("\nEnter a word to search: ");
        String word = sc.nextLine();

        // Search for matching books
        System.out.println("\nSearch Results:");

        boolean found = false;

        for (String book : books) {
            if (book.toLowerCase().contains(word.toLowerCase())) {
                System.out.println(book);
                found = true;
            }
        }

        // If no book found
        if (!found) {
            System.out.println("No book found containing the word: " + word);
        }

        sc.close();
    }
}

