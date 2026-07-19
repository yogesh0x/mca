class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread is running by extending Thread class.");
    }
}

public class Mai {
    public static void main(String[] args) {
        // Create an object of the MyThread class
        MyThread thread = new MyThread();
        
        // Start the thread
        thread.start();
    }
}