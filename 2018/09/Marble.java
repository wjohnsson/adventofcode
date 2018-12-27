public class Marble {

    public Long value;
    public Marble next;
    public Marble prev;

    public Marble(Long value, Marble next, Marble prev) {
        this.value = value;
        this.next = next;
        this.prev = prev;
    }

}
