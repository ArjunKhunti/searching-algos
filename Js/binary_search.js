function binarySearch(arr, element) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    mid = Math.floor((left + right) / 2);

    if (arr[mid] == element) {
      return mid;
    }

    if (arr[mid] > element) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return -1;
}

let list = [10, 20, 30, 40, 50, 60, 70, 80, 90];
let find = 640;

let position = binarySearch(list, find);

position == -1
  ? console.log("Element is not present in given list.")
  : console.log("Element is presented at " + (position + 1) + " position.");
