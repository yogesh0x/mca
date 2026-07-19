public class Assign1{
	public static void main(String args[]) {
    
   double itemPrice = 10.00;
   int numberOfItems = 5 ;
   double taxRate = 8.0/100.00;
   double discountPercentage = 10.0/100.00;

   
   double subtotal = numberOfItems * itemPrice ;

   System.out.println("Here is the Sub-total: "+subtotal);

   double discountAmount = subtotal*discountPercentage;
   System.out.println("Here is the Discount amount: "+discountAmount);

   double taxAmount = (subtotal-discountAmount)*taxRate;
   System.out.println("Here is the Tax amount: "+taxAmount);
  
   double totalCost = (subtotal-discountAmount)+taxAmount;
   System.out.println("Here is the Total cost: "+totalCost);


	}
}