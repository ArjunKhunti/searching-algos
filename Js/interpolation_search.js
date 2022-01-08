function interpolation_search(arr, find) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right && find >= arr[left] && find <= arr[right]) {
    let index =
      left +
      Math.floor(
        ((right - left) / (arr[right] - arr[left])) * (find - arr[left])
      );

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

let arr = new Array(10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47);
let find = 22;

let position = interpolation_search(arr, find);
position == -1
  ? console.log("Element was not present in given list.")
  : console.log("Element is presented at " + (position + 1) + " position.");
