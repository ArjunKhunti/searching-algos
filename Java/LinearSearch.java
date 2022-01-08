class LinearSearch {

    public static int search(int arr[], int element) {
        int length = arr.length;
        for (int i = 0; i < length; i++) {
            if (arr[i] == element) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int arr[] = { 12, 65, 78, 34, 73, 81, 51, 89 };
        int find = 73;

        int position = search(arr, find);

        if (position == -1) {
            System.out.println("Element is not present in given list.");
        } else {
            System.out.println("Element is presented at " + (position + 1) + " position.");
        }
    }
}