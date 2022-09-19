package duke.choice;

public class Customer {

    private String name;
    private String size = "M";

    private Clothing[] items;

    public Customer(String name, int meansurement) {
        this.name = name;
        setSize(meansurement);
    }

    public void addItems(Clothing[] someItems) {
        items = someItems;
    }

    public Clothing[] getItems() {
        return items;
    }

    public double getTotalClothingCost() {
        double total = 0.0;

        for (Clothing item : items) {
            total = total + item.getPrice();
        }

        return total;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public String getSize() {
        return size;
    }

    public void setSize(int meansurement) {
        switch (meansurement) {
            case 1:
            case 2:
            case 3:
                size = "S";
                break;
            case 4:
            case 5:
            case 6:
                size = "M";
                break;
            case 7:
            case 8:
            case 9:
                size = "L";
                break;
            default:
                size = "XL";
        }

    }
}
