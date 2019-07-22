import java.util.*;

public class Template {

    void run() {
        Scanner sc = new Scanner(System.in);

        // write your code
        System.out.println("Hello World");
    }

    void debug(Object... os) {
        System.err.println(Arrays.deepToString(os));
    }

    public static void main(String[] args) {
        new Template().run();
    }
}
