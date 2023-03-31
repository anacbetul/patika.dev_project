import java.util.Scanner;

public class hipotenus {
    public static void main(String[] args) {
        double kenar1, kenar2;
        double hipo, alan;
        Scanner scan= new Scanner(System.in);

        System.out.print("1. Kenar uzunluğunu giriniz: ");
        kenar1=scan.nextDouble();

        System.out.print("2. Kenar uzunluğunu giriniz: ");
        kenar2=scan.nextDouble();

        hipo= Math.sqrt( (kenar1*kenar1) + (kenar2*kenar2) );
        System.out.println("Hipotenüs: " + hipo);

        alan = (kenar1 * kenar2) / 2 ;
        System.out.println("Alan: " + alan);
    }

    


}
