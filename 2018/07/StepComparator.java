import java.util.Comparator;

public class StepComparator implements Comparator<Step> {
    @Override
    public int compare(Step step1, Step step2) {
        return step1.toString().compareTo(step2.toString());
    }
}
