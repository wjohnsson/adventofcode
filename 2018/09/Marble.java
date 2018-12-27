public class Marble {

    public int value;
    public Marble next;
    public Marble prev;

    public Marble(int value, Marble next, Marble prev) {
        this.value = value;
        this.next = next;
        this.prev = prev;
    }

}
