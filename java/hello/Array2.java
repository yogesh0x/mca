public class Array2 {
  public static void main(String[] args) {
    int st_marks[][] = {
      {98, 45, 75, 79, 68, 98},
      {88, 65, 45, 78, 78, 98},
      {78, 95, 75, 78, 78, 98},
      {78, 45, 45, 68, 78, 48}
    };

    for (int i = 0; i < st_marks.length; i++) {
      int sum = 0;
      for (int j = 0; j < st_marks[i].length; j++) {
        sum += st_marks[i][j];
      }
      System.out.println("Marks of student " + i + " is " + sum);
      float avg;
      avg = (float) sum / st_marks[i].length;
      System.out.println("Percent of student " + i + " is " + avg);
    }
  }
}