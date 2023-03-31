import java.util.Scanner;

public class taksimetre{
    public static void main(String[] args) {
        double total=10;
        double km=0;
        double perKm=2.20;
        Scanner scan= new Scanner(System.in);
        System.out.println("Mesafeyi km cinsinden giriniz: ");
        km= scan.nextInt();
        
        total += (km * perKm);
        total= (total<20)? 20 : total;
        System.out.println(total);     
    }
}