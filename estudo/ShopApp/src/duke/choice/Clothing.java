package duke.choice;

public class Clothing {
    
    private String description;
    private double price;
    private String size = "M";
    
    private final double MIN_TAX =  0.2;
    private final double MIN_PRICE = 10.0;

    public Clothing(String description, double price, String size) {
        this.description = description;
        this.price = price;
        this.size = size;
    }
    
    public void setDescription(String description){
        this.description = description;
    }
    
    public String getDescription(){
        return description;
    }
    
    public void setPrice(double price){
        this.price = (price > MIN_PRICE) ? price : MIN_PRICE;
    }
    
    public double getPrice(){
        return price + (price * MIN_TAX);
    }
        
}
