public class InterpolationSearch {
    private static int interpolationSearch(int[] arr, int find) {
        int left = 0;
        int right = arr.length - 1;

        while (left <= right & find >= arr[left] & arr[right] >= find) {
            int index = left + ((right - left) / (arr[right] - arr[left]) * (find - arr[left]));

            if (arr[index] == find) {
                return index;
            }

            if (arr[index] < find) {
                left = index + 1;
            } else {
                right = index - 1;
            }

        }
        return -1;
    }

    public static void main(String[] args) {
        int arr[] = { 10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47 };
        int find = 242;

        int position = interpolationSearch(arr, find);

        if (position == -1) {
            System.out.println("Element is not present in given list.");
        } else {
            System.out.println("Element is presented at " + (position + 1) + " position.");
        }
    }

}
