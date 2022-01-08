import java.lang.Math;

public class JumpSort {
    private static int jumpSort(int[] arr, int find) {

        int length = arr.length;
        double step = Math.sqrt(length);

        int prev = 0;

        while (arr[(int) Math.min(step, length) - 1] < find) {
            prev = (int) step;
            step += Math.sqrt(length);

            if (prev >= find) {
                return -1;
            }
        }

        while (arr[prev] < find) {
            prev += 1;

            if (prev == Math.min(step, length)) {
                return -1;
            }
        }

        if (arr[prev] == find) {
            return prev;
        }

        return -1;
    }

    public static void main(String[] args) {
        int arr[] = { 10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47 };
        int find = 22;

        int position = jumpSort(arr, find);

        if (position == -1) {
            System.out.println("Element is not present in given list.");
        } else {
            System.out.println("Element is presented at " + (position + 1) + " position.");
        }
    }

}
