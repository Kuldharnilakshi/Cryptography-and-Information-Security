import java.util.*;

public class ceaser {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Encryption
         System.out.println("ceaser cipher");
        System.out.println("Enter the string to be encrypted:");
        String str = sc.nextLine();
        System.out.println("Enter the key:");
        int key = sc.nextInt();
        StringBuilder encrypted = new StringBuilder();

        for (char c : str.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isLowerCase(c) ? 'a' : 'A';
                c = (char) ((c - base + key) % 26 + base);
            }
            encrypted.append(c);
        }
        System.out.println("Encrypted string: " + encrypted.toString());

        // Decryption
        sc.nextLine(); // consume leftover newline
        System.out.println("Enter the string to be decrypted:");
        String encryptedStr = sc.nextLine();
        System.out.println("Enter the key for decryption:");
        int decryptKey = sc.nextInt();
        StringBuilder decrypted = new StringBuilder();

        for (char c : encryptedStr.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isLowerCase(c) ? 'a' : 'A';
                c = (char) ((c - base - decryptKey + 26) % 26 + base);
            }
            decrypted.append(c);
        }
        System.out.println("Decrypted string: " + decrypted.toString());
    }
}