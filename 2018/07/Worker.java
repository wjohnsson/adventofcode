public class Worker {

    private int timeLeft;
    private Step currentStep;
    // Work work!
    public boolean workDone;

    public Worker() {
        timeLeft = 0;
        currentStep = null;
        workDone = false;
    }

    public void assignWork(Step s) {
        currentStep = s;
        timeLeft = s.getTime();
    }

    public void updateTime() {
        timeLeft--;

        if (timeLeft == 0) {
            workDone = true;
        }
    }

    public boolean isWorkDone() {
        return workDone;
    }

    public boolean isWorking() {
        return timeLeft != 0;
    }

    public Step getCurrentStep() {
        return currentStep;
    }
}
