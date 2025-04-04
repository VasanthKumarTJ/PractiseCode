public class swap_shortcut {
    public static void main(String[] args) {
       int a = 5;
       int b = 10;
       a = a + b - (b = a);
       System.out.println(" a: " + a + ", b: " + b); // Output: a: 10, b: 5
    }
}
