class BinarySearch {

    public static int binarySearch(int list[], int element) {

        int left = 0;
        int right = list.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (list[mid] == element) {
                return mid;
            }

            if (list[mid] > element) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int arr[] = { 10, 20, 30, 40, 50, 60, 70, 80, 90 };
        int find = 620;

        int position = binarySearch(arr, find);

        if (position == -1) {
            System.out.println("Element is not present in given list");
        } else {
            System.out.println("Element is presented at " + (position + 1) + " position.");
        }
    }
}